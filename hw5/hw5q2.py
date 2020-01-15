NOT_FOUND = -1

def count_occurrences(s, c):
    most_left_index = binary_search_most_left(s,c)
    if most_left_index == NOT_FOUND :
        return 0
    most_right_index = binary_search_most_right(s,c)
    return most_right_index - most_left_index + 1

def binary_search_most_left(some_str,some_char):
    ret_index = NOT_FOUND
    left = 0
    right = len(some_str)-1
    mid = right-(right-left)//2 # = (right+left)/2 other way protects from overflow
    while left < right :
        if some_str[mid] < some_char :
            left = mid + 1
        elif some_str[mid] > some_char:
            right = mid - 1
        else :
            right = mid - 1
            ret_index = mid
        mid = right-(right-left)//2

    return ret_index



def binary_search_most_right(some_str,some_char):
    ret_index = NOT_FOUND
    left = 0
    right = len(some_str)-1
    mid = right-(right-left)//2 # = (right+left)/2 other way protects from overflow
    while left < right :
        if some_str[mid] < some_char :
            left = mid + 1
        elif some_str[mid] > some_char:
            right = mid - 1
        else :
            left = mid + 1
            ret_index = mid
        mid = right-(right-left)//2
    return ret_index


def are_equal(s1, s2):
    for i in range(26):
        s1_occur = count_occurrences(s1,chr(i+ord('a')))
        s2_occur = count_occurrences(s2,chr(i+ord('a')))
        if s1_occur != s2_occur :
            return False
    return True

# just for debugging :
s1_1 = 'aaaab'
s1_2 = 'wxyz'
s1_3 = 'jklmmmm'
s2_1 = 'aaaabb'
s2_2 = 'wxyz'
s2_3 = 'jkllmmm'

s1 = s1_1
s2 = s2_1

def main():
    print('Enter s1:')
    s1 = input()
    print('Enter s2:')
    s2 = input()
    

    res = are_equal(s1, s2)
    if res:
        print('Strings are equal!')
    else:
        print('Strings are not equal...')


# leave intact
if __name__ == '__main__':
    main()


