class BigRandom(object):
    def __init__(self):
        self.data = "data.txt"
        # add attributes if you need more

    def answer(self):
        noh = 0 # variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag

        # your algorithm
        total = 0 
        file = open("data.txt","r")
        for i in file:
            for j in i:
                if ( j != '#'):
                    i = i[1: ]
                else :
                    break
            for j in i[1:] :
                if (j=='#'):
                    noh+=1
                suc+=ord(j)
        return(noh,suc)
        
            
            

jawab = BigRandom()
print (jawab.answer())
#return (noh,suc)

    # add methods if you need more
