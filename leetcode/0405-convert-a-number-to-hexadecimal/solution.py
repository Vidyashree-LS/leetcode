class Solution:
    def toHex(self, num: int) -> str:
        

        if num == 0:
            return "0"

        num &= 0xffffffff

        hex_chars = "0123456789abcdef"
        ans = ""

        while num:
            ans = hex_chars[num & 15] + ans
            num >>= 4

        return ans
        
