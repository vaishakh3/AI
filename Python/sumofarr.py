def Sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

arr=eval(input("Enter the array: "))
print("Sum of the elements is: ",Sum(arr))
