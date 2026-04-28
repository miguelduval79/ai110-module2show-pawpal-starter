from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Miguel")

dog = Pet("Max", "Dog", 3)
cat = Pet("Luna", "Cat", 2)

dog.add_task(Task("Morning walk", "Walk", 30, 1, "08:00"))
dog.add_task(Task("Feed breakfast", "Feeding", 10, 2, "07:30"))
cat.add_task(Task("Give medication", "Medication", 5, 1, "09:00"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler()
schedule = scheduler.generate_schedule(owner)

print("Today's Schedule")
print("----------------")

for pet_name, task in schedule:
    status = "Done" if task.completed else "Pending"
    print(
        f"{task.due_time} | {pet_name} | {task.title} "
        f"| Type: {task.task_type} | Duration: {task.duration} min "
        f"| Priority: {task.priority} | {status}"
    )