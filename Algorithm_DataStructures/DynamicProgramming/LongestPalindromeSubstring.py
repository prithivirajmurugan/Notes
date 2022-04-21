class Solution:
    def expand(self,s,low,high):
        """
        Utility function to provide the longest palindrome from mid-point
        """
        length = len(s)
        while low>=0 and high<length and s[low]==s[high]:
            low = low - 1
            high = high +1
        return s[low+1:high]
            
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        max_str = ""
        max_length = 0
        """
        Each element is considered as midpoint and is expanding for that to find the possible palindrome sequence
        """
        for i in range(length):
            # for odd value only one midpoint needed
            curr_str = self.expand(s,i,i)
            curr_length = len(curr_str)
            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str
            # for even value two mid point needed
            curr_str = self.expand(s,i,i+1)
            curr_length = len(curr_str)
            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str
        return max_str
            