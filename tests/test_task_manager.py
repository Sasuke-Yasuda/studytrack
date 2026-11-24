
import pytest
import task_manager


def test_add_task(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    task = task_manager.add_task("Finish Chemistry homework")

    assert task["id"] == 1
    assert task["description"] == "Finish Chemistry homework"


def test_reject_empty_task():
    with pytest.raises(ValueError):
        task_manager.add_task("")


def test_reject_whitespace_task():
    with pytest.raises(ValueError):
        task_manager.add_task("   ")


def test_tasks_are_saved_and_loaded(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    task_manager.add_task("Complete Math homework")

    tasks = task_manager.load_tasks()

    assert len(tasks) == 1
    assert tasks[0]["description"] == "Complete Math homework"


def test_task_ids_are_unique(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    first = task_manager.add_task("Math homework")
    second = task_manager.add_task("Science homework")

    assert first["id"] == 1
    assert second["id"] == 2
