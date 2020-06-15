def add(*args):
    '''Add 1 or more numbers together'''
    sum = 0
    for arg in args:
        sum += arg
    return sum

def main():
    print('hello')
    print(str(add(1)))
    print(str(add(1, 2)))
    print(str(add(1, 2, 3)))

if __name__ == '__main__':
    main()