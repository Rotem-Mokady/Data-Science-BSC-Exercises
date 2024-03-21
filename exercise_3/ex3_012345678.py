''' Exercise #67. Python for Engineers.'''
import sys

sys.setrecursionlimit(10000)

#########################################
# Question 1.a - do not delete this comment
#########################################


def threebonacci_rec(n: int) -> int:
    if n < 3:
        return n
    result = threebonacci_rec(n - 1) + threebonacci_rec(n - 2) + threebonacci_rec(n - 3)
    return result


#########################################
# Question 1.b - do not delete this comment
#########################################
def k_bonacci(n: int, k: int) -> int:
    if n < k:
        return n
    result = sum([k_bonacci(n - i - 1, k) for i in range(k)])
    return result


#########################################
# Question 2 - do not delete this comment
#########################################
def climb_combinations(n: int) -> int:
    if n <= 3:
        return 1
    result = climb_combinations(n - 1) + climb_combinations(n - 4)
    return result




#########################################
# Question 3.a - do not delete this comment
#########################################
def weigh_str(input_str):
    pass  # replace this with your implementation


#########################################
# Question 3.b - do not delete this comment
#########################################
def weigh_str_efficient(input_str, index=0):
    pass # replace this with your implementation


#########################################
# Question 4 - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    pass  # replace this with your implementation


#########################################
# Question 5.a - do not delete this comment
#########################################
def sum_nested(lst):
    pass  # replace this with your implementation


#########################################
# Question 5.b - do not delete this comment
#########################################
def count_construct(target, word_bank):
    pass  # replace this with your implementation


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    # Question 1.a tests - you can and should add more
    print("Question 1.a tests")
    print(threebonacci_rec(0) == 0)
    print(threebonacci_rec(5) == 11)
    print(threebonacci_rec(8) == 68)

    #Question 1.b tests - you can and should add more
    print("Question 1.b tests")
    print(k_bonacci(0, 2) == 0)
    print(k_bonacci(5, 2) == 5)
    print(k_bonacci(8, 2) == 21)
    print(k_bonacci(0, 3) == 0)
    print(k_bonacci(5, 3) == 11)
    print(k_bonacci(8, 3) == 68)
    print(k_bonacci(0, 5) == 0)
    print(k_bonacci(5, 5) == 10)
    print(k_bonacci(8, 5) == 76)

    #Question 2 tests - you can and should add more
    print("Question 2.a tests")
    print(climb_combinations(1) == 1)
    print(climb_combinations(4) == 2)
    print(climb_combinations(5) == 3)
    print(climb_combinations(6) == 4)
    print(climb_combinations(7) == 5)
    print(climb_combinations(8) == 7)
    print(climb_combinations(9) == 10)
    print(climb_combinations(10) == 14)
    print(climb_combinations(11) == 19)
    print(climb_combinations(12) == 26)

    #Question 3.a tests - you can and should add more
    print("Question 3 tests")
    print(weigh_str("a") == 0)
    print(weigh_str("aba") == 0)
    print(weigh_str("aa") == 0)
    print(weigh_str("AZ") == -1)
    print(weigh_str("cba") == 1)
    print(weigh_str("acsabdrZ") == 0)
    print(weigh_str("DDDDaaaa") == -4)

    #Question 3.b tests - you can and should add more
    print("Question 3 tests")
    print(weigh_str_efficient("a") == 0)
    print(weigh_str_efficient("aba") == 0)
    print(weigh_str_efficient("aa") == 0)
    print(weigh_str_efficient("AZ") == -1)
    print(weigh_str_efficient("cba") == 1)
    print(weigh_str_efficient("acsabdrZ") == 0)
    print(weigh_str_efficient("DDDDaaaa") == -4)

    #Question 4 tests - you can and should add more
    print("Question 4.a tests")
    print(find_num_changes_rec(5,[1,2,5,6]) == 4)
    print(find_num_changes_rec(4,[1,2,5,6]) == 3)
    print(find_num_changes_rec(0,[1,2,5,6]) == 1)
    print(find_num_changes_rec(105,[1,105,999,100]) ==3)

    #Question 5.a tests - you can and should add more
    print("Question 5.a tests")
    print(sum_nested([1, 2, [3, 4], [5, [6, 7], 8], 9]) == 45)
    print(sum_nested([1, 2, [-3, -4.5]]) == 10.5)
    print(sum_nested([1, 2, [-3, -4.5], 'abc', [5, 'abc', [-4, 0.5]]]) == 20.)

    #Question 5.b tests - you can and should add more
    print("Question 5.b tests")
    print(count_construct('purple', ["purp", "p", "ur", "le", "purpl"]) == 2)
    print(count_construct('abcdef', ["ab", "abc", "cd", "def", "abcd"]) == 1)
    print(count_construct('aaaaaaaaaaaaaaaaaaaaaaaz', ["a", "aa", "aaa", "aaaa", "aaaaa"]) == 0)

    pass
# ============================== END OF FILE =================================
