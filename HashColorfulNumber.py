class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        number_dict = {}
        t = A
        decimal = 10
        i = 0
        while t > 0:
            r = t%10
            t = int(t/10)
            number_dict[i]=r
            i += 1

        #create a list from hash
        num = []
        n_i = 0
        for i in range(i-1,-1,-1):
            num.append(number_dict[i])
        product_dict={}
        #length increment
        for i in range(1,len(num)+1):
            for j in range(0,len(num)):
                if i == 1:
                    if product_dict.get(num[j]):
                        return 0
                    else:
                        product_dict[num[j]] = 1
                    continue
                if j+i > len(num):
                    continue
                product = 1
                #iterate for the subsequence
                for k in range(j, j+i,1):
                    if k < len(num):
                        product *= num[k]
                if product_dict.get(product):
                    return 0
                else:
                    product_dict[product] = 1

        return 1    
