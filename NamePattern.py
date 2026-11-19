n = int(input("Size of name = ")) # Size must be between 1 to 3
def Character_Rect(char,times): # Functions for Rectangles of Characters
    for j in range(n*times):
        print(char,end="")
row1 = [("S",5),(" ",1),("H",1),(" ",3),("H",1),(" ",1),("I",5),(" ",1),("V",1),(" ",3),("V",1),(" ",1),("A",5),(" ",1),("M",2),(" ",1),("M",2),(" ",3),("H",1),(" ",3),("H",1),(" ",1),("U",1),(" ",3),("U",1)]
for i in range(n):    
    for char,times in row1:
        Character_Rect(char,times)
    print()     

row2 = [("S",1),(" ",5),("H",1),(" ",3),("H",1),(" ",3),("I",1),(" ",3),("V",1),(" ",3),("V",1),(" ",1),("A",1),(" ",3),("A",1),(" ",1),("M",1),(" ",1),("M",1),(" ",1),("M",1),(" ",3),("H",1),(" ",3),("H",1),(" ",1),("U",1),(" ",3),("U",1)]
for i in range(n):
    for char,times in row2:
        Character_Rect(char,times)
    print()

row3 = [("S",5),(" ",1),("H",5),(" ",3),("I",1),(" ",3),("V",1),(" ",3),("V",1),(" ",1),("A",5),(" ",1),("M",1),(" ",3),("M",1),(" ",3),("H",5),(" ",1),("U",1),(" ",3),("U",1)]        
for i in range(n):
    for char,times in row3:
        Character_Rect(char,times)                               
    print()

row4 =[(" ",4),("S",1),(" ",1),("H",1),(" ",3),("H",1),(" ",3),("I",1),(" ",4),("V",1),(" ",1),("V",1),(" ",2),("A",1),(" ",3),("A",1),(" ",1),("M",1),(" ",3),("M",1),(" ",3),("H",1),(" ",3),("H",1),(" ",1),("U",1),(" ",3),("U",1)]            
for i in range(n):
    for char,times in row4:
        Character_Rect(char,times)                                
    print()

row5 = [("S",5),(" ",1),("H",1),(" ",3),("H",1),(" ",1),("I",5),(" ",3),("V",1),(" ",3),("A",1),(" ",3),("A",1),(" ",1),("M",1),(" ",3),("M",1),(" ",3),("H",1),(" ",3),("H",1),(" ",2),("U",3)]                               
for i in range(n):
    for char,times in row5:
        Character_Rect(char,times)                         
    print()
                                           
