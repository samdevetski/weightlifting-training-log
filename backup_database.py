import sqlite3
from pathlib import Path
from datetime import datetime

project_folder = Path(__file__).parent
database_path = project_folder / "training_log.db"

if not database_path.exists():
    print("No training database found. Run training_log.py first.")
else:
    backup_folder = project_folder / "backups"
    backup_folder.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    backup_path = backup_folder / f"training_log_{timestamp}.db"

    with sqlite3.connect(database_path) as source:
        with sqlite3.connect(backup_path) as destination:
            source.backup(destination)

            for table in ("exercises", "workout_sets"):
                original_count = source.execute(
                    f"SELECT COUNT(*) FROM {table}"
                ).fetchone()[0]

                backup_count = destination.execute(
                    f"SELECT COUNT(*) FROM {table}"
                ).fetchone()[0]

                print(
                    f"{table}: original={original_count}, "
                    f"backup={backup_count}"
                )

    print("Backup created:", backup_path)