from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion_changes_status():
    task = Task("Morning walk", "Walk", 30, 1, "08:00")

    task.mark_complete()

    assert task.completed is True


def test_adding_task_increases_pet_task_count():
    pet = Pet("Max", "Dog", 3)
    task = Task("Feed breakfast", "Feeding", 10, 2, "07:30")

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_scheduler_sorts_tasks_chronologically():
    owner = Owner("Miguel")
    pet = Pet("Max", "Dog", 3)

    pet.add_task(Task("Night walk", "Walk", 20, 2, "20:00"))
    pet.add_task(Task("Breakfast", "Feeding", 10, 1, "07:00"))
    pet.add_task(Task("Medication", "Medication", 5, 1, "12:00"))

    owner.add_pet(pet)

    scheduler = Scheduler()
    schedule = scheduler.generate_schedule(owner)

    assert schedule[0][1].title == "Breakfast"
    assert schedule[1][1].title == "Medication"
    assert schedule[2][1].title == "Night walk"


def test_daily_recurring_task_creates_next_occurrence():
    task = Task("Morning walk", "Walk", 30, 1, "08:00", recurring="daily")

    next_task = task.create_next_occurrence()

    assert next_task is not None
    assert next_task.title == "Morning walk"
    assert next_task.due_time == "08:00"
    assert next_task.recurring == "daily"
    assert next_task.completed is False


def test_scheduler_detects_duplicate_time_conflict():
    owner = Owner("Miguel")
    dog = Pet("Max", "Dog", 3)
    cat = Pet("Luna", "Cat", 2)

    dog.add_task(Task("Morning walk", "Walk", 30, 1, "08:00"))
    cat.add_task(Task("Medication", "Medication", 5, 1, "08:00"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler()
    tasks = owner.get_all_tasks()
    conflicts = scheduler.detect_conflicts(tasks)

    assert len(conflicts) == 1
    assert "08:00" in conflicts[0]