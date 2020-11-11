#!/usr/bin/env python
# coding: utf-8

# In[1]:


def vacuum_cleaner():
    rooms = (int)(input("Total number of rooms: "))
    col = 2
    arr = []
    print("Enter 1 if the half is dirty else Enter 0 for all rooms: ")
    for i in range(rooms):
        arr.append(input().split())
    print("Initial Condition:")    
    print(arr)
    print("\n")
    start_cleaning(rooms, col, arr)
    
def start_cleaning(rooms, col, arr):
    for i in range(rooms):
        if i%2 == 0:
            print("Inside a new room(left-half): ")
            for j in range(col):
                if arr[i][j] == '1':
                    arr[i][j] = '0'
                    print(arr)
                    print("Position Cleaned!!!")
                    if j != 1:
                        print("Now Moving towards the Right Half")
                    print("\n")
                else:
                    print(arr)
                    print("No Operation Needed !!!")
                    if j != 1:
                        print("Now Moving towards the Right Half")
                    print("\n")
                
        else:
            print("Inside a new room(right-half): ")
            for j in reversed(range(col)):
                if arr[i][j] == '1':
                    arr[i][j] = '0'
                    print(arr)
                    print("Position Cleaned!!!")
                    if j != 0:
                        print("Now Moving towards the Left Half")
                    print("\n")
                else:
                    print(arr)
                    print("No Operation Needed !!!")
                    if j != 0:
                        print("Now Moving towards the Left Half")
                    print("\n")
    print("Final Condition: ")                
    print(arr)
    
vacuum_cleaner()

