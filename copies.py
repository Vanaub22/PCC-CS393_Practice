#to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). 
s=input("Enter the string: ")
if len(s)<2:
    print("Wrong input \n Enter again!")
    s=input("Enter the new string: ")
def modify(str):
    l=str[len(str)-2:]
    ms=4*l
    print("The modified string is :",ms)
modify(s)
    
