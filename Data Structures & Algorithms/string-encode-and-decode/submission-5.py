class Solution:

    def encode(self, strs: List[str]) -> str:
         if not strs:
            return 'empty'
            
         return chr(31).join(strs)


    def decode(self, s: str) -> List[str]:
        if s == 'empty':
            return []

        return s.split(chr(31))
