from argparse import ArgumentParser
import fileinput


def parse_args():
    parser = ArgumentParser()

    parser.add_argument("filename", nargs='*', help="Path to files, if not specified read from stdin")

    return parser.parse_args()


def parse_line_stat(line):
    bytes_count = len(line.encode('utf-8'))
    words_count = len(line.split())

    return words_count, bytes_count

def wc(args):
    statistic = []

    if not args.filename:
        lines_count = 0
        words_count = 0
        bytes_count = 0
        stdin_lines = []
        for line in fileinput.input():
            stdin_lines.append(line)
            lines_count += 1
            stat = parse_line_stat(line)
            words_count += stat[0]
            bytes_count += stat[1]
        print(f"      {lines_count}      {words_count}     {bytes_count}")
    else:
        for filename in args.filename:
            lines_count = 0
            words_count = 0
            bytes_count = 0
            with open(filename) as file:
                lines = file.readlines()
            for line in lines:
                lines_count += 1
                stat = parse_line_stat(line)
                words_count += stat[0]
                bytes_count += stat[1]
            print(f"      {lines_count}      {words_count}     {bytes_count} {filename}")
            statistic.append((lines_count, words_count, bytes_count))
        if len(args.filename) > 1:
            print(f"      {sum(stat[0] for stat in statistic)}      {sum(stat[1] for stat in statistic)}    {sum(stat[2] for stat in statistic)} total")



def main():
    args = parse_args()
    wc(args)


if __name__ == "__main__":
    main()