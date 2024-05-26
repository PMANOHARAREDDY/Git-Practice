#Solution as per the leetcode constraints(OOP Paradigm and Functions Paradigms)
class Solution:
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        target = min(strs, key=len)
        for i in range(len(target)):
            char = target[i]
            if all(s[i] == char for s in strs):
                continue
            else:
                return target[:i]
        return target

#Procedural Paradigm
import sys
strs=eval(input("Enter the list of items: "))
if not strs:
    print("")
    sys.exit()
target = min(strs, key=len)
for i in range(len(target)):
    char=target[i]
    if all(s[i]==char for s in strs):
        continue
    else:
        print(target[:i])
        sys.exit()
print(target)
sys.exit()
