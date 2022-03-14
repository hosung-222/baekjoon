while True:
    n = input()

    if int(n) == 0:
        break

    if n == n[::-1]:  #문자열을 뒤집은것과 비교
        print('yes')
    else:
        print("no")
        
    

