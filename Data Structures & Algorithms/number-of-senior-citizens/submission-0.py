class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for person in details:
            if int(person[11:13]) > 60:
                res += 1

        return res