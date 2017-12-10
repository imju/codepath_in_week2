class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        char_dict = {}
        if len(A)==0:
            return 0
        if len(A)==1:
            return 1
        start = end = 0
        max_len = 0
        #print len(A)
        for i in range(len(A)):#starting index
            end = i
            prev_idx = char_dict.get(str.lower(A[i]))
            if prev_idx>=0 or prev_idx>start:#dup found

                 max_len = max(end-start, max_len)
                 start = prev_idx + 1
                 #print('max_len:'+str(max_len))
                 '''
                 if i > 1660:
                 print 'i at '+str(i) + ' start at '+str(start)+':char:'+A[start]+':end:'+ str(end)+\
                 ' end char:'+A[i] + ' chart_dict[str.lower(A[i])]:'+ str(char_dict[str.lower(A[i])])
                 '''
            char_dict[str.lower(A[i])]=i

        print('start:'+str(start)+':end:'+str(end)+':max_len:'+str(max_len))

        return max_len

        int getLongestStr(String a) {
          int result = 0;
          HashMap<Character, Integer> charLocMap = new HashMap<Character, Integer>();

          int start = 0;
          int i = 0;

          while (i < a.length()) {
            char ch = a.charAt(i);
            if (charLocMap.containsKey(ch)) {
              int charLoc = charLocMap.get(ch);
              if (charLoc >= start) {
                // found duplicate
                int len = i - start;
                result = Math.max(len, result);
                start = charLoc+1;
              }
            }
            charLocMap.put(ch, i);
            i++;
          }
          return Math.max(result, i-start);
        }        
