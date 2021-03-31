# Code Challenges
This Python script guides the user through a CLI coding interview. After the admin sends an invitation to a user, the user inputs his/her unique code.

![](https://github.com/andrewpeng02/code-challenge/blob/main/README%20images/admin.png)

 It gives the user 1 easy, 1 medium, and 1 hard question (courtesy of Leetcode) randomly pulled from a Firebase Realtime Database with the questions and testcases. After the interview, the user gets a score out of 35 and uploads his/her score to the database. The expected input file must support taking the proper arguments and printing its answer to stdout. An example is provided in example.py, and the program supports Python, Javascript, or C++ files.

![](https://github.com/andrewpeng02/code-challenge/blob/main/README%20images/Screenshot2.png)

![](https://github.com/andrewpeng02/code-challenge/blob/main/README%20images/Screenshot.png)

An example of the script handling correct/incorrect test cases
## Requirements
Install the pip packages in requirements.txt

## Usage
Run ```pip install code-challenge``` and enter ```code-challenge``` in the terminal to begin the CLI program

## Potential Improvements
1. Using authentication rather than just trusting that the user won't tamper with the user scores data (although I did make the problems read-only)
2. More problems and test cases
3. Using Firebase functions to evaluate the user's answers outside of client-side so that it's harder to reverse-engineer the right answers
4. Inputs and outputs are passed as strings, it would be better to pass them in their native types (like int)

![The Firebase database containing the problems and the scores of users](https://github.com/andrewpeng02/code-challenge/blob/main/README%20images/Firebase.png)

The Firebase database containing the problems and the scores of users
