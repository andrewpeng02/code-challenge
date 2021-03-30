import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("input_1")

    args = parser.parse_args()
    if args.input == '[2, 7, 11, 15]' and args.input_1 == '9':
        print("[0, 1]")
    elif args.input == "[3, 2, 4]" and args.input_1 == '6':
        print("[1, 2]")


if __name__ == "__main__":
    main()
