class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a hashmap to count up number of each letter in each str
        # if they're == then true, otherwise false
        
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}
        for l in s:
            s_map[l] = s_map.get(l, 0) + 1
        for r in t:
            t_map[r] = t_map.get(r, 0) + 1
        
        return s_map == t_map


        