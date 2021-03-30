from threading import Thread, Event

import shutil
import subprocess
from firebase import Firebase
from colorama import init, Fore, Style
import random

move_on = False


def main():
    # Initialize colorama
    init()

    # Get firebase ref
    firebase = setup_firebase()
    print("─" * shutil.get_terminal_size().columns)
    print("Welcome to the coding interview!")
    print("You will be answering into 1 easy, 1 medium, and 1 hard random questions.")
    print("You may exit anytime by typing \"exit\".")

    print(Fore.GREEN + "Easy:" + Fore.RESET + " 5 min")
    print(Fore.YELLOW + "Medium:" + Fore.RESET + " 10 min")
    print(Fore.RED + "Hard:" + Fore.RESET + " 20 min")

    print("─" * shutil.get_terminal_size().columns)

    # Get user info
    print("Please enter your email address below:")
    email_address = input().replace(".", " dot ")
    if email_address == "exit":
        exit_seq()

    print("Please enter your name below:")
    name = input()
    if name == "exit":
        exit_seq()

    print("Thank you! Once you enter \"yes\", the interview will automatically start. Please make sure you\'re ready!")
    while True:
        user_input = input()
        if user_input == "exit":
            exit_seq()
        elif user_input == "yes":
            break

    # Begin the interview
    global move_on  # Set to True if the timer hits 0
    points = 0
    challenge_difficulties = {"easy": 5, "medium": 10, "hard": 20}
    for difficulty, time_limit in challenge_difficulties.items():
        print("─" * shutil.get_terminal_size().columns)

        if difficulty == "easy":
            color = Fore.GREEN
        elif difficulty == "medium":
            color = Fore.YELLOW
        else:
            color = Fore.RED
        print(f"Here is your {color + difficulty + Fore.RESET} challenge. "
              f"You have {time_limit} min to answer the test cases correctly.")

        # Get the random challenge with the stated difficulty from Firebase
        challenge = get_random_challenge(difficulty, firebase)
        print(Style.BRIGHT + challenge["name"] + Style.RESET_ALL)
        print(challenge["description"])

        # Start the timer
        stop_flag = Event()
        timer = Timer(stop_flag, time_limit)
        timer.start()

        print("─" * shutil.get_terminal_size().columns)
        user_ans_name = input("Please enter the name of your answer file here: ")
        user_ans_dir = input("Please enter the directory of your answer file here: ")
        move_on = False
        while not move_on:
            print("Type anything to grade")
            input_continue = input()
            if input_continue == "exit":
                exit_seq()
            if move_on:
                break

            # Check if the test cases the user enters match
            test_cases_passed = 0
            for i, test_case in enumerate(challenge["test-cases"]):
                print("─" * shutil.get_terminal_size().columns)
                print(f"Test case {i + 1}:")

                input_vals = []
                for input_name, input_val in test_case["input"].items():
                    print(f"{input_name }: {input_val}")
                    input_vals.append(str(input_val))

                try:
                    user_answer = subprocess.run(['python', user_ans_name] + input_vals, capture_output=True, text=True, cwd=user_ans_dir).stdout.strip("\n")
                except Exception as e:
                    print(Fore.RED + "Error: " + str(e) + Fore.RESET)
                    user_ans_name = input("Please enter the name of your answer file here: ")
                    user_ans_dir = input("Please enter the directory of your answer file here: ")
                    break

                answer = list(test_case["output"].values())[0]
                print(f"User answer: {user_answer}")
                print(f"Correct answer: {answer}")
                try:
                    if ((type(answer) is float or type(answer) is int) and float(user_answer) == float(answer)) or \
                            str(user_answer) == str(answer):

                        print(Fore.GREEN + "Passed!" + Fore.RESET)
                        test_cases_passed += 1
                    elif str(user_answer) == "exit":
                        exit_seq()
                    else:
                        print(Fore.RED + "Incorrect" + Fore.RESET)
                        break
                except:
                    print(Fore.RED + "Invalid input" + Fore.RESET)
                    break

            # User correctly answered all the test cases
            if test_cases_passed == len(challenge["test-cases"]):
                points += time_limit
                print(Fore.GREEN + "Solved the question!" + Fore.RESET)

                # Stop the timer
                stop_flag.set()

                # Move onto the next question
                move_on = True

                if difficulty != "hard":
                    print("Type \"yes\" when you're ready for the next question")

                    while True:
                        user_input = input()

                        if user_input == "exit":
                            exit_seq()
                        elif user_input == "yes":
                            break
            else:
                pass

    # Update the user's score to firebase
    print(f"Thank you for taking the coding challenge! You got {points} points out of 35")
    firebase.database().child(f"users/{email_address}/name").set(name)
    firebase.database().child(f"users/{email_address}/score").set(points)
    exit_seq()


def get_random_challenge(difficulty, firebase):
    easy_challenge = random.choice(firebase.database().child("challenges/" + difficulty).get().val()[1:])

    # Parse test cases
    test_cases_unparsed = easy_challenge["test-cases"]
    test_cases_parsed = []
    for test_case in test_cases_unparsed[1:]:
        test_cases_parsed.append({"input": parse_firebase_testcases(test_case["inputs"]),
                                  "output": parse_firebase_testcases(test_case["outputs"])})
    easy_challenge["test-cases"] = test_cases_parsed
    return easy_challenge


def parse_firebase_testcases(test_cases):
    input_dict = {}
    for input_name, input_val in test_cases.items():
        input_split = input_val.split(" ")
        if input_split[0] == "arr":
            input_dict[input_name] = [int(x) for x in input_split[1:]]
        elif input_split[0] == "str":
            input_dict[input_name] = str(input_split[1])
        elif input_split[0] == "int":
            input_dict[input_name] = int(input_split[1])
        elif input_split[0] == "float":
            input_dict[input_name] = float(input_split[1])
    return input_dict


def setup_firebase():
    config = {
        "apiKey": "AIzaSyCAxiYl8U5SQTeZ9JyXx3iBP8Gye7g8ge0",
        "authDomain": "code-challenge-4edda.firebaseapp.com",
        "databaseURL": "https://code-challenge-4edda-default-rtdb.firebaseio.com",
        "projectId": "code-challenge-4edda",
        "storageBucket": "code-challenge-4edda.appspot.com",
        "messagingSenderId": "719044340737",
        "appId": "1:719044340737:web:52bb81a8c29b38b747e400"
    }

    firebase = Firebase(config)
    return firebase


# https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
class Timer(Thread):
    def __init__(self, event, time_remaining):
        Thread.__init__(self)
        self.stopped = event
        self.time_remaining = time_remaining

    def run(self):
        while not self.stopped.wait(60):
            print(f"{Fore.LIGHTMAGENTA_EX + str(self.time_remaining) + Fore.RESET} min remaining")
            self.time_remaining -= 1

            if self.time_remaining == 0:
                print("No time left! Please type anything to move onto the next question")
                global move_on
                move_on = True
                return


def exit_seq():
    _ = input("You may exit the program")


if __name__ == "__main__":
    main()
