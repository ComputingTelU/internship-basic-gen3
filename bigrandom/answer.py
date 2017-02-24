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
        data = open ("data.txt", "r")
        for char in data :
            while (char[0] != "#") :
                char = char[1:]
            char = char[1:]
            for i in char :
                if (i == "#") :
                    noh+=1
                suc = suc + ord(char)
        data.close()
        return (noh,suc)

    # add methods if you need more
data = BigRandom()
print(data.answer())