''' Exercise #1 '''
from typing import Union

#########################################
# Question 1 - do not delete this comment
#########################################


def hi_name(name: str) -> None:
    # Write the rest of the code for question 1 below here.
    print(f"Hi {name.title()}{3*'!'}")


#########################################
# Question 2 - do not delete this comment
#########################################

def deltoid(AB: float, AD: float, ABD: float, ABC: float) -> None:
    # Write the rest of the code for question 2 below here.
    perimeter = 2 * (AB + AD)
    print(f"Perimeter is: {perimeter}")

    ac, bd = ABC - 2 * AB, ABD - AB - AD
    print(f"AC: {ac}")
    print(f"BD: {bd}")

    s = ac * bd / 2
    print(f"S: {s}")


#########################################
# Question 3 - do not delete this comment
#########################################
def divide_by_seven(num: str) -> Union[int, float, None]:
    # Write the rest of the code for question 3 below here.
    divided_by = 7
    _num = int(num)

    if not _num % divided_by:
        print(f"The number {num} is divisible by {divided_by}")
        return _num / divided_by

    print(f"The number {num} is not divisible by {divided_by}")


#########################################
# Question 4 - do not delete this comment
#########################################
def str_mixer(text: str, copies1: int, copies2: int) -> None:
    # Write the rest of the code for question 4 below here.
    sub1, sub2 = '', ''

    for idx, char in enumerate(text):
        if not idx % 2:
            sub1 += char
        else:
            sub2 += char

    print(f"{copies1 * sub1}{copies2 * sub2}")


#########################################
# Question 5 - do not delete this comment
#########################################
def rearrange_str(name: str, ind1: int, ind2: int):
    # Write the rest of the code for question 5 below here.
    pass

#########################################
# Question 6 - do not delete this comment
#########################################
def divisor_checker(digits, divisor): 
    # Write the rest of the code for question 6 below here.
    pass

#########################################

if __name__=='__main__':

    # Ex1 tests
    hi_name('Tom')
    hi_name('oxana')

    # Ex2 tests
    deltoid(10.0, 5.0, 28.0, 26.0)

    # Ex3 tests
    divide_by_seven('77')
    divide_by_seven('-17')

    # Ex4 tests
    str_mixer('tom', 3, 4)
    str_mixer('oxana', 2, 3)

    # Ex5 tests
    rearrange_str('ibaccaMleTvivA', 7, 10)
    rearrange_str('ibaccaMleTvivA', 6, 30)
    rearrange_str('ibaccaMleTvivA', 8, 7)
    rearrange_str('', 7, 10)

    # Ex6 tests
    divisor_checker('428315', 4)
    divisor_checker('428315', 5)
