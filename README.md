# Code Challenges

This Python script guides the user through a CLI coding interview. It gives the user 1 easy, 1 medium, and 1 hard question (courtesy of Leetcode) randomly pulled from a Firebase Realtime Database with the questions and testcases. 

## Requirements
Install the pip packages in requirements.txt. To freeze the python script, install PyInstaller and run pyinstaller main.py in the terminal

## Usage
Either install all the pip packages and run main.py, or just run dist/main.exe (the executable produced by PyInstaller which doesn't require Python, only compatible with Windows 10). 

## Potential Improvements
1. Using authentication rather than just trusting that the user won't tamper with the user scores data (although I did make the problems read-only)
2. More problems and test cases
3. Using Firebase functions to evaluate the user's answers outside of client-side so that it's harder to reverse-engineer the right answers