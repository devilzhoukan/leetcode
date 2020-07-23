## 953. Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 
```
Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, 
then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], 
hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, 
and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", 
because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
```


```Java
class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        int[] index = new int[26];
        for (int i = 0; i < order.length(); ++i) {
            index[order.charAt(i) - 'a'] = i;
        }
        
        for (int i = 0; i < words.length - 1; ++i) {
            String word1 = words[i];
            String word2 = words[i + 1];
            // System.out.print("Math.min(word1.length(), word2.length(): ");
            // System.out.println(Math.min(word1.length(), word2.length()));
            
            for (int k = 0; k < Math.min(word1.length(), word2.length()); ++k) {
                // System.out.print("k = ");
                // System.out.println(k);
                if (word1.charAt(k) != word2.charAt(k)) {
                    // System.out.println(index[word1.charAt(k) - 'a']);
                    // System.out.println(index[word2.charAt(k) - 'a']);
                    if (index[word1.charAt(k) - 'a'] > index[word2.charAt(k) - 'a']) {
                    return false;
                    }
                    
                    break;

                }
                if ((k == Math.min(word1.length(), word2.length() - 1) && word1.length() > word2.length())) {
                        return false;
                    }
            }
        }
        return true;
    }
}
```
