# 어떤 값에 대해서도 최댓값을 잘 구할 수 있도록 함수를 만들고 여러값에 대해서 테스트

def max3(a,b,c) :
    """a, b, c의 최대값을 구하여 반환"""
    maximum = a
    if b > maximum : maximum = b
    if c > maximum : maximum = c
    return maximum # 최대값을 반환

print(f'max3(3,2,1) = {max3(3,2,1)}')
print(f'max3(3,2,2) = {max3(3,2,2)}')
print(f'max3(3,1,2) = {max3(3,1,2)}')
print(f'max3(2,1,3) = {max3(2,1,3)}')
print(f'max3(3,2,3) = {max3(3,2,3)}')
print(f'max3(3,3,2) = {max3(3,3,2)}')
print(f'max3(3,3,3) = {max3(3,3,3)}')
print(f'max3(2,2,3) = {max3(2,2,3)}')
print(f'max3(2,3,1) = {max3(2,3,1)}')
print(f'max3(2,3,2) = {max3(2,3,2)}')
print(f'max3(1,3,2) = {max3(1,3,2)}')
print(f'max3(2,3,3) = {max3(2,3,3)}')
print(f'max3(1,2,3) = {max3(1,2,3)}')