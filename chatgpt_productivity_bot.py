import openai
import datetime
import csv

# Author: Eman Mozaffar (mozaffar)
# Document contains functions used in script to generate action plan for
# user, by using ChatGPT's API and chatbot functionalities.
# For more information, please refer to the README document located in
# this repository.

# Use key to access API - make sure you have key file saved
openai.api_key = open("key.txt", "r").read().strip('\n')

def generate_action_plan(prompt):
    """
    Generate an action plan using OpenAI API based on the given prompt.

    Parameters
    ----------
    prompt : str
        The prompt for generating the action plan.

    Returns
    -------
    str
        The generated action plan as a string.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role" : "user",
                "content": prompt}]
    )

    return response.choices[0].message.content

def save_to_csv(action_plan, file_name):
    """
    Save the action plan to a CSV file.

    Parameters
    ----------
    action_plan : list of dict
        The action plan as a list of dictionaries, each representing a step with the required fields.
    file_name : str
        The name of the CSV file to save the action plan.
    """
    with open(file_name, "w", newline="") as csvfile:
        fieldnames = ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description", "Location", "Private"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for step in action_plan:
            writer.writerow(step)
