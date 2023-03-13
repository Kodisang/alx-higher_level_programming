def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")
    for i in my_list:
        if not isinstance(i, int):
            raise TypeError("List must contain only integers")
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return multiples
