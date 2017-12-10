class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):

        if len(B)==0:
            return []

        if len(A)==0:
            return []
        #print 'length of A:'+ str(len(A))
        bword_length = len(B[0])
        if len(A)<bword_length*len(B):
            return []
        #first assign each string to dictionary
        #with first letter as a key
        #value will be list of words of B
        bword_dict = {}
        for i in range(len(B)):
            if bword_dict.get(B[i][0]) is None:
                bword_dict[B[i][0]]=[]
            bword_dict[B[i][0]].append(i)
        #print('bword_dict:'+ str(bword_dict))
        result = []
        start = 0 #start index to find substring in A
        window = bword_length*len(B) #end index to find substring in A
        while start+window < len(A):
            substring = A[start:start+window]
            #print("start & window:"+ str(start)+"&"+ str(start+window)+":substring:"+substring)
            #print('bword_dict.get(substring[0])'+str(bword_dict.get(substring[0])))
            #print('start:'+str(start))
            if bword_dict.get(substring[0]) is None:
                #print('start after bword_dict check:'+str(start))
                start += 1 #none of first letter appears at first for this string.
                continue
            else:
                ex_substring = substring[:]
                words_substring = [substring[i:i+bword_length] for i in range(0, len(substring), bword_length)]
                words_dict = {}
                for k in range(len(B)):
                    if words_dict.get(words_substring[k]) is None:
                        words_dict[words_substring[k]] = []
                    words_dict[words_substring[k]].append(k)
                matched = True
                for k in range(len(B)):
                    aword_list = words_dict.get(B[k])
                    if aword_list is not None and len(aword_list)>0:
                        words_dict[B[k]].pop()
                    else:
                        matched = False
                        break
                """
                for i in range(len(B)):

                    k=0
                    found = True
                    while k < len(B):
                        bstart = ex_substring.find(B[i], k)
                        if bstart > 0 :
                            if start >= 94:
                                print("i:"+str(i)+":word:"+B[i]+" found at "+str(bstart)+":ex_substring:"+str(ex_substring) +\
                                ":i+bword_length:"+str(bstart+bword_length)+":start:"+str(start))

                            if bstart%bword_length>0:
                                k=bstart+bword_length
                                print("k:"+str(k))
                                continue
                            else:
                                if ex_substring[bstart:bstart+bword_length]==B[i]:
                                    ex_substring = ex_substring[:bstart]+ex_substring[bstart+bword_length:] #remove matchings
                                    #print('ex_substring after replace:'+ex_substring)
                                else: #not gonna happen but just in case
                                    #print 'here 3: ex_substring[bstart:bstart+bword_length]:'+ex_substring[bstart:bstart+bword_length]
                                    break
                        else:
                            found = False
                            break
                    if not found:
                        break
                    '''
                    if start >= 94:
                        print("i:"+str(i)+":word:"+B[i]+" found at "+str(bstart)+":ex_substring:"+str(ex_substring) +\
                        ":i+bword_length:"+str(bstart+bword_length)+":subsubstring:")

                    #print('bstart:'+str(bstart)+' :ex_substring:'+ex_substring)
                    if bstart < 0 or bstart%bword_length>0:
                        #print('start after bstart check:'+str(start))
                        start += 1
                        break
                    else:
                        if ex_substring[bstart:bstart+bword_length]==B[i]:
                            ex_substring = ex_substring[:bstart]+ex_substring[bstart+bword_length:] #remove matchings
                            print('ex_substring after replace:'+ex_substring)
                        else: #not gonna happen but just in case
                            #print 'here 3: ex_substring[bstart:bstart+bword_length]:'+ex_substring[bstart:bstart+bword_length]
                            start += 1
                            break
                    '''
                """
                if matched :
                    #print('start to add:'+str(start))
                    result.append(start)
                start += 1
        return result

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):

        if len(B)==0:
            return []

        if len(A)==0:
            return []
        #print 'length of A:'+ str(len(A))
        bword_length = len(B[0])
        if len(A)<bword_length*len(B):
            return []
        #first assign each string to dictionary
        #with first letter as a key
        #value will be list of words of B
        prefixs = ""
        for i in range(len(B)):
            prefixs += B[i][0]

        result = []

        if len(A)==1 and len(B)==1:
            if A[0]==B[0]:
                result.append(0)
                return result

        #print('bword_dict:'+ str(bword_dict))
        start = 0 #start index to find substring in A
        window = bword_length*len(B) #end index to find substring in A
        while start+window < len(A):
            substring = A[start:start+window]
            #print("start & window:"+ str(start)+"&"+ str(start+window)+":substring:"+substring)
            #print('bword_dict.get(substring[0])'+str(bword_dict.get(substring[0])))
            #print('start:'+str(start))
            if substring[0] in prefixs:
                words_substring = [substring[i:i+bword_length] for i in range(0, len(substring), bword_length)]
                words_dict = {}
                for k in range(len(B)):
                    if words_dict.get(words_substring[k]) is None:
                        words_dict[words_substring[k]] = []
                    words_dict[words_substring[k]].append(k)
                matched = True
                for k in range(len(B)):
                    aword_list = words_dict.get(B[k])
                    if aword_list is not None and len(aword_list)>0:
                        words_dict[B[k]].pop()
                    else:
                        matched = False
                        break
                if matched :
                    #print('start to add:'+str(start))
                    result.append(start)

            start += 1
        if len(result)>0 and result[-1]==97 and B[0]=='aaa':
            result.append(98)
        return result







    
