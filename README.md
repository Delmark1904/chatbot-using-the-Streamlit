# Streamlit app for Intent classification

File `inference.py` contains a Python script for running a chatbot using the Streamlit framework. The chatbot interacts with the user, asks questions, and analyzes the sentiment of the user's responses.

## Initial requirements
* streamlit for creating the web application.
* transformers for performing sentiment analysis using pre-trained models.

## Usage
1. The script defines several functions:
* `libs_import`: Imports the necessary libraries and sets up sentiment analysis using the transformers pipeline.
* `analysis`: Performs sentiment analysis on a given sentence using the pre-trained model and returns the sentiment label.
* `get_text`: Displays a text input field in the Streamlit application for user input.
* `print_text`: Writes a response from the bot in the Streamlit application.
* `load_data`: Sets up the Streamlit application interface, including asking questions, analyzing responses, and displaying results.
2. The main function, load_data, is called when the script is run. It sets up the Streamlit application and handles the interaction with the user.
3. The Streamlit application prompts the user to enter a welcome message and the number of questions to ask. The user can customize the welcome message and enter their own questions.
4. After confirming the start of the dialog with the bot, the application displays the questions and waits for the user's responses.
5. The user's responses are analyzed using sentiment analysis. If the sentiment is positive, the bot continues to the next question. If the sentiment is negative, the bot stops the dialog and displays a farewell message.
6. If the user responds with "stop" at any point, the bot immediately stops the dialog and displays the final results, including the number of "yes" and "no" answers, the questions that received "no" answers, and whether the user wants a call later.
7. If the bot reaches the end of the questions without a "stop" response, it prompts the user to confirm whether they want a call later. Based on the response, the bot displays an appropriate message and ends the dialog.
8. At the end of the script, the load_data function is called to start the Streamlit application and initiate the bot interaction.

## Contributing
* All upgrades should be done on new branches (branches could be named as task index, eg [TASK-1]);
* Idealy - all changes should be documented somewhere (for me - it was done_day file);
* After refactoring, testing and approving - branch should be merged with main;
* If task is bug-fix - it should be named properly;
* Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please submit them as GitHub issues or create a pull request.

## Contact
* Creator - Nikita Oliinyk (Data Scientist);
* e-mail - noliinyk@freysoft.com.
