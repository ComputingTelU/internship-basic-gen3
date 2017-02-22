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
            words = ""
            for x in line:
                x = ord(x) - key
                if x < 0: x += 127
                words += chr(x)

            if "Tugas" in words: break
        #real	0m0.046s
        #user	0m0.040s
        #sys	0m0.003s

        return (key)

    # add methods if you need more
    def displayText(self, key):
        data = open(self.ciphertext, "r")
        line = data.read()

        words = ""
        for x in line:
            x = ord(x) - key
            if x < 0: x += 127
            words += chr(x)

        print(words)

        data.close()

    # Analysis purpose only
    def bruteForce(self):
        data = open(self.ciphertext, "r")
        line = data.read()

        res  = open("result.txt", "w")

        for i in range(128):
            res.write("[Key: " + str(i) + "]\n")

            words = ""
            for x in line:
                x = ord(x) - i
                if x < 0: x += 127
                words += chr(x)

            res.write(words + "\n\n")

        data.close()
        res.close()

caesar = Caesar()
#caesar.bruteForce() # Run this if you need it

result = caesar.answer()

print("Key that contain \"Tugas\": " + str(result) + "\n")
print(caesar.displayText(result))
