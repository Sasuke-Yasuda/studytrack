
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

def update_task(task_id, new_description):
    """Update an existing homework assignment."""

    # Reject empty descriptions
    if not isinstance(new_description, str) or not re.search(r"\S", new_description):
        raise ValueError("Assignment cannot be empty.")

    # Load existing assignments
    tasks = load_tasks()

    # Find the assignment
    for task in tasks:
        if task["id"] == task_id:

            # Update its description
            task["description"] = new_description.strip()

            # Save the updated assignments
            save_tasks(tasks)

            return task

    # If no assignment was found
    raise ValueError("Assignment not found.")