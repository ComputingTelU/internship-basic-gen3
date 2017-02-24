class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        key = 0 # variable to store the key

        # your algorithm
        my_file = open (self.ciphertext,"r");
        key = 46								#coba-coba
        tmp = ""								#penampung dari tiap huruf nanti
        for x in my_file.read():				#akes perhuruf
        	index = 0							#penampung tiap karakter itu ascii berapa
        	index = ord(x)-key					#mis decode 5 maka A = 1+5 = 6 => F, biar balik lagi kurang dengan key
        	if (index<0):						#Z misal 26 + 5 maka balik ke 5, biar ke 26 lagi dikurang key ditambah keseluruhan
        		index += 127
        	tmp += chr(index)					#tiap karakter ditampung di sini
        print (tmp)
        print ("\nEnkrip yang digunakan: ", key)
        return (key)
        my_file.close()
hasil = Caesar()
hasil.answer()
        

    # add methods if you need more
