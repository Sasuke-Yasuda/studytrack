
import json
import re
from pathlib import Path

# Location of our homework storage file
TASKS_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    """Load homework assignments from the JSON file."""

    if not TASKS_FILE.exists():
        return []

    with open(TASKS_FILE, "r") as file:
        return json.load(file)
    
def view_tasks():
    """Return all saved homework assignments."""

    return load_tasks()

def save_tasks(tasks):
    """Save homework assignments to the JSON file."""

    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    """Add a new homework assignment."""

    # Reject empty or whitespace-only assignments
    if not isinstance(description, str) or not re.search(r"\S", description):
        raise ValueError("Assignment cannot be empty.")

    # Load existing assignments
    tasks = load_tasks()

    # Generate a unique ID
    new_id = max((task["id"] for task in tasks), default=0) + 1

    # Create the new assignment
    new_task = {
        "id": new_id,
        "description": description.strip()
    }

    # Add and save the assignment
    tasks.append(new_task)
    save_tasks(tasks)

    return new_task
