#!/usr/bin/python
sum_of_n = lambda n : (n * (n + 1))/2

def mul_of_3_and_5(n):
    n = n - 1
    return 3 * sum_of_n(n/3) + 5 * sum_of_n(n/5) - 15 * sum_of_n(n/15)

if __name__ == '__main__':
	N = int(raw_input())
	print mul_of_3_and_5(N)

