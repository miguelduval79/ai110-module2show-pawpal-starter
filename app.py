import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+.

This app connects the Streamlit UI to your backend logic in `pawpal_system.py`.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

with st.expander("What this version does", expanded=True):
    st.markdown(
        """
- Creates an owner
- Creates a pet
- Adds real `Task` objects
- Stores data using `st.session_state`
- Calls your `Scheduler` to generate a schedule
"""
    )

st.divider()

st.subheader("Owner + Pet Info")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_name)

if "pet" not in st.session_state:
    st.session_state.pet = Pet(pet_name, species, 0)
    st.session_state.owner.add_pet(st.session_state.pet)

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

if st.button("Update Owner/Pet"):
    st.session_state.owner = Owner(owner_name)
    st.session_state.pet = Pet(pet_name, species, 0)
    st.session_state.owner.add_pet(st.session_state.pet)
    st.success("Owner and pet updated.")

st.divider()

st.subheader("Tasks")

col1, col2, col3 = st.columns(3)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")

with col2:
    duration = st.number_input(
        "Duration (minutes)",
        min_value=1,
        max_value=240,
        value=20
    )

with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

due_time = st.text_input("Due time", value="09:00", placeholder="Example: 09:00")

if st.button("Add task"):
    priority_map = {
        "high": 1,
        "medium": 2,
        "low": 3,
    }

    new_task = Task(
        title=task_title,
        task_type="general",
        duration=int(duration),
        priority=priority_map[priority],
        due_time=due_time,
    )

    st.session_state.pet.add_task(new_task)
    st.success(f"Task added: {task_title}")

if st.session_state.pet.tasks:
    st.write("Current tasks:")

    task_rows = [
        {
            "title": task.title,
            "duration_minutes": task.duration,
            "priority": task.priority,
            "due_time": task.due_time,
            "completed": task.completed,
        }
        for task in st.session_state.pet.tasks
    ]

    st.table(task_rows)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    schedule = st.session_state.scheduler.generate_schedule(st.session_state.owner)

    if schedule:
        st.success("Schedule generated!")

        schedule_rows = [
            {
                "time": task.due_time,
                "pet": pet_name,
                "task": task.title,
                "duration_minutes": task.duration,
                "priority": task.priority,
                "status": "Done" if task.completed else "Pending",
            }
            for pet_name, task in schedule
        ]

        st.table(schedule_rows)
    else:
        st.info("No tasks available to schedule.")

if st.button("Clear all tasks"):
    st.session_state.pet.tasks = []
    st.success("Tasks cleared.")
    st.rerun()