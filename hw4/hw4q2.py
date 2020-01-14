def digit_match(n, m):
    if (n<10 or m<10):
        return int(n%10==m%10)
    curr_digit_m = m%10
    curr_digit_n = n%10
    return digit_match(n//10,m//10)+int(curr_digit_m==curr_digit_n)


def main():
    print('Enter n:')
    n = int(input())
    print('Enter m:')
    m = int(input())
    print('{} and {} share {} common digits!'.format(n, m, digit_match(n, m)))


if __name__ == '__main__':
    main()
