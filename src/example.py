# Solution 
def add(*args):
    '''Add 1 or more numbers together'''
    total = 0
    for arg in args:
        total += arg
    return total

def main():
    print('add(1) = ' + str(add(1)))
    print('add(1, 2) = ' + str(add(1, 2)))
    print('add(1, 2, 3) = ' + str(add(1, 2, 3)))

if __name__ == '__main__':
    main()