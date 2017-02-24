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
        data= open (self.data,"r")
        for line in data:
        	for b in(line):
        		if (b!="#"):
        			line = line[1:]
        		else:
        			break
        	for d in (line[1:]):
        		if (d=="#"):
        			noh+=1
        		suc+=ord(d)
        return (noh,suc)
a=BigRandom()
noh, suc=a.answer()
print("suc: ", suc)
print("noh: ", noh)
