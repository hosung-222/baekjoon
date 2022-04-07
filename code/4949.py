#균형잡힌 세상
while True:
    s = input()
    if s == '.':
        break
    
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) !=0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break

        elif i == ')':
            if len(stack) !=0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        print('yes')         
    else:
        print('no')

