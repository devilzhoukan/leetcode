def longestPalindrome(s):
    result = s[0]
    for i in range(len(s)):
        # consider s[i] as center
        # even situation
        for j in range(0, i + 1):
            # print('i, j=', i, j)
            if i+j+1>len(s)-1:
                break
            if s[i-j] == s[i+j+1]:
                temp = s[i-j:i+j+2]
                if len(temp) > len(result):
                    result = temp
            else:
                break

        # odd situation
        for j in range(0, i):    
            if i-j-1<0 or i+j+1>len(s)-1:
                break
            # print('i, j=', i, j)            
            if s[i-j-1] == s[i+j+1]:
                temp = s[i-j-1: i+j+2]
                if len(temp) > len(result):
                    result = temp
            else:
                break
            

    return result

if __name__ == "__main__":
    r = longestPalindrome('abcdcecd')
    print(r)

