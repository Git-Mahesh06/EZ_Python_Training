# You have been given the task of making the content on a social media platform more userfriendly. Your task is to find and return an integer value representing the count of the 
# number of spaces in a given string S. 
# Input: A 
# string S 
# Output : 
# Return an integer value representing the count of the number of spaces in a given string S. 
# Example:
# Input: Hello World Hey 
# Output:2
st=input("enter the string")
s=0
for i in st:
    if i==" ":
        s+=1
print("count of space in given string: ",s)