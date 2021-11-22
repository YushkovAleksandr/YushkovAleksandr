"""
Task 2 with summ of numbers in list

"""

def sum(lst):
    count = 0
    for elem in lst:
        if type(elem) == type([]):
            count = count + sum(elem)
        else:
            count = count + elem
    return count

if __name__ == '__main__':
    print(sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))
    