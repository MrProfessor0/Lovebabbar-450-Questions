def wavePrint(arr, nRows, mCols):
    ans = []
    # Write your code here.
    # Return a list of integers denoting the sine wave of the matrix
    for i in range(0,mCols):
        # print(ans)
        if i % 2 == 0:
            for j in range(nRows):
                ans.append(arr[j][i])
        else:
            for j in range(nRows):
                ans.append(arr[nRows-1-j][i])

    return ans

arr = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
nRows = 3
mCols = 4
print(arr)
print(wavePrint(arr,nRows,mCols))



    