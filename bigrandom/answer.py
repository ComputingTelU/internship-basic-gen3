class BigRandom:
    def __init__(self):
        self.data = "data.txt"
        # add attributes if you need more

    def answer(self):
        noh = 0  # variable to store number of hashtag
        # ommiting line number's hashtag
        suc = 0  # variable to store sum of character's code in ascii,
        # ommiting line number and its hashtag

        # your algorithm

        f = open(self.data, "r")
        for baris in f:
            ind=0
            for i in range(len(baris)):
                if baris[i]=="#":
                    ind=i+1
                    break
            for j in range(ind,len(baris)):
                if baris[j]=="#":
                    noh+=1
                suc+= ord(baris[j])
        return (noh,suc)

    # add methods if you need more
x= BigRandom()
print(x.answer())