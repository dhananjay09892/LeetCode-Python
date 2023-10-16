"""
Easy
4.5K
316
Companies
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?"""
def getRow(rowIndex):
    # if rowIndex == 0 : return [1]
    if rowIndex == 0 : 
        return [1]
    elif rowIndex == 1:
        return [1, 1]
    else:
        tempArr = getRow(rowIndex-1)
        result = [1]
        lastVal  = 0
        for v in tempArr:
            if lastVal == 0:
                lastVal = v
            else:
                result.append(lastVal+v)
                lastVal = v
        result.append(1)
    return result

        
print(getRow(1))
print(getRow(2))
print(getRow(3))
print(getRow(4))
# Completed