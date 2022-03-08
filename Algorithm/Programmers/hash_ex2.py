
def solution(phone_book):
    phone_book.sort()
    result = 0

    for i, num in enumerate(phone_book):

        length = len(num)

        try :
            if num == phone_book[i+1][:length]:
                return False

        except : IndexError

    return True



print(solution(["123","456","789"]))
