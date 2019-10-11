#!/usr/bin/python3.6
import argparse


class Cat:
    def __init__(self, args = None):
        self.args = args if args else self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('file', metavar='FILE', nargs='+', type=str)
        parser.add_argument('-n', action='store_true', help='print line number')
        return parser.parse_args()

    def execute(self):
        i = 0
        for f in self.get_lines():
            for line in f.split('\n'):
                if self.args.n:
                    print(f'{i+1} {line}')
                    i += 1
                else:
                    print(line)

    def get_lines(self):
        for file in self.args.file:
            try:
                yield open(file).read()
            except FileNotFoundError:
                print(f'cat: {file}: No such file or directory')


if __name__ == '__main__':
    Cat().execute()

