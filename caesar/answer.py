class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        key = 0 # variable to store the key

        # your algorithm
        data = open(self.ciphertext, "r")
        line = data.read()

        for key in range(128):
            words = ''.join(chr(ord(x) + key) for x in line)

            if "Tugas" in words: break
        #real	0m0.044s
        #user	0m0.040s
        #sys	0m0.000s

        return (key)

    # add methods if you need more
    def bruteForce(self):
        data = open(self.ciphertext, "r")
        line = data.read()

        res  = open("result.txt", "w")

        for i in range(128):
            res.write("[Key: " + str(i) + "]\n")

            words = ''.join(chr(ord(x) + i) for x in line)

            res.write(words + "\n\n")

        data.close()
        res.close()

caesar = Caesar()
#caesar.bruteForce() # Run this if you need it

result = caesar.answer()

print("Key that contain \"Tugas\": " + str(result))
