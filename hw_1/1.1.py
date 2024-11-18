from argparse import ArgumentParser
import fileinput


def parse_args():
    parser = ArgumentParser()

    parser.add_argument("filename", nargs='?', help="Path to file, if not specified read from stdin", default="")

    return parser.parse_args()


def numerate_rows(args):
    row_count = 1
    if not args.filename:
        for line in fileinput.input():
            print(f"     {row_count}  {line}", end="")
            row_count += 1
    else:
        with open(args.filename) as file:
            lines = file.readlines()
        for line in lines:
            print(f"     {row_count}  {line}", end="")
            row_count += 1


def main():
    args = parse_args()
    numerate_rows(args)


if __name__ == "__main__":
    main()