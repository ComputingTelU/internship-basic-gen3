class BigRandom:
    def __init__(self):
    	self.data = "data.txt"

    def answer(self):
        self.data = open("data.txt", "r")
        noh, suc = 0, 0
        for line in self.data.readlines(): 
            noh = noh + len([x for x in line if x == '#']) #______ count of '#'
            suc = suc + sum([ord(x) for x in line]) #_____________ sum of asciis of all chars

           
        numbs = ''.join([str(x) for x in range(10000)])	# 1234567891011121314...999910000

        self.data.close() # close data stream

        # ord('#') * 10000 _________________ sum of asciis of first '#' in each row
        # sum([ord(x) for x in nomor]) _____ sum of asciis of numbs
        return (noh - 10000, suc - (ord('#') * 10000 + sum([ord(x) for x in numbs])))

# instantiation
big = BigRandom()
a, b = big.answer()
print(a, b)