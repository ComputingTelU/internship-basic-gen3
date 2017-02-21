import math

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
        i    = 0

        for line in data:
            if i < 10:
                dex = 2
            else:
                dex = math.floor(math.log10(i)) + 2

            line = line[dex:]
            noh += sum(1 for x in line if x == '#')
            suc += sum(ord(x) for x in line)

            i   += 1

        data.close()
        return (noh,suc)

    # add methods if you need more


br       = BigRandom()
noh, suc = br.answer()

print("Sum of Hashtag   : " + str(noh))
print("Sum of all ASCII : " + str(suc))
