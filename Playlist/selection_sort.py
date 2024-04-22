
if __name__ == "__main__":
    # arr = [6,2,8,4,10]
    arr = [5,4,3,2,1]
    n = 5
    print(arr,end="\n\n")

    for i in range(0,n-1):
        min_index = i

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j

        print(i,min_index,end="\t\t")
        # temp = arr[i]
        # arr[i] = arr[min]
        # arr[min] = temp

        arr[i],arr[min_index] = arr[min_index],arr[i]

        print(arr)