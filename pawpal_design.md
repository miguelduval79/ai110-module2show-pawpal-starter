# PawPal UML

Owner → Pets  
Pet → Tasks  
Scheduler → Tasks  

Owner:
- name
- pets
- add_pet()

Pet:
- name
- species
- age
- tasks
- add_task()

Task:
- title
- duration
- priority
- due_time
- recurring
- mark_complete()

Scheduler:
- tasks
- sort_tasks()
- detect_conflicts()
- generate_schedule()