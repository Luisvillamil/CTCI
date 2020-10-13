# 1.6 String Compression
# Similar problem in Leetcode: https://leetcode.com/problems/string-compression

class Solution:
    def compress(self, chars: List[str]) -> int:
        l = chars[0]
        count = 1
        del chars[0]
        end = len(chars)
        size = 0
        while(size < end):
            size+=1
            if l != chars[0]:
                chars.append(l)
                if count >= 2:
                    for x in str(count):
                        chars.append(x)
                l = chars[0]
                count = 1
            else:
                count+=1
            del chars[0]
        chars.append(l)
        if count >= 2:
            for x in str(count):
                chars.append(x)
        return len(chars)
