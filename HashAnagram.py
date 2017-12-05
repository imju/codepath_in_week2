class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        #create a dict for each word in the list
        char_list = []
        #create a list of list to hold anagrams to each other
        anag_list = []
        k=1
        for a in A:
            char_dict = {}
            #print('length of a:'+str(len(a)))
            for i in range(len(a)):
                if char_dict.get(a[i]):
                    char_dict[a[i]] += 1
                else:
                    char_dict[a[i]] = 1
            '''
            if k==3 or k==10 or k==11:
                print('k:'+str(k)+' :'+str(char_dict))
            '''
            k+=1

            char_list.append(char_dict)
        #initialize anag_dict
        for i in range(len(A)):
            anag_list.append([])
            anag_list[i].append(i+1)

        #comparing ith and jth words
        #if the lenth is same and they match then it's anagram

        for i in range(len(A)):
            #print(' at i='+str(i)+'A[i]:'+A[i])
            for j in range(i+1,len(A)):
                #print('i:'+str(i)+'j:'+str(j)+':anag_list:'+str(anag_list[j])+' :A: '+str(len(A)))
                if anag_list[j] is None:
                    continue
                if len(A[i]) != len(A[j]):
                    continue
                s_dict = char_list[i]#source
                t_dict = char_list[j]#target
                matching = True
                for key, val in s_dict.items():
                    '''
                    if i==2 and j==9:
                        print('i:'+str(i)+'j:'+str(j)+'key:'+key+' :val:'+str(val)+\
                        ':s_dict[key]:'+str(s_dict[key])+':t_dict[key]:'+str(t_dict[key]))
                    '''
                    if t_dict.get(key):
                        if s_dict[key] != t_dict[key]:
                            matching = False
                            break
                    else:
                        matching = False
                        break
                if matching:
                    #print('matching A[i]:'+A[i]+'anag_list[i]:'+str(anag_list[i]) + ':A[j]:'+A[j]+':j:'+str(j))
                    if anag_list[i] and len(anag_list[j])>0:
                        anag_list[i]=anag_list[i]+anag_list[j]
                        anag_list[j]=None
                else:
                    pass

        anags = list(filter (lambda x:x!=None, anag_list))
        return anags
