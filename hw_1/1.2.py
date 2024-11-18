from argparse import ArgumentParser
import fileinput


def parse_args():
    parser = ArgumentParser()

    parser.add_argument("filename", nargs='*', help="Path to files, if not specified read from stdin")

    return parser.parse_args()


def tail(args):
    for filename in args.filename:
        if len(args.filename) > 1:
            print(f"==> {filename} <==")
        with open(filename) as file:
            lines = file.readlines()
        for line_index in range(max(len(lines) - 10, 0), len(lines)):
            print(f"{str(lines[line_index])}", end="")
        print()

    if not args.filename:
        stdin_lines = []
        for line in fileinput.input():
            stdin_lines.append(line)
        for line_index in range(max(len(stdin_lines) - 17, 0), len(stdin_lines)):
            print(f"{str(stdin_lines[line_index])}", end="")


def main():
    args = parse_args()
    tail(args)


if __name__ == "__main__":
    main()