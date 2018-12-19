# victorcc
# bitwise
# assci code
# 10878 - Decode the tape

import sys


class ProblemSolver10878:
    def line_to_number(self, line):
        number = 0
        i = len(line) - 5
        for character in line:
            if character == 'o':
                number += (2 ** i)
            if character in ['o' ,' '] :
                i -= 1
        return number

    def solve(self):
        message = ''
        for line in sys.stdin:
            if line[0] != '_':
                number = self.line_to_number(line)
                message += chr(number)
        print(message, end = '')

if __name__ == "__main__":
    problem_solver = ProblemSolver10878()
    problem_solver.solve()
