"""
Bynary searchin, 1-st task

"""


def binary_search(l1, ind, high, low=0):
    if (high < low):
        return None
    else:
        res = low + ((high - low) // 2)
        if l1[res] > ind:
            return binary_search(l1, ind, res - 1, low)
        elif l1[res] < ind:
            return binary_search(l1, ind, high, res + 1)
        else:
            return res

if __name__ == '__main__':

    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], high=9, ind=9))