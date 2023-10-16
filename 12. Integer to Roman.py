# 12. Integer to Roman
# Medium
# 6.4K
# 5.3K
# Companies
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

 

# Example 1:

# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
# Example 2:

# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 3:

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= num <= 3999
class Solution:
    def intToRoman(self, num: int) -> str:
        # I can be placed before V (5) and X (10) to make 4 and 9. 
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        # C can be placed before D (500) and M (1000) to make 400 and 900.
        # Given an integer, convert it to a roman numeral.
        result = ''
        # M 1000
        while num >= 1000:
            result += 'M'
            num -= 1000
        # D 500
        if num >= 500:
            # CM 900
            if num >= 900:
                result += 'CM'
                num -= 900
            else:
                result += 'D'
                num -= 500
        # C 100
        while num >= 100:
            # CD 400
            if 400 <= num:
                result += 'CD'
                num -= 400
            else:
                result += 'C'
                num -= 100
        # L 50
        if num >= 50:
            # XC 90
            if 90 <= num:
                result += 'XC'
                num -= 90
            else:
                result += 'L'
                num -= 50
        # X 10
        while num >= 10:
            # XL 40
            if 40 <= num:
                result += 'XL'
                num -= 40
            else:
                result += 'X'
                num -= 10
        # V 5
        if num >= 5:
            # IX 9
            if 9 == num:
                result += 'IX'
                num -= 9
                return result
            else:
                result += 'V'
                num -= 5
        # I             1
        while num >= 1:
            # IV 4
            if 4 == num:
                result += 'IV'
                num -= 4
                return result
            else:
                result += 'I'
                num -= 1
        return result
# Completed