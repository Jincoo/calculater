def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

while True:
    print("\n계산기 프로그램")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 종료")
    
    choice = input("원하는 연산을 선택하세요 (1/2/3/4/5): ")
    
    if choice == '3':
        print("계산기를 종료합니다.")
        break
    
    if choice in ('1', '2'):
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {subtract(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {subtract(num1, num2)}")
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")