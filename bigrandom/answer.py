class BigRandom:
    def __init__(self):
        self.data = "data.txt"

    def answer(self):
        noh = 0 
        suc = 0 
        a = open(self.data,"r")
        s=0
        for x in a :
            s+=1
            t=0
            tmp=0
            for y in x:
                t+=1
                for z in y:
                    if (t == 1 and z != "#"):
                        tmp += ord(z)
                    if (z=="#"):
                        noh +=1
                    else :
                        suc += ord(z)
                if (t==1):
                    suc-=tmp
        a.close()
        noh -= s
        return (noh,suc)

b= BigRandom()
print (b.answer())
