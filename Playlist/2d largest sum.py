def largest_row_sum(arr):
    max = -1
    index = 0
    count = 0
  
    for row in arr:
        sum = 0
        for i in row:
            sum += i

        if sum > max:
            max = sum
            index = count

        count += 1

    return index,sum




arr = [[3,4,11],[2,12,1],[7,8,7]]

print(largest_row_sum(arr))