def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    freq1 = {digit: str(num1).count(str(digit)) for digit in range(10)}
    freq2 = {digit: str(num2).count(str(digit)) for digit in range(10)}
    return freq1 == freq2
