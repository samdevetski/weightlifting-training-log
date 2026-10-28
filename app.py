import sqlite3
from pathlib import Path

import streamlit as st

st.title("Weightlifting Training Log")
st.write("Review your recorded workouts.")

database_path = Path(__file__).parent / "training_log.db"

if not database_path.exists():
    st.warning("No training database found. Record a set using training_log.py first.")
    st.stop()

with sqlite3.connect(
    database_path.resolve().as_uri() + "?mode=ro",
    uri=True
) as connection:
    connection.row_factory = sqlite3.Row

    exercises = connection.execute("""
        SELECT name
        FROM exercises
        ORDER BY id
    """).fetchall()

    exercise_options = ["All exercises"] + [
        exercise["name"] for exercise in exercises
    ]

    selected_exercise = st.selectbox(
        "Choose an exercise",
        exercise_options
    )
    
    saved_sets = connection.execute("""
        SELECT workout_sets.workout_date AS Date,
               exercises.name AS Exercise,
               workout_sets.weight_lb AS "Weight (lb)",
               workout_sets.reps AS Reps
        FROM workout_sets
        JOIN exercises
            ON workout_sets.exercise_id = exercises.id
        WHERE (? = 'All exercises' OR exercises.name = ?)
        ORDER BY workout_sets.workout_date DESC,
                 workout_sets.id DESC
    """, (selected_exercise, selected_exercise)).fetchall()

st.write(f"Matching sets: {len(saved_sets)}")

if not saved_sets:
    st.info("No recorded sets match this selection.")
else:
    st.dataframe(
        [dict(saved_set) for saved_set in saved_sets],
        hide_index=True
    )