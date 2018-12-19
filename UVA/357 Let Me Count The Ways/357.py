# victorcc
# memorization
# dp
# dinamic programing
# 357

import sys

sys.setrecursionlimit(30002)

memo = [[-1 for x in range(5)] for y in range(30001)]

coins = [1, 5, 10, 25, 50]


class ProblemSolver357:
    def solve(self):
        for line in sys.stdin:
            n = int(line)
            ans = self.count(n, 0)
            sans = "There is only 1 way"
            if ans != 1:
                sans = "There are %d ways" % ans
            sans += " to produce %d cents change." % n

            print(sans)

    def count(self, n, ind):
        if ind > 4:
            return 0
        if 0 > n:
            return 0

        ans = 1
        if n != 0:
            if memo[n][ind] == -1:
                # if there wasn't calculated before we can calculate
                # and store it in the bidimensional array memo
                memo[n][ind] = self.count(n - coins[ind], ind) + self.count(n, ind + 1)
            ans = memo[n][ind]
        return ans

if __name__ == "__main__":
    problem_sol = ProblemSolver357()
    problem_sol.solve()
