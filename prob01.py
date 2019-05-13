# 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
import sys


"""if number.isdigit():
    if number % 3 == 0:
        print('3의 배수 입니다.')"""
"""number = int(input('정수를 입력하세요:'))
if number % 3 == 0:
    print('3의 배수 입니다.')
    sys.exit(0)
elif number % 3 != 0:
    print('3의 배수가 아닙니다.')
    sys.exit(0)
else:
    print('정수가 아닙니다.')
    sys.exit(0)"""
number1 = input('정수를 입력하세요: ')

if number1.isalpha():
    print('정수가 아닙니다, 정수를 입력하세요.')
    sys.exit(0)
if number1.isdigit():
    if int(number1) % 3 == 0:
        print('3의 배수 입니다.')
        sys.exit(0)
    else:
        print('3의 배수가 아닙니다.')
        sys.exit(0)
