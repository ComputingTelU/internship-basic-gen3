class BigRandom:
    def __init__(self):
        self.data = open("data.txt","r")

    def answer(self):
        noh = 0 # variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag

        # your algorithm
        for line in big.data:
            for c in line:
                c = c[1:]
                if (c == "#"):
                    break
            for c in line:
                suc += ord(c)
                if c == '#':
                    noh += 1
            noh -= 1
        return (noh,suc)

big = BigRandom()
print (big.answer())
