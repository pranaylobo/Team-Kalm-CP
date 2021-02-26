import sys

def middle_char(txt,mid1):
    
    if len(txt)>0:

        mid = int((len(txt) - 1)/2)
        

        print(txt[mid],end="")

        middle_char(txt[:mid],mid1)
        middle_char(txt[mid+1:],mid1)
       
        

mid1=0
for i in range(int(input())):
    x1=int(input())
    text=input()
    var=middle_char(text,mid1)
    print("\n")



