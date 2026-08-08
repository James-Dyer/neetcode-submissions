class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string))
            output += '#'
            output += string
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        n = len(s)
        i = 0
        length = ""
        while i < n:
            if s[i] == '#':
                word_len = int(length)
                output.append(s[i + 1 : i + 1 + word_len])
                i = i + 1 + word_len
                length = ""
            else:
                length += s[i]
                i += 1
        return output
