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
        file = open("data.txt","r")
        for baris in file:
            for char in baris:
                baris=baris[1:]
                if ( char == '#'):
                    break
            for char in baris[1:]:
                if (char=='#'):
                    noh+=1
                suc+=ord(char)
        return (noh,suc)

    # add methods if you need more
acak = BigRandom()
print (acak.answer())
