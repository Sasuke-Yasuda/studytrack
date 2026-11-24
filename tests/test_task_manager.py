
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

def test_view_tasks(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    task_manager.add_task("Math homework")
    task_manager.add_task("Science homework")

    tasks = task_manager.view_tasks()

    assert len(tasks) == 2
    assert tasks[0]["description"] == "Math homework"
    assert tasks[1]["description"] == "Science homework"


def test_view_empty_tasks(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    tasks = task_manager.view_tasks()

    assert tasks == []

def test_update_task(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    task = task_manager.add_task("Math homework")

    updated = task_manager.update_task(
        task["id"], "Chemistry homework"
    )

    assert updated["id"] == 1
    assert updated["description"] == "Chemistry homework"


def test_update_preserves_task_id(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    task = task_manager.add_task("Math homework")
    original_id = task["id"]

    updated = task_manager.update_task(original_id, "Science homework")

    assert updated["id"] == original_id


def test_update_rejects_empty_description(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    task = task_manager.add_task("Math homework")

    with pytest.raises(ValueError):
        task_manager.update_task(task["id"], "   ")


def test_update_rejects_missing_id(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    with pytest.raises(ValueError):
        task_manager.update_task(999, "Science homework")

def test_delete_task(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    task = task_manager.add_task("Math homework")

    deleted = task_manager.delete_task(task["id"])

    assert deleted["id"] == 1
    assert deleted["description"] == "Math homework"
    assert task_manager.view_tasks() == []


def test_delete_preserves_other_tasks(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    task_manager.add_task("Math homework")
    task_manager.add_task("Science homework")

    task_manager.delete_task(1)

    tasks = task_manager.view_tasks()

    assert len(tasks) == 1
    assert tasks[0]["id"] == 2
    assert tasks[0]["description"] == "Science homework"


def test_delete_rejects_missing_id(monkeypatch, tmp_path):
    monkeypatch.setattr(
        task_manager, "TASKS_FILE", tmp_path / "tasks.json"
    )

    with pytest.raises(ValueError):
        task_manager.delete_task(999)
