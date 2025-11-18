# daily_reminder.py

# # Prompt for a Single Task
# task = input("Enter your task: ")
# priority = input("Priority (high/medium/low): ").lower()
# time_bound = input("Is it time-bound? (yes/no): ").lower()
#
# # Provide Customized Reminder
# reminder = f"Reminder: '{task}' is a {priority} priority task"
#
# # Modify based on time-sensitivity
# if time_bound == "yes":
#     reminder += " that requires immediate attention today!"
# else:
#     reminder += ". Consider completing it when you have free time."
#
# # Print the Reminder
# print(reminder)

# daily_reminder.py

# --- 1. Prompt for a Single Task ---
task = input("Enter your task: ")

# Use a loop for input validation (mandatory requirement)
# Loop for priority input until 'high', 'medium', or 'low' is entered
valid_priorities = ['high', 'medium', 'low']
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in valid_priorities:
        break
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

# Loop for time-bound input until 'yes' or 'no' is entered
valid_time_bounds = ['yes', 'no']
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in valid_time_bounds:
        break
    print("Invalid response. Please enter 'yes' or 'no'.")

# --- 2. Process the Task Based on Priority and Time Sensitivity ---
# Initialize the base message
base_message = f"Note: '{task}' is a **{priority}** priority task"
additional_message = ""

# Use a Match Case statement (mandatory requirement)
match priority:
    case 'high':
        # High priority tasks often have a strong call to action
        base_message = f"**Reminder:** '{task}' is a **HIGH** priority task"
    case 'medium':
        # Medium priority tasks suggest scheduled action
        base_message = f"**Heads Up:** '{task}' is a **medium** priority task"
    case 'low':
        # Low priority tasks offer flexibility
        base_message = f"**Note:** '{task}' is a **low** priority task"
    # The default case is technically unnecessary here because the loop ensures valid input,
    # but it's good practice:
    case _:
        base_message = f"'{task}' is a task with an unspecified priority"


# --- 3. Provide a Customized Reminder ---

# Modify the reminder based on time-sensitivity (using an if statement)
if time_bound == "yes":
    # Time-bound tasks require immediate action, overriding the base message conclusion
    additional_message = " **that requires immediate attention today!**"
elif priority == 'low':
    # This specifically addresses the 'low priority' example output
    additional_message = ". Consider completing it when you have free time."
else:
    # Default completion for non-time-bound, medium/high tasks
    additional_message = ". Plan to complete it soon."

# Combine and Print the Final Reminder
final_reminder = base_message + additional_message
print("-" * 40)
print(final_reminder)
print("-" * 40)
