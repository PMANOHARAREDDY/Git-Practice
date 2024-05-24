class Solution(object):
    def intToRoman(self, num):
        l1=['I','II','III','IV','V','VI','VII','VIII','IX']
        l2=['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        l3=['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        l4=['M','MM','MMM']
        target=list(str(num))
        Roman=""
        for j in range(1,len(target)+1):
            if len(target)==1:
                for i in range(1,10):
                    if int(target[0])==i:
                        Roman+=l1[i-1]
            elif len(target)==2:
                for i in range(1,10):
                    if int(target[0])==i:
                        Roman+=l2[i-1]
                        target.pop(0)
                        break
                    if int(target[0])==0:
                        target.pop(0)
                        break
            elif len(target)==3:
                for i in range(1,10):
                    if int(target[0])==i:
                        Roman+=l3[i-1]
                        target.pop(0)
                        break
                    if int(target[0])==0:
                        target.pop(0)
                        break
            elif len(target)==4:
                for i in range(1,10):
                    if int(target[0])==i:
                        Roman+=l4[i-1]
                        target.pop(0)
                        break
        return Roman
        

    

        
