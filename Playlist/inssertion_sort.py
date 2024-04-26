from typing import List

def insertionSort(n: int, arr: List[int]) -> None:
    print(arr)
    print(n)
    # Write your code here.
    for i in range(1,n):
        for j in range(0,i):
            if arr[j] > arr[i]:
                temp = arr[i]
                counter = i
                while(counter>j):
                    arr[counter] = arr[counter-1]
                    counter -= 1
                arr[j] = temp
            print(j,end=" ")
            print(arr)
        print()




# arr = [10, 1, 7, 4, 8, 2, 11]
arr = [1,2,3,4,5,6,7]

insertionSort(len(arr),arr)