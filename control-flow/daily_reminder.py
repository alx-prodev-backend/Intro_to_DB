# daily_reminder.py
# Objective: Provide a customized reminder for a single priority task

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process Task Based on Priority Using Match Case (Python 3.10+)
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unspecified priority"

# Modify Reminder if Task is Time-Bound
if time_bound == "yes" and priority in ["high", "medium"]:
    reminder += " that requires immediate attention today!"
elif time_bound == "yes" and priority == "low":
    reminder += ". Consider doing it today if possible."
elif time_bound == "no" and priority in ["high", "medium"]:
    reminder += ". Schedule it as soon as convenient."
else:
    reminder += ". Consider completing it when you have free time."

# Print the Final Reminder
print(reminder)
