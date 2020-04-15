class FibSolution:
    def byRecursion(self, n):
        if n == 1:
            return 0
        elif n==2:
            return 1
        else:
            return self.byRecursion(n-2) + self.byRecursion(n-1)

    def byDP(self, n, dictionary):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            if n in dictionary:
                return dictionary[n]
            else:
                dictionary.update({n:self.byDP(n-2, dictionary) + self.byDP(n-1, dictionary)})
                return dictionary[n]

    def byIteration(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            a, b = 0, 1
            for i in range(n-2):
                tmp = a + b
                a = b
                b = tmp
            return b

if __name__ == '__main__':
    solver = FibSolution()
    print(solver.byRecursion(10))
    print(solver.byDP(10, {}))
    print(solver.byIteration(10))

