def main():
    fin = input("Input name of file to add to dictionary: ")
    fhandle = open(fin,"r", encoding='utf-8')
    PUNC = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
    words = []
    for line in fhandle:
        line.strip()
        wordsinline = line.split()
        for word in wordsinline:
            word = word.lower()
            for char in word:
                if char in PUNC:
                    word = word.replace(char, "")
            if word not in words:
                words.append(word)
    fhandle.close()
    fhandle = open("dictionary.txt", 'a')
    for word in words:
        fhandle.write(word + "\n")
    print(str(len(words)) + " words added to dictionary")
if __name__ == "__main__":
    main()
