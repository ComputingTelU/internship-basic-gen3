class BigRandom:
    def __init__(self):
        self.data = "data.txt"

    def answer(self):
        noh = 0 
        suc = 0 
        text = open(self.data,"r")
        jmlhline=0

        for x in text : #mengakses per line
            jmlhline +=1
            t=0
            tmp=0
            for y in x: #mengakses per kata
                t+=1
                for z in y: #mengaskes per huruf
                    if (t == 1 and z != "#"):
                        tmp += ord(z)
                    if (z=="#"):
                        noh +=1
                    else :
                        suc += ord(z)
            suc -=tmp
               
        text.close()
        noh -= jmlhline
        return (noh,suc)

b= BigRandom()
print (b.answer())
