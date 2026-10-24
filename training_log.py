import sqlite3
from pathlib import Path
from datetime import date

database_path = Path(__file__).parent / "training_log.db"

exercise_names = [
    "Military Press",
    "Weighted Row",
    "Bicep Curl",
    "Tricep Ext",
    "Cross Body Curl",
    "Front Raise",
    "Side Raise",
    "Back Raise",
    "Dumbbell Pullover",
    "Dumbbell Flye",
    "Weighted Squat",
    "Deadlift"
]

with sqlite3.connect(database_path) as connection:
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("""
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
    """)
    for name in exercise_names:
        connection.execute(
            "INSERT OR IGNORE INTO exercises (name) VALUES (?)",
            (name,)
        )
        connection.execute("""
        CREATE TABLE IF NOT EXISTS workout_sets (
            id INTEGER PRIMARY KEY,
            exercise_id INTEGER NOT NULL,
            workout_date TEXT NOT NULL,
            weight_lb REAL NOT NULL CHECK (weight_lb >= 0),
            reps INTEGER NOT NULL CHECK (reps > 0),
            FOREIGN KEY (exercise_id) REFERENCES exercises(id)
        )
    """)

    search = input(
        "Search exercises (press Return for all): "
    ).strip()

    exercises = connection.execute("""
        SELECT id, name
        FROM exercises
        WHERE name LIKE ?
        ORDER BY id
    """, ("%" + search + "%",)).fetchall()
    
print()

if search:
    print(f'Exercises matching "{search}"')
else:
    print("All exercises")

print()

if len(exercises) == 0:
    print("No matching exercises found.")
else:
    for exercise in exercises:
        print(f"{exercise[0]}: {exercise[1]}")

print()
print("Matching exercises:", len(exercises))

print()
record_set = input("Record a new set? (y/n): ").strip().lower()

if record_set == "y":
    print("Record a set")

    try:
        exercise_id = int(input("Exercise ID: "))
        weight_lb = float(input("Weight used (lb): "))
        reps = int(input("Reps completed: "))

    except ValueError:
        print("Enter whole numbers for ID and reps, and a number for weight.")

    else:
        if weight_lb < 0 or reps <= 0:
            print("Weight cannot be negative, and reps must be greater than zero.")
        else:
            workout_date = date.today().isoformat()

            with sqlite3.connect(database_path) as connection:
                connection.execute("PRAGMA foreign_keys = ON")

                exercise = connection.execute(
                    "SELECT name FROM exercises WHERE id = ?",
                    (exercise_id,)
                ).fetchone()

                if exercise is None:
                    print("That exercise ID does not exist.")
                else:
                    connection.execute("""
                        INSERT INTO workout_sets (
                            exercise_id, workout_date, weight_lb, reps
                        )
                        VALUES (?, ?, ?, ?)
                    """, (
                        exercise_id,
                        workout_date,
                        weight_lb,
                        reps
                    ))

        if exercise is not None:
            print("Set saved!")
            
print()
print("Saved sets")

with sqlite3.connect(database_path) as connection:
    saved_sets = connection.execute("""
        SELECT workout_sets.workout_date,
               exercises.name,
               workout_sets.weight_lb,
               workout_sets.reps
        FROM workout_sets
        JOIN exercises
            ON workout_sets.exercise_id = exercises.id
        ORDER BY workout_sets.workout_date DESC,
                 workout_sets.id DESC
    """).fetchall()

if len(saved_sets) == 0:
    print("No sets recorded yet.")
else:
    for saved_set in saved_sets:
        workout_date, exercise_name, weight_lb, reps = saved_set

        print(
            f"{workout_date} | {exercise_name} | "
            f"{weight_lb:g} lb × {reps} reps"
        )