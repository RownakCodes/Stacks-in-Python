from stacks import Stack

def deciToBin(num):
    binaryStack = Stack()
    binNum = ""
    print(f"The binary of {num} is: ", end = "")
    while num >   0:
        binaryStack.push(num % 2)
        num = num // 2
        
    while not(binaryStack.isEmpty()):
        binNum += str(binaryStack.peek())
        binaryStack.pop()
    print(binNum)

num1 = 242
num2 = 177
num3 = 6

deciToBin(num1)
deciToBin(num2)
deciToBin(num3)