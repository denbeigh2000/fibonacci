#!/usr/bin/python2

import sys

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    to_process = [(n, n-1, n-2)]

    def add_to_process_list(n):
        to_process.append((n, n-1, n-2))

    memo = {
        0: 1,
        1: 1,
    }

    while len(to_process) > 0:
        n, f1, f2 = to_process[-1]
        if n in memo:
            del to_process[-1]

        elif f1 in memo and f2 in memo:
            # Add the new fibonacci number to the memoisation table
            memo[n] = memo[f1] + memo[f2]

            # Remove the value we no longer need to calculate
            del to_process[-1]

        else:
            if f1 not in memo:
                add_to_process_list(f1)
            if f2 not in memo:
                add_to_process_list(f2)

    return memo[n]

def main():
    if len(sys.argv) < 2:
        print "Need at least one integer argument"
        return

    target = int(sys.argv[1])
    print fibonacci(target)

if __name__ == '__main__':
    main()
