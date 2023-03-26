# chatgpt-tool
Final project for SI568

1. Use Case: Many students want to set goals and accomplish tasks to meet their career, academic, or personal objectives, but they might not be sure where to start. I want to create a tool that gives students personalized action plans that will help them reach goals that cater to their timelines, areas of focus, and other things they value. My tool will take in responses to a series of specific questions, which could be as follows:
    - What are you currently working on? What do you already know or feel confident about in regards to your learning and accomplishments?
    - What are the areas of focus that matter most to you? What are you struggling with academically or professionally?
    - What is your timeline?
    - What’s your ultimate goal?
    - Using parameters such as the responses generated from the questions above, I want to use ChatGPT to create an action plan. This plan can contain a calendar of sub-goals and when you want to accomplish each goal, tools you can use throughout, ways to measure your success, detailed steps, a holistic calendar overview of the course of your journey, and other details that are organized in one document you can pull down and have for your personal use.
2. How I would use ChatGPT: 
    - The API lets you input a series of requests, and gives you responses in the form of a dictionary that you can use to get the response to each prompt. Using this, we can put in several queries and save all the responses in some data structure in Python.
    - We can use all of these responses to build a visually appealing document, and give the user the option to preview and/or save the document. Hopefully, from there, they will have access to a guide that will help them reach their goals.
    - After previewing the document, we can ask the user if it’s sufficient, and if it isn’t we can ask additional questions about what we can do to make the document more useful for them.
3. Presentation
    - I want to either use a Flask app or a different interface application to display my results and my prompts. I might make it chatbot-style similar to the OpenAI website, but I need to play around with my options and actually get my results first before deciding on this.
    - We can give them the option to save different file formats, and maybe even a Google Calendar download that they can import into their personal calendar.
    - I also want to play around with what else I can do visually with the results.
