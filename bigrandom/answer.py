from math import floor, log10

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
            dex  = 2 if i < 10 else floor(log10(i)) + 2
            line = line[dex:]

            # An alternative using List Comprehension
            """noh += sum(1 for x in line if x == "#")
            suc += sum(ord(x) for x in line)"""
            #real	0m1.098s
            #user	0m1.083s
            #sys	0m0.003s

            # Better use this one
            for x in line:
                if x == "#": noh += 1
                suc += ord(x)
            #real	0m0.998s
            #user	0m0.993s
            #sys	0m0.003s

            i   += 1

        data.close()
        return (noh,suc)

    # add methods if you need more


br       = BigRandom()
noh, suc = br.answer()

print("Sum of Hashtag   : " + str(noh))
print("Sum of all ASCII : " + str(suc))
