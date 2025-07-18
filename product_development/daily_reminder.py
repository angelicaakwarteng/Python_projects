# Personal Daily Reminder
task = input("Enter your task: ")
priority = str(input("Priority (high/medium/low): "))
time_bound = str(input("Is it time-bound? (yes/no): "))

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Task: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: This is a {priority} priority task.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: 'Don't forget the deadline'. This is a {priority} priority task that requires attention!")
        else:
            print(f"Reminder: This is a {priority} priority task.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: This is a {priority} priority task but it is time-bound.")
        else:
            print(f"'Read a book' is a low priority task. Consider completing it when you have free time.")