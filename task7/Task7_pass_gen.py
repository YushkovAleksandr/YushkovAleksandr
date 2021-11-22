import random
"""
Password generator implementation
"""
def get_action(message):
     return input(message)
def pas_gen():
    simple_symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    special_symbols = '!@#$%^&*;/,._-[]{}()'
    operation = get_action(
 """Choose what the password will consist of
 1: Only letters and numbers 
 2: Letters, numbers and symbols
  """) 
    if operation == "1":
        all = simple_symbols
    elif operation == "2":
        all = simple_symbols + special_symbols
    else:
        print("Make a choice: 1 or 2")
        return
    length = int(input('Pleas, enter lenпth of your password:\n'))
    password = "".join(random.sample(all, length))
    print(password)
if __name__ == "__main__":
    pas_gen() 