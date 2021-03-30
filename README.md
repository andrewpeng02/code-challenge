# Code Challenges
This Python script guides the user through a CLI coding interview. It gives the user 1 easy, 1 medium, and 1 hard question (courtesy of Leetcode) randomly pulled from a Firebase Realtime Database with the questions and testcases. After the interview, the user gets a score out of 35 and uploads his/her score, name, and email to the database

![](https://github.com/andrewpeng02/code-challenge/blob/main/README%20images/Screenshot%20app%201.png)

The script directs the user to input his/her information
![](https://github.com/andrewpeng02/code-challenge/blob/main/README%20images/Screenshot%20app%202.png)

An example of the script handling correct/incorrect test cases
## Requirements
Install the pip packages in requirements.txt. To freeze the python script, install PyInstaller and run pyinstaller main.py in the terminal

## Usage
Clone the repo and either install all the pip packages and run main.py, or just run dist/main.exe (the executable produced by PyInstaller which doesn't require Python, only compatible with Windows 10)

## Potential Improvements
1. Using authentication rather than just trusting that the user won't tamper with the user scores data (although I did make the problems read-only)
2. More problems and test cases
3. Using Firebase functions to evaluate the user's answers outside of client-side so that it's harder to reverse-engineer the right answers

![The Firebase database containing the problems and the scores of users](https://github.com/andrewpeng02/code-challenge/blob/main/README%20images/Firebase.png)

The Firebase database containing the problems and the scores of users
