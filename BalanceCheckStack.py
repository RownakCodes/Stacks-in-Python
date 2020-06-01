from stacks import Stack

def balanceCheck(strng):
    brackets = Stack()
    index = 0
    isBalanced = True
    while index < len(strng) and isBalanced:
        content = strng[index]
        ending = content in ")}]"
        if not(brackets.isEmpty()):
            if ending:
                brackets.pop()
            else:
                brackets.push(content)
        elif ending and brackets.isEmpty():
            isBalanced = False
        else:
            brackets.push(content)
        index += 1
    if isBalanced:
        print("It is balanced!")
    else:
        print("It is unbalanced!")


str1 = "(({{}}))"
str2 = "[[{{}}]]]]]]]"
str3 = "[[{{(())}}]]"

balanceCheck(str1)
balanceCheck(str2)
balanceCheck(str3)