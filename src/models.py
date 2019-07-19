
import math


class Fib:

    def __init__(self, num):
        self.num = int(num)
        if self.num < 0:
            self.num = 1

    def calculate(self):
        """Return fibonacci numeral in the @num position
        Use closed formula

        """
        SQRT5 = math.sqrt(5)
        PHI = (SQRT5 + 1) / 2

        return int(PHI ** self.num / SQRT5 + 0.5)


class Fact:

    def __init__(self, num):
        self.num = int(num)

    def calculate(self):
        """Return factorial of the @num

        """
        result = 1

        for i in range(1, self.num + 1, 1):
            result *= i

        return result
