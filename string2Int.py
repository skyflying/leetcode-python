class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        #NULL
        if not s :
            return 0
        #only space
        s = s.strip()
        if not s :
            return 0
        number, flag = 0,1
         
        #'+'or'-''
        if s[0]=='-':
            s= s[1:]
            flag=-1
        elif s[0]=='+':
            s=s[1:]
        
        for c in s:
            if c>='0' and c<='9':
                number =10*number + ord(c) -ord('0')
            else:
                break

        number = flag * number
        
        if number >INT_MAX:
            return INT_MAX
        if number <INT_MIN:
            return INT_MIN
        return number
