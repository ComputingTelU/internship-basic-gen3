class BigRandom:
    def __init__(self):
        self.data = "data.txt"
        # add attributes if you need more

    def answer(self):
        noh = 0 # variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag
<<<<<<< HEAD
        data = open('data.txt','r')
        # your algorithm
        line = ""
        for char in data:

            for x in range(0,len(char)):
                if (char[x]=='#'):
                    line = char[x+1:]
                    break
                x+=1
            for y in line:
                if (y=='#'):
                    noh+=1
                suc+=ord(y)

            # i=0
            # while (line[0]!="#"):

        # for char in data.readline():
        #     if (char=='#'):
        #         noh+=1
        #     else:
        #         suc= suc+ ord(char)
        #
        # noh = noh-10000
        # suc = suc-orc(10000)
        return (noh,suc)

    # add methods if you need more
big = BigRandom()
print (big.answer())
=======

        # your algorithm

        return (noh,suc)

    # add methods if you need more
>>>>>>> 64e1f92e25e7147b206ac73695e846881e7f9b0d
