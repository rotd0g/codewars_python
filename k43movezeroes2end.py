
def move_zeros(lst):
    """
    Write an algorithm that takes an array and moves all of the zeros
    to the end, preserving the order of the other elements.
    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
    """

    for i in lst:
        if i == 0:
            lst.remove(i)  # Remove the element from the array
            lst.append(i)  # Append the element to the end
    return lst



    # j = 0
    # for i in range(len(lst)):
    #     if lst[i] != 0:
    #         lst[j], lst[i] = lst[i], lst[j]
    #         j += 1
    # return lst

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

