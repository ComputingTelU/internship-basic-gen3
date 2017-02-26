class BigRandom:
    def __init__(self):
        self.data = "data.txt"
<<<<<<< HEAD


    def answer(self):
        noh = 0 
        suc = 0 
        a = open("data.txt","r")
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
=======
        # add attributes if you need more

    def answer(self):
        noh = 0 # variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag

        # your algorithm

        return (noh,suc)

    # add methods if you need more
>>>>>>> 64e1f92e25e7147b206ac73695e846881e7f9b0d
