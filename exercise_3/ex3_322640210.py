''' Exercise #67. Python for Engineers.'''
import sys
from typing import Union, List

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
    if n < 0:
        raise RuntimeError("input number must be positive")
    if n <= 3:
        return 1
    result = climb_combinations(n - 1) + climb_combinations(n - 4)
    return result

#########################################
# Question 3.a - do not delete this comment
#########################################


def weigh_str(input_str: str) -> Union[int, float]:
    if not input_str:
        raise RuntimeError("input must include one char at least")
    if len(input_str) == 1:
        return 0

    current_calc = ord(input_str[0]) - ord(input_str[-1])
    current_result = current_calc / abs(current_calc) if current_calc else 0

    next_input_str = input_str[1:-1]
    general_result = current_result + (0 if not next_input_str else weigh_str(input_str=next_input_str))

    return general_result


#########################################
# Question 3.b - do not delete this comment
#########################################
def weigh_str_efficient(input_str: str, index: int = 0) -> Union[int, float]:
    if not input_str:
        raise RuntimeError("input must include one char at least")

    right_idx = len(input_str) - index - 1
    if index >= right_idx:
        return 0

    current_calc = ord(input_str[index]) - ord(input_str[right_idx])
    current_result = current_calc / abs(current_calc) if current_calc else 0

    next_idx = index + 1
    general_result = current_result + weigh_str_efficient(input_str=input_str, index=next_idx)

    return general_result


#########################################
# Question 4 - do not delete this comment
#########################################
def find_num_changes_rec(n: int, lst: List[int]) -> int:
    if not n:
        return 1
    if n < 0 or not lst:
        return 0

    array_prep = sorted(set(lst))
    greater_num, new_array = array_prep[-1], array_prep[:-1]

    result = find_num_changes_rec(n - greater_num, array_prep) + find_num_changes_rec(n, new_array)
    return result

#########################################
# Question 5.a - do not delete this comment
#########################################


def sum_nested(lst: Union[int, float, str, List]) -> float:
    if isinstance(lst, str):
        return 0.0
    elif isinstance(lst, (int, float)):
        return float(abs(lst))
    elif isinstance(lst, List):
        first_obj, next_array = lst[0], lst[1:] if len(lst) > 1 else 0
        result = sum_nested(first_obj) + sum_nested(next_array)
        return result
    else:
        raise TypeError(f"input type {type(lst).__name__} is inappropriate ")


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
    print(find_num_changes_rec(-1, [1, 2, 5, 6]) == 0)
    print(find_num_changes_rec(20, []) == 0)
    print(find_num_changes_rec(1, [3,4,5]) == 0)
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
