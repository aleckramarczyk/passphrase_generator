import random
class password_generator:
    global crack_time
    def crack_time(strength, hashtype):
        cracktime = ""
        divide = 0
        MD5GUESS = 180000000000
        SHA1GUESS = 63000000000
        SHA512GUESS = 364000
        BCRYPTGUESS = 71000
        DAY = 86400
        YEAR = 31536000
        if hashtype == "MD5":
            if strength/MD5GUESS < DAY:
                cracktime = "less than a day"
            elif strength/MD5GUESS < YEAR:
                divide = round(strength/MD5GUESS, 2)
                cracktime = str(divide/DAY) + " days"
            else:
                divide = round(strength/MD5GUESS, 2)
                cracktime = str(divide/YEAR) + " years"
        elif hashtype == "SHA1":
            if strength/SHA1GUESS < DAY:
                cracktime = "less than a day"
            elif strength/SHA1GUESS < YEAR:
                divide = strength/SHA1GUESS
                cracktime = str(divide/DAY) + " days"
            else:
                divide = strength/SHA1GUESS
                cracktime = str(divide/YEAR) + " years"
        elif hashtype == "SHA512":
            if strength/SHA512GUESS < DAY:
                cracktime = "less than a day"
            elif strength/SHA512GUESS < YEAR:
                divide = strength/SHA512GUESS
                cracktime = str(divide/DAY) + " days"
            else:
                divide = strength/SHA512GUESS
                cracktime = str(divide/YEAR) + " years"
        elif hashtype == "BCRYPT":
            if strength/BCRYPTGUESS < DAY:
                cracktime = "less than a day"
            elif strength/BCRYPTGUESS < YEAR:
                divide = strength/BCRYPTGUESS
                cracktime = str(divide/DAY) + " days"
            else:
                divide = strength/BCRYPTGUESS
                cracktime = str(divide/YEAR) + " years"
        return cracktime
    def main():
        fin = input("Input name of file to use a dictionary: ")
        fhandle = open(fin,"r", encoding='utf8')
        words = []
        for line in fhandle:
            line = line.rstrip()
            if line != "":
                words.append(line)
        number_of_words = int(input("How many words do you want to include in your passphrase? "))
        dict_length = len(words)
        print("The length of your dictionary is: " + str(dict_length))
        count = 0
        symbol_list = ['!', '(', ')', '{', '}', '[', ']', ';', ':', '"', ',', '<', '>', '.', '/', '?', '@', '#', '$', '%', '^', '&', '*', '_', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        passphrase = "" 
        symbol = symbol_list[random.randrange(0, len(symbol_list))]
        while count < number_of_words :
            rand_number = random.randrange(0, dict_length)
            if passphrase == "" :
                passphrase = passphrase + words[rand_number]
            else:
                passphrase = passphrase + symbol + words[rand_number]
            count += 1
        strength = (dict_length ** number_of_words) * len(symbol_list)
        print("\nYour passphrase is: \n" + passphrase)
        print("\nAssuming an attacker has your dictionary, hash, and a supercomputer, these are your estimated crack times:")
        print("MD5: " + crack_time(strength, "MD5"))
        print("SHA1: " + crack_time(strength, "SHA1"))
        print("SHA512: " + crack_time(strength, "SHA512"))
        print("Bcrypt: " + crack_time(strength, "BCRYPT"))

    if __name__ == "__main__":
        main()
