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
