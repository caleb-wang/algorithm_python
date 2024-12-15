from ListNode import ListNode


# 递归
class Solution:
    def __init__(self):
        self.mem = []
        self.cache = {}

    # region 斐波那契数列
    def fibonacci(self, n: int) -> int:
        self.mem = [0] * (n + 1)
        return self.fibonacci_r(n)

    def fibonacci_r(self, n) -> int:
        if n == 1 or n == 2: return 1

        if self.mem[n] != 0: return self.mem[n]

        self.mem[n] = (self.fibonacci_r(n - 1) + self.fibonacci_r(n - 2)) % 1000000007
        return self.mem[n]

    # endregion

    # region 递归求N阶乘
    def factorial(self, n: int) -> int:
        return self.factorial_r(n)

    def factorial_r(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        if self.cache.get(n) is not None: return self.cache.get(n)

        self.cache[n] = (self.factorial_r(n - 1) * n) % 7777777
        return self.cache[n]

    # endregion

    # region 爬楼梯（I）
    def climbStairs(self, n: int) -> int:
        return self.climbStairs_r(n=n)

    def climbStairs_r(self, n: int) -> int:
        if n == 1 or n == 2: return n
        if self.cache.get(n) is not None: return self.cache.get(n)

        self.cache[n] = self.climbStairs_r(n - 1) + self.climbStairs_r(n - 2)
        return self.cache[n]

    # endregion

    # region 爬楼梯（II）
    def climbStairsTwo(self, n: int) -> int:
        return self.climbStairsTwo_r(n=n)

    def climbStairsTwo_r(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 4

        if self.cache.get(n) is not None: return self.cache.get(n)
        self.cache[n] = (self.climbStairsTwo_r(n - 1) + self.climbStairsTwo_r(n - 2) + self.climbStairsTwo_r(
            n - 3)) % 1000000007
        return self.cache[n]

    # endregion

    # region  猴子吃桃
    def eatPeaches(self, nDays: int) -> int:
        return self.eatPeaches_r(nDays=nDays)

    def eatPeaches_r(self, nDays: int) -> int:
        if nDays == 1: return 1
        m = (self.eatPeaches_r(nDays - 1) + 1) * 2
        return m

    # endregion

    # region 倒序遍历链表
    def reversePrint(self, head: ListNode):
        return self.reversePrint_r(head=head)

    def reversePrint_r(self, head: ListNode):
        if head is None: return
        self.reversePrint_r(head=head.next)
        head.print()

    # endregion


if __name__ == '__main__':
    fb = Solution()

    three = ListNode(3)
    fb.reversePrint([3, 1, 4])
    # print(re)
