def leading_hand(h, m):
    """
    >>> leading_hand(22, 51)
    'minute hand'
    >>> leading_hand(21, 45)
    'draw'
    >>> leading_hand(6, 28)
    'hour hand'
    >>> leading_hand(4, 20)
    'draw'
    """
    if 0 <= h < 24 and 0 <= m < 60:
        if (h == 0 or h == 12) and m == 0:
            return 'draw'
        elif (h == 1 or h == 13) and m == 5:
            return 'draw'
        elif (h == 2 or h == 14) and m == 10:
            return 'draw'
        elif (h == 3 or h == 15) and m == 15:
            return 'draw'
        elif (h == 4 or h == 16) and m == 20:
            return 'draw'
        elif (h == 5 or h == 17) and m == 25:
            return 'draw'
        elif (h == 6 or h == 18) and m == 30:
            return 'draw'
        elif (h == 7 or h == 19) and m == 35:
            return 'draw'
        elif (h == 8 or h == 20) and m == 40:
            return 'draw'
        elif (h == 9 or h == 21) and m == 45:
            return 'draw'
        elif (h == 10 or h == 22) and m == 50:
            return 'draw'
        elif (h == 11 or h == 23) and m == 55:
            return 'draw'

        if (h == 0 or h == 12) and m > 0:
            return 'minute hand'
        elif (h == 1 or h == 13) and m > 5:
            return 'minute hand'
        elif (h == 2 or h == 14) and m > 10:
            return 'minute hand'
        elif (h == 3 or h == 15) and m > 15:
            return 'minute hand'
        elif (h == 4 or h == 16) and m > 20:
            return 'minute hand'
        elif (h == 5 or h == 17) and m > 25:
            return 'minute hand'
        elif (h == 6 or h == 18) and m > 30:
            return 'minute hand'
        elif (h == 7 or h == 19) and m > 35:
            return 'minute hand'
        elif (h == 8 or h == 20) and m > 40:
            return 'minute hand'
        elif (h == 9 or h == 21) and m > 45:
            return 'minute hand'
        elif (h == 10 or h == 22) and m > 50:
            return 'minute hand'
        elif (h == 11 or h == 23) and m > 55:
            return 'minute hand'
        else:
            return 'hour hand'





if __name__ == "__main__":
    import doctest
    print(doctest.testmod())