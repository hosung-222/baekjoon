n = int(input())

count = 0       #스택에 쌓을 변수
stack = []      #스택 역활 
result = []     #출력할 내용 저장
message = True  #연산 불가능 판단


for i in range(n):
    x = int(input())
    
    while count < x:    #만약 입력수보다 스택에 쌓인 변수가 작으면
        count += 1      
        stack.append(count)     #스택에 오름차순으로 쌓음
        result.append("+")      #쌓을때마다 +
    
    if stack[-1] == x:  #스택의 끝값이 입력변수와 같으면
        stack.pop()     #제거후 -출력
        result.append("-")
    else:
        message = False #다르면 연산불가능판단
        
        
if message == False:
    print("NO")

else:
    print("\n".join(result))
        
