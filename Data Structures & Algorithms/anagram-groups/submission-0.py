class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort
        # add to set, make new group
        # check for existance
        # append to group

        my_dict = dict()
        group_strs = []

        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in my_dict:
                group_strs[my_dict[sorted_str]].append(string)
            else:
                my_dict[sorted_str] = len(group_strs)
                group_strs.append([string])

        return group_strs