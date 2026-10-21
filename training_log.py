import sqlite3
from pathlib import Path

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

    search = input(
        "Search exercises (press Return for all): "
    ).strip()

    exercises = connection.execute("""
        SELECT name
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
        print(exercise[0])

print()
print("Matching exercises:", len(exercises))