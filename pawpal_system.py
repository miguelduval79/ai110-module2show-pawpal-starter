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
        pass

    def update_task(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass

    def get_tasks(self):
        pass


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        pass

    def get_pets(self):
        pass


@dataclass
class Scheduler:
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass

    def get_tasks_for_today(self):
        pass

    def sort_tasks_by_priority(self):
        pass

    def detect_conflicts(self):
        pass

    def generate_schedule(self):
        pass