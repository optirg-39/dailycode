Given a string S, check if it is palindrome or not.

class Solution:
	def isPlaindrome(self, S):
	    r = len(S)//2
	    for i in range(r):
	        if S[i] != S[-i]:return 0
	    return 1
    
