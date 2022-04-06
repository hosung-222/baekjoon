#균형잡힌 세상
while True:
    s = input()
    if s == '.':
        break
    
    stack = []
    t = True
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) !=0 and stack[-1] == '[':
                stack.pop()
            else:
                t = False
        elif i == ')':
            if len(stack) !=0 and stack[-1] == '(':
                stack.pop()
            else:
                t = False  

    if t == True:
        print('yes')         
    else:
        print('no')
