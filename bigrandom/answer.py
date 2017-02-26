class BigRandom:
    def __init__(self):
        self.data = 'data.txt'
        # add attributes if you need more

    def answer(self):
        noh = 0  # variable to store number of hashtag
        # ommiting line number's hashtag
        suc = 0  # variable to store sum of character's code in ascii,
        # ommiting line number and its hashtag
        # your algorithm

        kondisi = False
        x = open('data.txt', 'r')
        for i in range(10000):
            j = x.readline()    #52411
            noh += j.count("#")
        x.close()
        kondisi1 = False
        x = open('data.txt', 'r')
        for i in range(10000):
            J = x.readline()
            for item in J:
                if(kondisi1 == True):
                    suc += ord(item)
                if(item == "#"):
                    kondisi1 = True
        x.close()
        noh -= 10000 #karena ada 10000 penunjuk baris
        print noh  
        print suc
        return (noh, suc)

bigrandom = BigRandom()
bigrandom.answer()
