# abelian_printout.py
# Max Liang
# created 04/18/2022
# Description:
#
#

import abelian


def print_out(ele_list):
    string = ""
    for e in ele_list:
        string += f"X Z_{e} "

    string = string.lstrip("X")
    print(string)


def abelian_print(factor_list):
    for i in range(len(factor_list)):
        f_list = factor_list.copy()
        for j in range(i, len(f_list)-1):
            f_list[1+i] = f_list[0+i] * f_list[1+i]
            f_list.pop(0+i)
            print_out(f_list)


