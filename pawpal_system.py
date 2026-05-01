from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class Task:
    title: str
    task_type: str
    duration: int
    priority: int
    due_time: str
    recurring: str | bool = False
    completed: bool = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def update_task(self, title=None, due_time=None, priority=None):
        """Update task details if new values are provided."""
        if title is not None:
            self.title = title
        if due_time is not None:
            self.due_time = due_time
        if priority is not None:
            self.priority = priority

    def create_next_occurrence(self):
        """Create the next recurring task if recurrence is daily or weekly."""
        if not self.recurring:
            return None

        current_time = datetime.strptime(self.due_time, "%H:%M")

        if self.recurring == "daily":
            next_time = current_time + timedelta(days=1)
        elif self.recurring == "weekly":
            next_time = current_time + timedelta(weeks=1)
        else:
            return None

        return Task(
            title=self.title,
            task_type=self.task_type,
            duration=self.duration,
            priority=self.priority,
            due_time=next_time.strftime("%H:%M"),
            recurring=self.recurring,
        )


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a task to the pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for the pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_pets(self):
        """Return all pets owned by the owner."""
        return self.pets

    def get_all_tasks(self):
        """Return all tasks for all pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.get_tasks():
                all_tasks.append((pet.name, task))
        return all_tasks


@dataclass
class Scheduler:
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a task to the scheduler."""
        self.tasks.append(task)

    def get_tasks_for_today(self, owner):
        """Return all tasks from all pets owned by the owner."""
        return owner.get_all_tasks()

    def sort_by_time(self, tasks):
        """Sort tasks by due time."""
        return sorted(tasks, key=lambda item: item[1].due_time)

    def sort_tasks_by_priority(self, tasks):
        """Sort tasks by priority, with priority 1 treated as highest."""
        return sorted(tasks, key=lambda item: item[1].priority)

    def filter_by_pet(self, tasks, pet_name):
        """Return only tasks for a specific pet."""
        return [
            (name, task)
            for name, task in tasks
            if name.lower() == pet_name.lower()
        ]

    def filter_by_status(self, tasks, completed=False):
        """Return tasks based on completion status."""
        return [
            (name, task)
            for name, task in tasks
            if task.completed == completed
        ]

    def detect_conflicts(self, tasks):
        """Detect tasks scheduled at the same time."""
        seen_times = {}
        conflicts = []

        for pet_name, task in tasks:
            if task.due_time in seen_times:
                conflicts.append(
                    f"Conflict: {task.due_time} is shared by "
                    f"{seen_times[task.due_time]} and {pet_name}"
                )
            else:
                seen_times[task.due_time] = pet_name

        return conflicts

    def generate_schedule(self, owner):
        """Generate a schedule sorted by time."""
        tasks = self.get_tasks_for_today(owner)
        return self.sort_by_time(tasks)