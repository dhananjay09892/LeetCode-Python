"""13. Roman to Integer
Easy
12.6K
744
Companies
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer."""
# class Solution:
def romanToInt(s):
    # str to array 
    result = 0
    for i in range(len(s)):
        # M 1000
        if i == len(s)-1:
            if s[i] == "M" and s[i-1]+s[i] != "CM": result += 1000 
            if s[i] == "D" and s[i-1]+s[i] != "CD": result += 500
            if s[i] == "C" and s[i-1]+s[i] != "XC": result += 100 
            if s[i] == "L" and s[i-1]+s[i] != "XL": result += 50
            if s[i] == "X" and s[i-1]+s[i] != "IX": result += 10 
            if s[i] == "V" and s[i-1]+s[i] != "IV": result += 5 
            if s[i] == "I" : result += 1 
        elif s[i] == 'M':
            if s[i-1] + s[i] == 'CM'and i != 0:
                continue
            else:
                result +=1000
        # CM    900
        elif i!= len(s) and i < len(s)-1:
            if s[i]+s[i+1] == 'CM':
                result += 900
            # D 500
            elif s[i] == 'D':
                if s[i-1] + s[i] == 'CD'and i != 0:
                    continue
                else:
                    result +=500
            # CD    400
            elif i!= len(s) and i < len(s)-1:
                if s[i]+s[i+1] == 'CD':
                    result += 400
                # C 100
                elif s[i] == 'C':
                    if s[i-1] + s[i] == 'XC'and i != 0:
                        continue
                    else:
                        result +=100
                # XC    90
                elif i!= len(s) and i < len(s)-1:
                    if s[i]+s[i+1] == 'XC':
                        result += 90
                    # L 50
                    elif s[i] == 'L':
                        if s[i-1] + s[i] == 'XL'and i != 0:
                            continue
                        else:
                            result +=50
                    # XL    40
                    elif i!= len(s) and i < len(s)-1:
                        if s[i]+s[i+1] == 'XL':
                            result += 40
                        # X 10
                        elif s[i] == 'X':
                            if s[i-1] + s[i] == 'IX'and i != 0:
                                continue
                            else:
                                result +=10
                        # IX    9
                        elif i!= len(s) and i < len(s)-1:
                            if s[i]+s[i+1] == 'IX':
                                result += 9
                            # V 5
                            elif s[i] == 'V':
                                if s[i-1] + s[i] == 'IV'and i != 0:
                                    continue
                                else:
                                    result +=5
                            # IV    4
                            elif i!= len(s) and i < len(s)-1:
                                if s[i]+s[i+1] == 'IV':
                                    result += 4
                                # I 1
                                elif s[i] == 'I':
                                    result +=1              
                            elif s[i] == 'I':
                                result +=1              
    return result
s = "MCMXCIV"
print(romanToInt(s))
# Completed