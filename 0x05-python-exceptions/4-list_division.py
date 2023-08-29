#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    function that divides element by element 2 lists.
    """

    new_list = []
    for i in range (list_length):
        try:
            divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
        finally:
            new_list.append(divide)
    return (new_list)

