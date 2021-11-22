from bl_task6 import valid, deploy, calc, calculator

def show_message(message: str):
    print(message)
def get_result(valid_inp: str):
    result = calculator(calc(deploy(valid_inp)))
    if result == -1:
        return show_message('Please dont devide by 0')
    return show_message(f'Your result:\n{result}')
if __name__ == '__main__':
    show_message('Enter your expression:')
    while True:
        valid_input = valid(input())
        if valid_input:
            get_result(valid_input)
            break
        else:
            show_message('Please only use numbers\n:')
            continue