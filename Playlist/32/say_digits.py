def say_digits(n):
    say = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    if n == 0:
        return

    digit = n % 10
    n = n//10

    say_digits(n)
    
    print(say[digit],end=" ")

    return


say_digits(1230)