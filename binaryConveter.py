
print("\n\n Decimal to Binary converter \n")
num=int(input("Enter the number to convert: "))
def binary(num):
    if num>1:
        binary(num//2)    
    print(num%2, end='') 
print(f"The binary of {num} is: ")
binary(num)



