def sum_of_integers() -> int:
    a = input('Please enter an integer: ')
    b = input('Please enter a second integer: ')
    sum = int(a) + int(b)
    return sum

if __name__ == '__main__':
    print(sum_of_integers())
