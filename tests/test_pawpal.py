from pawpal_system import Pet, Task


def test_task_completion_changes_status():
    task = Task("Morning walk", "Walk", 30, 1, "08:00")

    task.mark_complete()

    assert task.completed is True


def test_adding_task_increases_pet_task_count():
    pet = Pet("Max", "Dog", 3)
    task = Task("Feed breakfast", "Feeding", 10, 2, "07:30")

    pet.add_task(task)

    assert len(pet.tasks) == 1