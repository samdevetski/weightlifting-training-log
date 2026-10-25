# Weightlifting Training Log

A Python and SQLite command-line tool for searching an exercise
library, recording dated weightlifting sets, and viewing saved history.

## Features

- Creates a local SQLite database automatically.
- Adds 12 starter exercises.
- Displays exercises in their original insertion order.
- Prevents duplicate exercise names across repeated runs.
- Displays the total number of exercises.
- Searches exercise names using partial text, ignoring capitalization.
- Shows all exercises when the search is left blank.
- Preserves workout order when displaying matches.
- Displays a friendly message when no exercises match.
- Optionally records a set using an exercise ID, weight in pounds, and reps.
- Automatically dates new sets using the computer's current date.
- Validates numeric input, exercise IDs, nonnegative weight, and positive reps.
- Displays saved sets with exercise names, newest first.
- Preserves workout records between program runs.
- Filters saved workout history by partial exercise name.
- Matches exercise names regardless of capitalization.
- Shows all saved sets when the history search is blank.
- Displays the number of matching sets and handles no matches.
- Summarizes all saved training data by exercise.
- Displays the number of sets and total reps in workout order.

## Requirements

Python 3. No additional packages required.

## How to run

Open a terminal in the project folder:

```bash
python3 training_log.py
```

The program creates training_log.db alongside the script
on its first run.

When prompted, enter part of an exercise name:

```text
Search exercises (press Return for all): curl

Exercises matching "curl"

Bicep Curl
Cross Body Curl

Matching exercises: 2
```

Press Return without entering text to display all exercises.

Search uses a parameterized SQL LIKE query. The % wildcard
matches any sequence of characters; _ matches one character.

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
The workout_sets table stores an ID, exercise ID, workout date,
weight in pounds, and reps. A foreign key links each set to its
exercise. A SQL JOIN retrieves exercise names for the history display.

## Checks performed

- Confirmed all 12 exercises display in the intended order.
- Ran the program again and confirmed the total remained 12.
- Confirmed the database is excluded from Git.
- Confirmed curl and CURL both return two matching exercises.
- Confirmed an empty search displays all 12 exercises in workout order.
- Confirmed swimming returns no matches and a count of zero.
- Confirmed a partial exercise name filters saved history.
- Confirmed uppercase input returns the same matches.
- Confirmed a blank search displays all saved sets.
- Confirmed a search with no matches displays a message and count of zero.
- Compared summary set counts and rep totals with saved history.
- Confirmed viewing history does not change the totals.
- Confirmed the summary is independent of the history filter.

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
- Aggregating records with SQL COUNT, SUM, and GROUP BY.

## Current limitations

- Records one set per program run.
- New sets use today's date; backdated entries are not supported yet.
- Saved sets cannot yet be edited or deleted.
- Weight is recorded as entered; use a consistent convention for
  per-dumbbell versus total weight.
- Exercise names are defined in the source code.
- Changing the source list order does not reorder existing records.
- Runs in the terminal; phone access is a future improvement.

## Filter workout history

After recording or skipping a set, enter part of an exercise name
at the history prompt. For example, curl finds saved sets for
exercises whose names contain curl.

Press Return without typing to display all saved sets.
Results show the newest workout dates and entries first.