from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    task_type: str
    duration: int
    priority: int
    due_time: str
    recurring: bool = False
    completed: bool = False

    def mark_complete(self):
        self.completed = True

    def update_task(self, title=None, due_time=None, priority=None):
        if title is not None:
            self.title = title
        if due_time is not None:
            self.due_time = due_time
        if priority is not None:
            self.priority = priority


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_pets(self):
        return self.pets

    def get_all_tasks(self):
        all_tasks = []
        for pet in self.pets:
            for task in pet.get_tasks():
                all_tasks.append((pet.name, task))
        return all_tasks


@dataclass
class Scheduler:
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks_for_today(self, owner):
        return owner.get_all_tasks()

    def sort_tasks_by_priority(self, tasks):
        return sorted(tasks, key=lambda item: item[1].priority)

    def detect_conflicts(self, tasks):
        seen_times = set()
        conflicts = []

        for pet_name, task in tasks:
            if task.due_time in seen_times:
                conflicts.append((pet_name, task))
            else:
                seen_times.add(task.due_time)

        return conflicts

    def generate_schedule(self, owner):
        tasks = self.get_tasks_for_today(owner)
        return sorted(tasks, key=lambda item: item[1].due_time)