class BigRandom:
    def __init__(self):
        self.data = open("data.txt","r")
        # add attributes if you need more

    def answer(self):
        noh = 0 # variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag

        # your algorithm

        for x in b.data:
            for i in x:
                x = x[1:]
                if (i == "#"):
                    break
            for i in x:
                if ( i == "#"):
                    noh += 1
                suc += ord(i)
        return (noh, suc)

b = BigRandom()

print (b.answer())




    # add methods if you need more