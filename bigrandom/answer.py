def answer():
    noh = 0 # variable to store number of hashtag
            # ommiting line number's hashtag
    suc = 0 # variable to store sum of character's code in ascii,
            # ommiting line number and its hashtag
    data = open('data.txt', 'r')
    l = data.readline()
    # your algorithm
    for line in data:
        for ch in line:
            suc += ord(ch)
            if ch == '#':
                noh += 1
        noh -= 1

    data.close()
    return (noh,suc)

noh, suc = answer()

print('NOH: ' + str(noh))
print('SUC: ' + str(suc))
