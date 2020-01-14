import ast


def second_best_recursive(lst):
    if len(lst)==2:
        max_n = max(lst[0],lst[1])
        min_n = min(lst[0],lst[1])
        lst[1] = max_n
        lst[0] = min_n
        return lst[0]
    first_item = lst[0]
    del lst[0]
    second_highest = second_best_recursive(lst)
    highest = lst[-1]
    if first_item > highest :
        lst[-1]=first_item
        return highest
    elif first_item > second_highest :
        return first_item
    return second_highest
    

    


def main():
    print('Please enter a list of numbers of size >= 2:')
    lst = ast.literal_eval(input())
    print('The second largest number in the list is {}'.format(second_best_recursive(lst)))


if __name__ == '__main__':
    main()
