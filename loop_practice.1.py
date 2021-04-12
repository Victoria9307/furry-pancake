# Q.1 for 문을 이용하여 1부터 입력받은 정수까지의 합을 구하여 출력하는 프로그램을 작성하시오.¶
# 100 이하의 양의 정수만 입력된다.
# 입력 예: 10
# 출력 예: 55

number = int(input("Number Please : "))
sum = 0
for x in range (1, number+1) :
    sum += x
if number <= 100 :
    print(sum)
    

    
 



    
# Q.3 정수를 입력받아서 3의 배수가 아닌 경우에는 아무 작업도 하지 않고, 
# 3의 배수인 경우에는 3으로 나눈몫을 출력하는 작업을 반복하다가 -1이 입력되면 종료하는 프로그램을 작성하시오.¶
# 예시:
# 5
# 12
# 4
# 21
# 7
# 100
# -1

a = (int(input("Number please : ")))
msum = 0
while a == -1 :
    break
if (a % 3) == 0 :
    msum = (a//3)
    print(msum)

    
    
    
# Q.3 (plus)
# 아래와 같은 모양으로 출력하는 프로그램을 작성하시오.
# 사용자에게 숫자를 입력받아 입력 받은 높이 만큼의 삼각형을 출력하시오.
# 입력 예: 5
#     *
#    **
#   ***
#  ****
# *****

a = int(input("Number Please"))
for x in range (1,a+1) :
    for y in range(1,(a+1-x)) :
        print(" ",end="")
    for b in range(0,x) :
        print("*", end="")
    print()

    
    
    

    
 
# Q.9(bonus)
# 아래와 같은 모양으로 출력하는 프로그램을 작성하시오.
# 사용자에게 숫자를 입력받아 입력 받은 높이 만큼의 삼각형을 출력하시오.
# 입력 예: 5
# *****
#  ****
#   ***
#    **
#     *

