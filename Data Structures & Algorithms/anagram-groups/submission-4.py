class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		# create anagram hash 
		# hash -> [words]
		hashes = defaultdict(list)
		for word in strs:
			freq = [0]*26
			for char in word:
				freq[ord(char)-ord('a')] += 1
			
			my_hash = tuple(freq)
			hashes[my_hash].append(word)

		res = []
		for words in hashes.values():
			res.append([word for word in words])
		return res