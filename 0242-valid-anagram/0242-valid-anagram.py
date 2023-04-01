class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_hash = {}
        t_hash = {}
        
        for i in s:
            if i in s_hash.keys():
                s_hash[i] += 1
            else:
                s_hash[i] = 1

        for i in t:
            if i in t_hash.keys():
                t_hash[i] += 1
            else:
                t_hash[i] = 1
                
        if s_hash == t_hash:
            return True
        else:
            return False
