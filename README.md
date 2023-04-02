# chatgpt-tool
Final project for SI568

1. Use Case: Many students want to set goals and accomplish tasks to meet their career, academic, or personal objectives, but they might not be sure where to start. I want to create a tool that gives students personalized action plans that will help them reach goals that cater to their timelines, areas of focus, and other things they value. My tool will take in responses to a few questions, which will give ChatGPT context to understand the following:
    - What are you currently working on? What do you already know or feel confident about in regards to your learning and accomplishments?
    - What are the areas of focus that matter most to you? What are you struggling with academically or professionally?
    - What is your timeline?
    - What’s your ultimate goal?
    - Using parameters such as the responses generated from the questions above, I want to use ChatGPT to create an action plan. This plan can contain a calendar of tasks and when you want to accomplish each goal, tools you can use throughout, ways to measure your success, detailed steps, a holistic calendar overview of the course of your journey, and other details that are organized in a document you can pull down and have for your personal use.
2. How I would use ChatGPT:
    - The API lets you input a series of requests, and gives you responses in the form of a dictionary that you can use to get the response to each prompt. Using this, we can put in several queries and save all the responses in some data structure in Python.
    - We can use all of these responses to build a useful document, and give the user the option to save the document. Hopefully, from there, they will have access to a guide that will help them reach their goals.
3. Presentation
    - I want to use the command line as a simple interface for the user.
    - I want to give the user the option to save the details in a CSV format they can upload to Google Calendar directly.
