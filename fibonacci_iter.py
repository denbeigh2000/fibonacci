import sys

def fibonacci(target):
    if target == 1:
        return 1

    n = 1
    f = 1
    f_1 = 1

    while n < target:
        old_f = f
        f = f + f_1
        f_1 = old_f
        n += 1

    return f


def main():
    if len(sys.argv) < 2:
        print "Need at least one integer argument"
        return

    target = int(sys.argv[1])
    print fibonacci(target)

if __name__ == '__main__':
    main()
