from typing import List


class Solution:
    # region 冒泡排序
    def bubbleSort(self, arr: List[int], n: int) -> None:
        self.bubbleSort_r(arr, n)

    def bubbleSort_r(self, arr: List[int], n: int) -> None:
        if n <= 1: return

        for i in range(n - 1):
            flag = False
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    tem = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = tem
                    flag = True
            if not flag:
                break

    # endregion

    def insertSort(self, arr: List[int], n: int) -> None:
        self.insertSort_s(arr=arr, n=n)

    def insertSort_s(self, arr: List[int], n: int) -> None:
        if len(arr) < 2: return

        for i in range(n - 1):
            for j in range(n - 1 - i):

                if arr[j] > arr[n - 1 - i]:
                    tem = arr[j]


if __name__ == '__main__':
    fb = Solution()
    arr = [3, 2, 5, 1, 6]
    fb.bubbleSort(arr, 5)
    print(arr)
