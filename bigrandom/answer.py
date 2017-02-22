class BigRandom:
    def __init__(self):
        self.data = "data.txt"
        # add attributes if you need more

    def answer(self):
        noh = 0 # variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag

        # your algorithm
        txt = open(self.data, "r")
        for each in txt:
            line = each
            i=0
            while(line[0]!="#"):
                line = line[1:]
            line = line[1:]
            for x in line:
                if(x=="#"):
                    noh+=1
                suc+=ord(x)

        return (noh,suc)

    # add methods if you need more

big = BigRandom()
print (big.answer())