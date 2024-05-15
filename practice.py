def HELLO(a):
    print("INSIDE HELLO")
    print(a)
    a += 1
    print(a)
    print("end")
if __name__ == "__main__":
    a = 0
    print(a)
    HELLO(a)
    print(a)