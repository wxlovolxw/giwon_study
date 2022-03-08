def is_leap(year):

    if year % 400 != 0:

        if year % 100 != 0 :

            if year % 4 != 0 :
                result = False
            else : result = True

        else : result = False

    else : result = True

    return result
