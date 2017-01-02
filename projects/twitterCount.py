s = raw_input("Enter your text: ")

longestWord = max(s.split(), key=len)

k = list(s)

count = len(k)

wordsOver = []

over = count - 140

def numLen(s, n):
    for x in s.split():
        if len(x) >= 7:
            wordsOver.append(x)
    return len(wordsOver)

val = numLen(s, 7)

if count > 140:
    print ("Sorry, that is more than 140 characters.")
    print ("You had a total of " + str(count) + " characters.")
    print ("That's " + str(over) + " over the max allowed.")
    print ("You're longest word was, \"" + longestWord + "\"")
    print ("There are " + str(val) + " words over 7 characters.")
    print ("They were:")
    print (wordsOver)
    print ("You may want to consider changing them for shorter words.")
else:
    print ("That's short enough!")
