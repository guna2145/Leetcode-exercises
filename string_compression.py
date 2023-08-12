text = "AABBCCCDDEEFFFGGHH"
compressed = ""
count = 1

for i in range(len(text)-1):
    print("Current Text:",text[i])
    print("Next Text:",text[i+1])
    if text[i] == text[i+1]:
        count =+ 1
        print(count)
    else:
        print(text[i],count)
        compressed = compressed + text[i] + str(count)
        count = 1

compressed = compressed + text[-1] + str(count)
print(compressed)