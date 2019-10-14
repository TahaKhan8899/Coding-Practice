class Solution():
    def fibonacci_recursive(self, n):
        # fill this in.
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return (self.fibonacci_recursive(n-1) + self.fibonacci_recursive(n-2))

    def fibonacci_iterative(self, n):

        num1 = 0
        num2 = 1

        if n == 0:
            return 0
        elif n == 1:
            return 1

        fibNum = 0
        for i in range(0, n-1):
            fibNum = num1 + num2
            num1 = num2
            num2 = fibNum

        return fibNum


for i in range(0, 100):
    n = i
    print(Solution().fibonacci_iterative(n))

n = 6
print(Solution().fibonacci_recursive(n))
