# PawPal+ Project Reflection

No major design changes were made. The initial class structure already aligned well with the requirements and responsibilities of the system.

My initial design includes four main classes: Owner, Pet, Task, and Scheduler.

Owner is responsible for managing pets and stores the owner’s name and a list of pets.

Pet represents each animal and is responsible for managing its care tasks. It stores basic information such as name, species, age, and a list of tasks.

Task represents individual activities such as feeding, walking, medication, or appointments. It stores details such as duration, priority, due time, and whether the task is recurring or completed.

Scheduler is responsible for organizing and managing all tasks. It will handle sorting tasks by priority, detecting conflicts, and generating a daily schedule.

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

1. Add a pet to the system and associate it with an owner.
2. Create and schedule tasks such as feeding, walking, medication, or appointments.
3. View and organize tasks for the day based on time or priority.


- What classes did you include, and what responsibilities did you assign to each?
My initial UML design includes four main classes: Owner, Pet, Task, and Scheduler.

The Owner class represents the user of the system and is responsible for managing pets. It stores basic information such as the owner's name and a list of pets.

The Pet class represents each individual animal and is responsible for managing its associated care tasks. It stores details such as the pet's name, species, and a list of tasks.

The Task class represents individual activities such as feeding, walking, medication, or appointments. It stores information such as the task name, duration, priority, due time, and whether it is recurring.

The Scheduler class is responsible for organizing and managing all tasks. It handles sorting tasks by priority, generating a daily schedule, and detecting conflicts between tasks.

These classes work together to create a modular system where responsibilities are clearly separated and tasks can be efficiently managed and scheduled.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

## 6. Reflection
🐶 Owner

Attributes:

* name
* pets (list of Pet)

Methods:

* add_pet(pet)
* get_pets()

⸻

🐾 Pet

Attributes:

* name
* species
* age
* tasks (list of Task)

Methods:

* add_task(task)
* get_tasks()

⸻

📋 Task

Attributes:

* title
* task_type (feeding, walking, etc.)
* duration
* priority
* due_time
* recurring
* completed

Methods:

* mark_complete()
* update_task()

⸻

🧠 Scheduler

Attributes:

* tasks (list of Task)

Methods:

* add_task(task)
* get_tasks_for_today()
* sort_tasks_by_priority()
* detect_conflicts()
* generate_schedule()p

## AI Strategy Reflection

I used AI as a design and debugging partner, but I kept control of decisions.

Most useful:
- breaking system into Owner, Pet, Task, Scheduler
- generating and refining algorithms

Example I rejected:
- overly complex scheduling suggestions; I kept simple time-based logic for clarity

Using separate phases helped me stay organized:
- design → backend → tests → UI → algorithms

Main lesson:
Being the lead architect means validating AI output, not blindly accepting it.