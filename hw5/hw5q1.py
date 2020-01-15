import ast


def compare_strings(s1, s2):
    s1_copy = s1.lower()
    s2_copy = s2.lower()
    len_s1 = len(s1_copy)
    len_s2 = len(s2_copy) 
    same_count = 0
    for i in range(min(len_s1,len_s2)):
        if ord(s1_copy[i]) > ord(s2_copy[i]):
            return False
        if s1_copy[i]==s2_copy[i]:
            same_count += 1
    if len_s1 > len_s2 and same_count==len_s2:
        return False
    return True


def sort_list_of_strings(str_lst):
    for i in range(len(str_lst)):
        for j in range(len(str_lst)-1):
            if not compare_strings(str_lst[j],str_lst[j+1]):
                str_lst[j+1],str_lst[j] = str_lst[j],str_lst[j+1]
                
# just for debugging : 
str_lst1 = ['b','bb','bB','bbB','']
str_lst2 = ['.a.a','.a.a','.a.','.a','..','...','.']
str_lst3 = ['ert','erT','eRt','Ert','eRT','ErT','ERt','ERT']
str_lst4 = ['aaaaa','aaaaab','aaaa','aaaA','aa133']
lst = str_lst1

# leave intact
def main():
    #print('Insert a list of strings:')
    #lst = ast.literal_eval(input())
    sort_list_of_strings(lst)
    print()
    print('The sorted list:')
    print(lst)


if __name__ == '__main__':
    main()

