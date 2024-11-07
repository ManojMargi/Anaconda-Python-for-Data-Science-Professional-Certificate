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
