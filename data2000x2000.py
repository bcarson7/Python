dataFile = open("silvas.txt", "w")
for i in range(1, 2001):
    for j in range(1, 2001):
        dataFile.write(str(i) + "," + "%s\n" % j)
dataFile.close()
