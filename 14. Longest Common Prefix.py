"""
Easy
16.1K
4.2K
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters."""
def longestCommonPrefix(strs):
    result = ''
    for index,i in enumerate(strs[0]):
        tempchar = i[0]
        for j in enumerate(strs):
            if len(j[1]) > index:
                if j[1][index] == tempchar:
                    if j[0] == len(strs)-1: result = result + tempchar
                else: return result
            else: return result
    return result 
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))
strs = ["ab", "a"]
print(longestCommonPrefix(strs))
# def longestCommonPrefix(strs):
#     result = ''
#     # Find shortest len 
#     for index,i in enumerate(strs[0]):
#         tempchar = i[0]
#         # print("temp char = ",tempchar)
#         for j in enumerate(strs):
#             if len(j[1])-1 >= index:
#                 # index of word = j[0]
#                 print("value of j = ",j[1])
#                 # print("value of j char = ",j[1][index])
#                 # print("j index value =",j[index])
#                 if j[1][index] == tempchar:
#                     if j[0] == len(strs)-1:
#                         result = result + tempchar
#                         # print(result)
#                     else:
#                         continue
#                 else:
#                     return result
#             else:
#                 return result
#     return result 
# strs = ["flower","flow","flight"]
# print(longestCommonPrefix(strs))
# strs = ["dog","racecar","car"]
# print(longestCommonPrefix(strs))
# strs = ["ab", "a"]
# print(longestCommonPrefix(strs))