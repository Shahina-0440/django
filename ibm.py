s1="qiix gz clro".split()
s2="one orange ball".split()
s2.reverse()

s="abcdefghijklmnopqrstuvwxyz"
res=""

for i in range(len(s1)):
        if len(s2[i])%2==0:
            for k in range(len(s1[i])):
                ind=s.index(s1[i][k])
                res+=s[ind-len(s2[i])]

            res+=" "
        else:
            for l in range(len(s1[i])):
                ind=s.index(s1[i][l])
                res+=s[ind+len(s2[i])]
            res+=" "
print(res)

            
                   
