from hash_table_ayrik_zincirleme import seperateChainingHashST
import time
from tkinter import *

def pull_data_frombook(file_name):
    book = open(file_name,"r")
    book = book.read().lower()

    punctuations = '''!()-[]};{:'"\,<>./?@#$%^&*_~'''
    punctless = ""
    for char in book:
        if char=="\n":
            punctless = punctless + " "
        elif char not in punctuations:
            punctless = punctless + char

    words=punctless.split(" ")
    i=0
    while i<len(words):
        if words[i]=='':
            del(words[i])
        else:
            i+=1
    return words

def Unordered_linked_list(symbolTable,words):
    start=time.perf_counter()
    for word in words:
        symbolTable.put(word)
    end=time.perf_counter()
    timeOFcreation=end-start

    addedWords=["qwerty","asdfg","zxcvb","tyui"]
    start=time.perf_counter()
    for word in addedWords:
        symbolTable.put(word)
    end=time.perf_counter()
    avg_putTime=(end-start)/len(addedWords)

    hit_words=["skunk","had","as","determined","blacksnake"]
    start=time.perf_counter()
    for word in hit_words:
        symbolTable.get(word)
    end=time.perf_counter()
    ort_get_hit=(end-start)/len(hit_words)

    miss_kelimeler=["ninos","kedis","istinye","abu"]
    start=time.perf_counter()
    for word in miss_kelimeler:
        symbolTable.get(word)
    end=time.perf_counter()
    ort_get_miss=(end-start)/len(miss_kelimeler)

    print("The creation time of Symbol Table={}".format(timeOFcreation))
    print("Average put time={}".format(avg_putTime))
    print("Average get time (hit)={}".format(ort_get_hit))
    print("Average get time (miss)={}".format(ort_get_miss))
    print("\n")

def Separate_chaining(words):
    root = Tk()
    root.title("Bar Graph")
    root.geometry('1280x500')
    can = Canvas(root,width=1500,height=500)
    can.pack()
    symbolTable = seperateChainingHashST(97)
    for word in words:
        a=0
        x1=6
        x2=14
        i,j = symbolTable.put(word)
        while(a!=i):
            x1=x2+5
            x2=x1+8
            a+=1
        try:
            can.create_rectangle(x1,500,x2,500-j*10+5, fill="grey")
        except TclError:
            print("Procces stoped")
            return
        can.update()
    root.mainloop()
