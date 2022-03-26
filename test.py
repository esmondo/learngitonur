def summation():
    pass

def multiply(number, multip: 2):
    """ This function multipley input number

        Args:
            number(int): Input number to multiply

        Return
            result(int): Output number
    """
    number_type = type(number)
    if number_type is int:
        result = number * multip

    return result