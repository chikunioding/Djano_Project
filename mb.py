
w = ["why", "whenw", "what", "whewre", "while"]
a =[]
for i in w:
    count = 0
    for j in i:
        if j == "w":
            count += 1
            if count == 2:
                a.append(i)
                break
print(a)