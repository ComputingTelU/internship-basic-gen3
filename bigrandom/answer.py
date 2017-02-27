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
        d = open(self.data, "r")
        for c in d:
            for x in c:
                c = c[1:]
                if (x == "#"):
                    break
            for x in c:
                if (x == "#"):
                    noh += 1
                suc += ord(x)
        return (noh,suc)


d = BigRandom()
print (d.answer())

    # add methods if you need more