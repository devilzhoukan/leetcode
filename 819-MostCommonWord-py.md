## 819. Most Common Word

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.


It's an easy problem, anyway.

```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banset = set(banned)
        
        # paragraph = re.sub(r'[^\w\s]',' ',paragraph)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, ' ')
        counter = collections.Counter(paragraph.lower().split())
        
        ans = None
        highest = 0
        for word in counter:
            if counter[word] > highest and word not in banset:
                ans = word
                highest = counter[word]
                
        return ans
```
