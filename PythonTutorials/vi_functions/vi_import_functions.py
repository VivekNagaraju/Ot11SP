'''
Created on 06-Nov-2025

@author: Vivek
'''
from vi_functions.vi_arguments import add, var_len # importing specific functions
# from vi_functions.vi_arguments import * # importing everything from vi_arguments
from vi_functions.vi_func_intro import welcome as wc # aliasing

wc()
add(4, 6)
var_len(3, 5, 6, 7, 8, 299)