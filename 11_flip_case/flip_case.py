def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    modified_char = []
    for char in phrase :
        if char.lower() == to_swap.lower() :
            modified_char.append(char.swapcase())
        else : modified_char.append(char)
    return "".join(modified_char)
