def cercanias(linea, sentido):
    """
    >>> cercanias(3,'N')
    12
    >>> cercanias(7,'N')
    0
    >>> cercanias(4,'S')
    15
    >>> cercanias(2,'W')
    0
    """
    if sentido == 'N':
        if linea == 1:
            return 8
        elif linea == 2:
            return 10
        elif linea == 3:
            return 12
        elif linea == 4:
            return 14
        else:
            return 0
    elif sentido == 'S':
        if linea == 1:
            return 7
        elif linea == 2:
            return 9
        elif linea == 3:
            return 13
        elif linea == 4:
            return 15
        else:
            return 0
    else:
        return 0


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())