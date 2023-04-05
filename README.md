# chatgpt-tool

## Final project for SI568

1. Use Case: Many students want to set goals and accomplish tasks to meet their career, academic, or personal objectives, but they might not be sure where to start. I have created a tool that gives students personalized action plans that will help them reach goals that cater to their timelines, areas of focus, and other things they value. My tool takes in responses to a few questions, which will give ChatGPT context to understand the following:
    - What are you currently working on? What do you already know or feel confident about in regards to your learning and accomplishments?
    - What is your timeline?
    - Using parameters such as the responses generated from the questions above, ChatGPT will create an action plan. This plan can contain a calendar of tasks and when you want to accomplish each goal, tools you can use throughout, ways to measure your success, detailed steps, a holistic calendar overview of the course of your journey, and other details that are organized in a document you can pull down and have for your personal use.
2. How I use ChatGPT:
    - The OpenAI API gives us responses we can use to build our action plans. Using the API, we can ask ChatGPT a detailed query and use the results of the response to build results and a file for the user.
    - Our document will include specific details about the proposed plan, and we will give the user the option to save the document. Hopefully, from there, they will have access to a guide that will help them reach their goals.
3. Presentation
    - I will use the command line prompt as a simple interface for the user.
    - I will give the user the option to save the details in a CSV format they can upload to Google Calendar directly. After importing the file, the user will have customized events and reminders that will help them stay on track to meet their goals.

## User Guide: Getting Started

- **Welcome!** This tool is designed to help you formulate a plan based on what you want to accomplish. Start off by ensuring all program files are downloaded, and run main.py to launch the prompt in the command line.
- When you download the file, you will want to have a key.txt file that includes your API key. This will be used to access the API.
- The main file  will ask you for a few inputs. It will ask you what your goal is, along with how many days you want to work on it, and any additional information you can provide. When it asks for additional information, be as specific as you like! If you have preferences for how often you want a particular type of task will occur (for example, you are training for a 5k, and you prefer to run 3 times a week and in the mornings, or you want to incorporate strength training), please specify that if you wish.
- After providing your input, the tool will give you a preview of the tasks it generated, and will ask you if you want to save the detailed output to a csv file for your viewing and use.
- If you choose to save the CSV file, note that you can certainly use the file for personal use in any way you see fit, but the file is also specifically designed to be imported into Google Calendar. If you do so, the events will be populated in your calendar, and you will be able to adjust them in any way you would like.
- If, at any point, you enter in input that isn't understood by the tool, you will be prompted to enter your information again. You can run the script as often as you want, and for any type of goal imaginable. **Good luck!**
