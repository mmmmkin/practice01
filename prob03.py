# 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.
import sys
"""s =
*
**
***
****
*****
******
*******
********
*********
**********
"""


# print(s)

star = 0
i = 0
for star in range(10):
    for i in range(star + 1):
        print('*', end='')
    print()

# 별해
for star in range(1, 10):
    print('*' * star)
