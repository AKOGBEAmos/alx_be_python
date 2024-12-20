#Daily reminder
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print(f"Set a deadline for the task '{task}'")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task to be done as soon as possible.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a {priority} priority task. Consider setting a time for it next time in your agenda.")
        else:
            print(f"Set a deadline for the task '{task}'")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task to be done before the deadline.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a {priority} priority task. Set it in your next to-do list.")
        else:
            print(f"Set a deadline for the task '{task}'")