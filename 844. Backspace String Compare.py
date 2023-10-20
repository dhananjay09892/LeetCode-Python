"""
844. Backspace String Compare
Easy
7.2K
327
Companies
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
"""
# s= "ab#cd#"
# index =  s.find('#') - 1
# index1 =  s.find('#')
# listS = list(s)
# listS.pop(index1)
# listS.pop(index)
# s = "".join(listS)
# print(s)
def removeHash(s):
    List = list(s)
    indexes = [i for i, ltr in enumerate(s) if ltr == '#']
    indexes.reverse()
    for i in indexes:
        List.pop(i)
    s = "".join(List)
    return s

def addHash(s):
    List = list(s)
    indexes = [i for i, ltr in enumerate(s) if ltr == '#']
    indexes.reverse()
    for i in indexes:
        j = i - 1
        while i > 0 and s[j] == '#':
            j -= 1
        print(j)
        if j >= 0:
            List[j] = '#'
    s = "".join(List)
    return s
def backspaceCompare(s,t):
    def process_string(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return stack
    
    return process_string(s) == process_string(t)

s = "c##vnvr"
t = "c##vn#nvr"
print(backspaceCompare(s,t))
