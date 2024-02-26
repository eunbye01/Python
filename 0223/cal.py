def 더하기(x, y):
    return x + y

def 빼기(x, y):
    return x - y

def 곱하기(x, y):
    return x * y

def 나누기(x, y):
    if y == 0:
        return "0으로 나눌 수 없습니다."
    else:
        return x / y

while True:
    print("\n")
    print("사용 가능한 연산: +, -, *, /")
    연산자 = input("사용할 연산을 입력하세요 (종료하려면 '종료' 입력): ")

    if 연산자 == '종료':
        print("프로그램을 종료합니다.")
        break

    if 연산자 not in ['+', '-', '*', '/']:
        print("올바르지 않은 연산자입니다.")
    else:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        if 연산자 == '+':
            print("결과:", 더하기(num1, num2))
        elif 연산자 == '-':
            print("결과:", 빼기(num1, num2))
        elif 연산자 == '*':
            print("결과:", 곱하기(num1, num2))
        elif 연산자 == '/':
            print("결과:", 나누기(num1, num2))
