from chatgpt_productivity_bot import *

# Author: Eman Mozaffar (mozaffar)
# Main file including script for user inputs and CSV file as outputs.
# Uses functions defined in chatgpt_productivity_bot.py.
# For more information, please refer to the README document located in
# this repository.

def main():
    """
    Main function to execute the script. Takes in user input
    and returns prompts based on previous inputs. Allows the user
    to ask for an action plan based on their goals and timelines, and
    gives them the option to save the file in a CSV format in order to
    import the tasks as Google Calendar events.

    Parameters
    ----------
    User input in terminal.

    Returns
    -------
    None
    """
    goal = input("Enter your goal: ")
    timeline_str = input("Enter the timeline to complete your goal (in days): ")
    details = input("Enter some details about what you want to accomplish: ")

    try:
        timeline = int(timeline_str)
    except ValueError:
        print("Invalid input. Please enter a number for the timeline.")
        return

    start_date = datetime.datetime.now()
    prompt = (
        f"Generate a detailed action plan with steps and due dates in a list format for achieving the "
        f"following goal in {timeline} days: '{goal}'. Details: {details}. Start date: {start_date:%Y-%m-%d}. "
        f"Please provide the action plan as a list of dictionaries, where each dictionary represents a step "
        f"and contains keys and values for the following fields: 'Subject', 'Start Date', 'Start Time', 'End Date', "
        f"'End Time', 'All Day Event', 'Description', 'Location', 'Private'. This will be used to create Google "
        f"Calendar events after the list of dictionaries is written to a CSV file so it can be imported by the user."
    )

    action_plan_text = generate_action_plan(prompt)
    action_plan = eval(action_plan_text)
    print("\nAction Plan:")
    for step in action_plan:
        print(f"{step['Subject']} ({step['Start Date']} - {step['End Date']})")

    save_option = input("\nDo you want to save the action plan as a CSV file for Google Calendar? (yes/no): ").lower()
    if save_option == "yes":
        file_name = input("Enter the file name (without extension): ")
        save_to_csv(action_plan, file_name + ".csv")
        print(f"Action plan saved to {file_name}.csv. You can import this file into your Google Calendar directly. Good luck!")

if __name__ == "__main__":
    main()