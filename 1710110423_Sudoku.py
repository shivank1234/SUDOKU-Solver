from __future__ import print_function
import Tkinter,tkFileDialog,csv                                                                #Importing GUI,File Modules in Python
import tkSimpleDialog as simpledialog
from Tkinter import *


sudoku_list= [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]                                                                                          #Declaring the list that would contain the numbers to hold the Board Sequence
list1      = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
def open_file():
        global sudoku_list
        global list1
        file_path = tkFileDialog.askopenfilename()
        with open(file_path,'r') as csv_file:
           reader=csv.reader(csv_file)                                                                 #Fetching the file to read the data from it
           sudoku_list = list(reader)
           l=0
           m=0
           while(l<9):
                   while(m<9):
                           list1[l][m]=sudoku_list[l][m]
                           m=m+1
                   m=0
                   l=l+1
           i=0
           j=0
           while (i<9):
                   while(j<9):
                           btn_text[i][j].set(sudoku_list[i][j])
                           sudoku_list[i][j]=int(sudoku_list[i][j])
                           j=j+1
                   j=0
                   i=i+1

def GUI_Input():                                                                                        #Taking Input from the User
        ROW_INP = int(simpledialog.askstring(title="User Input System",
                                  prompt= "Give the Index of the row of the square",parent=window))
        COLUMN_INP = int(simpledialog.askstring(title="User Input System",
                                  prompt= "Give the Index of the Column of the square",parent=window))
        USER_INP = int(simpledialog.askstring(title="User Input System",
                                  prompt= "Give the Input for the Square",parent=window))
        btn_text[ROW_INP][COLUMN_INP].set(USER_INP)
        sudoku_list[ROW_INP][COLUMN_INP]=USER_INP
        list1[ROW_INP][COLUMN_INP]=USER_INP

def find_empty_location(arr,l):                                                                #Finding an empty location
    row=0
    col=0
    while (row <9): 
        while (col <9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
            col=col+1
        col=0
        row=row+1
    return False

def used_in_row(arr,row,num):                                                                   #Checking if the num is used in that row 
    i=0
    while (i<9): 
        if(arr[row][i] == num): 
            return True
        i=i+1
    return False

def used_in_col(arr,col,num):                                                                    #Checking if the num is used in that column
    i=0
    while (i<9): 
        if(arr[i][col] == num): 
            return True
        i=i+1
    return False

def used_in_box(arr,row,col,num):                                                               #Checking if the num is used in that Box
    i=0
    j=0
    while (i<3): 
        while (j<3): 
            if(arr[i+row][j+col] == num):
                return True
            j=j+1
        j=0
        i=i+1
    return False




def check_location_is_safe(arr,row,col,num): 
      
    # Check if 'num' is not there in current row,column,box
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num)

def printq(list1):
        i=0
        j=0
        while(i<9):
                while(j<9):
                        print(list1[i][j],end=" ")
                        j=j+1
                j=0
                i=i+1
                print("\n")
        print("End of Intermediate step")

def prints(arr,list1):
        i=0
        j=0
        z=0
        while(i<9):
                while(j<9):
                        list1[i][j]=arr[i][j]
                        j=j+1
                        printq(list1)     
                j=0
                i=i+1
                
        
def solve():

    i=0                                                                                       #Row Constraint
    j=0
    s=0
    zero_count=0
    column=0
    arr=sudoku_list
    while(i<9):
            while(j<9):
                    if(arr[i][j]!=0):
                            s=s+arr[i][j]
                    else:
                            zero_count=zero_count+1
                            column=j
                    j=j+1
            j=0
            if(zero_count==1):
                    arr[i][column]=45-s
                    prints(arr)
            i=i+1


    i=0                                                                                       #Column Constraint
    j=0
    s=0
    zero_count=0
    row=0
    while(j<9):
            while(i<9):
                    if(arr[i][j]!=0):
                            s=s+arr[i][j]
                    else:
                            zero_count=zero_count+1
                            row=i
                    i=i+1
            i=0
            if(zero_count==1):
                    arr[row][j]=45-s
            j=j+1
        
    
    solve_sudoku(sudoku_list)
    prints(sudoku_list,list1)
    global sudoku_list
    global btn_text
    i=0
    j=0
    while(i<9):
            while(j<9):
                    btn_text[i][j].set(sudoku_list[i][j])
                    j=j+1
            j=0
            i=i+1
    


def solve_sudoku(arr):
         
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function     
    l=[0,0]
      
    # If there is no unassigned location, we are done     
    if(not find_empty_location(arr,l)): 
        return True
      
    row=l[0] 
    col=l[1] 
      
    # Taking the digits from 1-9
    for num in range(1,10): 
          
        if(check_location_is_safe(arr,row,col,num)): 
              
            arr[row][col]=num
            
            if(solve_sudoku(arr)): 
                return True
  
            arr[row][col] = 0
              
    # this triggers backtracking         
    return False 
btn_text= [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

window=Tkinter.Tk()
window.title("SUDOKU")
top_frame= Tkinter.Frame(window).grid()
btn1=Tkinter.Button(top_frame, text="Solve    ",fg="red", command=solve).grid(row=0 ,column =0)           #Declaring Buttons to solve the SUDOKU
btn2=Tkinter.Button(top_frame ,text="Open file",fg="Purple", command=open_file ).grid(row =0,column=1)
middle_frame=Tkinter.Frame(window).grid()
bottom_frame=Tkinter.Frame(window).grid()                                                                 #Declaring frames for the SUDOKU Puzzle

i=0
j=0

while (i<9):                                                                                              #Preparing the list to store references to buttons
        while(j<9):
                btn_text[i][j]=Tkinter.StringVar()
                j=j+1
        j=0
        i=i+1

for rowindex in range (9):
        for colindex in range (9):
            if (rowindex in (0,1,2,6,7,8) and colindex in (3,4,5) or 
                (rowindex in (3,4,5) and colindex in (0,1,2,6,7,8))):
                    colour="light blue"
            else:
                colour="green"
                
            btn=Tkinter.Button(bottom_frame, width=8, height=4,command= GUI_Input, bg=colour,fg="black",textvariable=btn_text[rowindex][colindex]) #Declaring Buttons for Squares
            btn.grid(row=rowindex+1, column=colindex)
            
window.mainloop()

                        
        
                        

