class Solution(object):  
    def romanToInt(self, s):  
        """  
        :type s: str  
        """  
        o = 0   
        for i in range(len(s)):  
            v = s[i]  
            if v == "I":  
                if i+1 < len(s):  
                    if s[i+1] == "V":  
                        o = o + 4  
                        i = i + 1  
                    elif s[i+1] == "X":  
                        o = o + 9  
                        i = i + 1  
                    else:  
                        o = o + 1   
                else:  
                    o = o + 1   
 
            if v == "V":  
                o = o + 5   
 
            if v == "X":  
                if i+1 < len(s):  
                    if s[i+1] == "L":  
                        o = o + 40   
                        i = i + 1  
                    elif s[i+1] == "C":  
                        o = o + 90   
                        i = i + 1  
                    else:  
                        o = o + 10   
                else:  
                    o = o + 10   
                     
            if v == "L":  
                o = o + 50   
 
            if v == "C":  
                if i+1 < len(s):  
                    if s[i+1] == "D":  
                        o = o + 400   
                        i = i + 1  
                    elif s[i+1] == "M":  
                        o = o + 900   
                        i = i + 1 
                    else:  
                        o = o + 100   
                else:  
                    o = o + 100   
 
            if v == "D":  
                o = o + 500   
 
            if v == "M":  
                o = o + 1000   
 
        return o   
    
print("give me a number...")
s = input()
solution = Solution()
print(solution.romanToInt(s))