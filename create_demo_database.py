import sqlite3
from pathlib import Path

demo_database_path = (
    Path(__file__).parent / "demo_training_log.db"
)

with sqlite3.connect(demo_database_path) as connection:
    connection.execute("PRAGMA foreign_keys = ON")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
    """)

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

    demo_exercises = [
        (1, "Military Press"),
        (2, "Weighted Row"),
        (3, "Bicep Curl")
    ]

    connection.executemany("""
        INSERT OR IGNORE INTO exercises (id, name)
        VALUES (?, ?)
    """, demo_exercises)

    demo_sets = [
        (1, 1, "2026-10-20", 20, 10),
        (2, 1, "2026-10-20", 20, 10),
        (3, 2, "2026-10-20", 30, 12),
        (4, 1, "2026-10-23", 20, 12),
        (5, 1, "2026-10-23", 20, 11),
        (6, 2, "2026-10-23", 30, 12)
    ]

    connection.executemany("""
        INSERT OR IGNORE INTO workout_sets (
            id, exercise_id, workout_date, weight_lb, reps
        )
        VALUES (?, ?, ?, ?, ?)
    """, demo_sets)

print("Fictional demo workouts are ready.")