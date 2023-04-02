import openai
import datetime
import csv

# Use key to access API
openai.api_key = open("key.txt", "r").read().strip('\n')

# TODO: Set up appropriate context for bot
# TODO: Set up script to take in user input to let bot create project plan
# (What is the timeline? What subject do you want to master? What do you want to focus on?)
# TODO: Save contents of project plan into .doc and .CSV files
# CSV file should be importable into Google Calendar, .doc file for personal use

def generate_action_plan(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role" : "user",
                "content": prompt}]
    )

    return response.choices[0].message.content

def save_to_csv(action_plan, file_name):
    with open(file_name, "w", newline="") as csvfile:
        fieldnames = ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description", "Location", "Private"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for step in action_plan:
            writer.writerow(step)

def main():
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
