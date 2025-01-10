print("Hello Broz")


def sum(a, b):
    print(a+b)


sum(5, 6)


def sub(a, b):
    print(a-b)

sub(5, 3)

arr = [1, 2, 4, 3, 5]

def sumOfArr(arr):
    sum=0

    for item in arr:
        sum+=item
    
    return sum

print(sumOfArr(arr))