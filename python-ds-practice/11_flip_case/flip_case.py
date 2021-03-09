def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst = []
    for letter in phrase:
        if to_swap.islower():
            if letter == to_swap:
                lst.append(letter.upper())
            elif letter == to_swap.upper():
                lst.append(letter.lower())
            else:
                lst.append(letter)
        else:
            if letter == to_swap:
                lst.append(letter.lower())
            elif letter == to_swap.lower():
                lst.append(letter.upper())
            else: lst.append(letter)
    result = ''.join(lst)


    return result
