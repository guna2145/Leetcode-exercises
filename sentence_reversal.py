
def sentence_reversal(sentence):
    reversed = []
    for word in sentence.split():
       reversed.insert(0,word)
    return reversed

sentence = "A number specifying in which position to insert the value"
#print(sentence.split())
print(sentence_reversal(sentence))