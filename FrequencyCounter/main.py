from functions import *
from Binary_Search_Tree_bazli_ST import BST
from sequential_search_symbol_table import SequentialST
from binary_search_symbol_table import BinarySearchST

book = pull_data_frombook("book.txt")


Unordered_linked_list(SequentialST(),book)
Unordered_linked_list(BST(),book)
Unordered_linked_list(seperateChainingHashST(97),book)
Unordered_linked_list(BinarySearchST(),book)


Separate_chaining(book)