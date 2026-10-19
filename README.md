# Weightlifting Training Log

A Python and SQLite project for building a personal weightlifting
training log. This first version stores an exercise library.

## Features

- Creates a local SQLite database automatically.
- Adds 12 starter exercises.
- Displays exercises in their original insertion order.
- Prevents duplicate exercise names across repeated runs.
- Displays the total number of exercises.

## Requirements

Python 3. No additional packages required.

## How to run

Open a terminal in the project folder:

```bash
python3 training_log.py
```

The program creates training_log.db alongside the script
on its first run.

## Starter exercises

1. Military Press
2. Weighted Row
3. Bicep Curl
4. Tricep Ext
5. Cross Body Curl
6. Front Raise
7. Side Raise
8. Back Raise
9. Dumbbell Pullover
10. Dumbbell Flye
11. Deadlift
12. Weighted Squat

## Database structure

The exercises table contains:

- id: an integer primary key.
- name: a required, unique exercise name.

INSERT OR IGNORE prevents duplicate names.
SELECT retrieves the exercises, and ORDER BY id preserves
their original insertion order.

## Checks performed

- Confirmed all 12 exercises display in the intended order.
- Ran the program again and confirmed the total remained 12.
- Confirmed the database is excluded from Git.

## Data storage

training_log.db stays on the computer running the program
and is excluded from Git using .gitignore.

Cloning the repository creates a new exercise database when
the script runs; it does not copy an existing database.

## What I practiced

- Creating an SQLite table from Python.
- Inserting records using parameterized SQL.
- Preventing duplicates with a UNIQUE constraint.
- Retrieving and ordering records.
- Processing query results with a loop.

## Current limitations

- No workout dates, sets, reps, or weights are recorded yet.
- Exercise names are defined in the source code.
- Changing the source list order does not reorder existing records.
- Runs in the terminal; phone access is a future improvement.