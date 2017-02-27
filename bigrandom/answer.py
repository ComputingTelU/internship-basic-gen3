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
        data = open(self.data, "r")
        for line in data:
            i = 0
            while(line[0] != "#"):
                line = line[1:]
                i += 1
            line = line [1:]
            for y in line:
                if(y == "#"):
                    noh += 1
                suc += ord(y)
        data.close()
        return (noh,suc)

    # add methods if you need more

brd = BigRandom()
noh, suc = brd.answer()

print("Sum of Hastag :", noh)
print("Sum of ASCII  :", suc)