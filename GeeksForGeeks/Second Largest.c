class Solution:
    def getSecondLargest(self, arr):
        # code here
        n=len(arr)
        large=arr[0]
        second_large=-1
        for  i in range(0,n):
            if arr[i]>large:
              large=arr[i]
            
        for i in range(0,n):
            if arr[i]>second_large and arr[i]!=large:
                second_large=arr[i]
        return second_large