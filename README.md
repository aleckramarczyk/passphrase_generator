# passphrase_generator
This repository includes two tools. One will take a text file and add all unique words to a dictionary. This can then be used to generate secure passphrases from

To use:
Use python3 to run generatedictionary.py. Input a text file. Output will be saved to dictionary.txt in the same directory. Can be run on multiple files to create a larger dictionary.

Next, run generatepassphrase.py. Input the file your dictionary is saved to. This will generate a passphrase and estimate cracking times with a worst case scenario.

For best results:
Use a large, unique, and private dictionary
Adding further permutations on the generated passphrase to increase security
The idea is to get a very secure, yet memorable passphrase that can be used to secure things like password managers, which have even better yet less memorable password generators built in. This tool is not a replacement for a good password manager.

Issues and plans:
generatedictionary.py does not compare words that it collects to existing dictionary. This will cause repeat words if run on multiple input files. This will result in an overestimatation of dictionary size and cracking times.
I plan to fix this by switching to an SQL database in the future.
