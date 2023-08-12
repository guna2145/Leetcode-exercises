def anagram_with_set(s1,s2):
    return set(s1.replace(" ","")) == set(s2.replace(" ",""))

def anagram_manual_method(str1,str2):
    miscount = 0

    s1 = str1.lower()
    s2 = str2.lower()

    for x in s1:
        if x in s2.lower().replace(" ",""):
            miscount += 1

    for y in s2:
        if y in s1.lower().replace(" ",""):
            miscount -= 1
    
    if miscount:
        return False
    else:
        return True
    
str1 = "Saoirse Ronan"
str2 = "rare as onionS"
print(anagram_manual_method(str1,str2))