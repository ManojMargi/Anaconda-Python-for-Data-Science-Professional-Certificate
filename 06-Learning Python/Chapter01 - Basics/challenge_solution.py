# Python code​​​​​​‌‌​​​​​‌​‌‌​‌‌‌​​‌‌‌‌​​​​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    # Your code goes here.
    teststr = teststr.lower()
    temp = ''
    for x in teststr:
        if x.isalpha():
            temp += x
    if temp == temp[::-1]:
        return True
    else:
        return False

# def is_palindrome(teststr):
#     # one way to do it: calculate the reverse of the string
#     # reversestr = ""
#     # strindx = len(teststr)-1
#     # while (strindx >= 0):
#     #     reversestr += teststr[strindx]
#     #     strindx -= 1

#     # if teststr == reversestr:
#     #     return True
#     # return False

#     # more advanced: use the slice trick to reverse the string
#     if teststr == teststr[::-1]:
#         return True
#     return False

# run = True
# while (run):
#     teststr = input("Enter string to test for palindrome or 'exit':")

#     # If the user types "exit" then quit the program
#     if teststr == "exit":
#         run = False
#         break

#     # convert the string to all lower case
#     teststr = teststr.lower()

#     # strip all the spaces and punctuation from the string
#     newstr = ""
#     for x in teststr:
#         if x.isalnum():
#             newstr += x

#     print("Palindrome test:", is_palindrome(newstr))
