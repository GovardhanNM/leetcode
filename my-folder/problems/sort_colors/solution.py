class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        start = 0
        mid = 0
        end = n - 1

        while mid <= end:
            if arr[mid] == 0:
                temp = arr[mid]
                arr[mid] = arr[start]
                arr[start] = temp
                start += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                temp = arr[mid]
                arr[mid] = arr[end]
                arr[end] = temp
                end -= 1
            # print(start, mid, end)
        