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
         my_file = open ("ok.txt", "r")
        for a in my_file:
            for b in a:
                pagar = 0
                for c in b:
                    if (c=="#"):
                        noh = noh+1
                    else:
                        suc += ord(c)
        my_file.close()
        return (noh-10000,suc)
    
ok = BigRandom()
print(ok.answer())
    

    # add methods if you need more
