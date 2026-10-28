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

    saved_sets = connection.execute("""
        SELECT workout_sets.workout_date AS Date,
               exercises.name AS Exercise,
               workout_sets.weight_lb AS "Weight (lb)",
               workout_sets.reps AS Reps
        FROM workout_sets
        JOIN exercises
            ON workout_sets.exercise_id = exercises.id
        ORDER BY workout_sets.workout_date DESC,
                 workout_sets.id DESC
    """).fetchall()

if not saved_sets:
    st.info("No workout sets recorded yet.")
else:
    st.dataframe(
        [dict(saved_set) for saved_set in saved_sets],
        hide_index=True
    )