import data_task6 as data6

def valid(input: str):
    for i in input:
        if i in '1234567890().' or i in data6.operations:
            continue
        else:
            return None
    else:
        return input
def deploy(valid_inp: str):
    number = ''
    for i in valid_inp:
        if i in '1234567890.':
            number += i
        elif number:
            yield float(number)
            number = ''
        elif not number and i in '-':
            number += i
            continue
        if i in data6.operations or i in '()':
            yield i
    if number:
        yield float(number)
def calc(deployd):
    tmp = []
    for i in deployd:
        if i in data6.operations:
            while tmp and tmp[-1] != '(' and data6.operations[i][0] <= data6.operations[tmp[-1]][0]:
                yield tmp.pop()
            tmp.append(i)
        elif i == ')':
            while tmp:
                x = tmp.pop()
                if x == '(':
                    break
                yield x
        elif i == '(':
            tmp.append(i)
        else:
            yield i
    while tmp:
        yield tmp.pop()
def calculator(calc):
    arr = []
    for i in calc:
        try:
            if i in data6.operations:
                b = arr.pop()
                a = arr.pop()
                arr.append(data6.operations[i][1](a, b))
            else:
                arr.append(i)
        except ZeroDivisionError:
            return -1
    return arr[0]