import enchant
import glob

def checkEnc(text_file):
	dic = enchant.Dict("en_US")
	lineNum = 1
	wordCount = 1
	enc = False
	for line in text_file:
		words = line.split()
		for word in words:
			suggestions = dic.suggest(word)
			if not suggestions:
				print("the word starting in line " + str(lineNum) + " and column " + str(wordCount) + " may be encrypted\n")
				enc = True
			wordCount = wordCount + 1
		wordCount = 1
		lineNum = lineNum + 1
	if not enc:
		print("the file is not encrypted")


def main():
	text_file_list = glob.glob('./*.txt')
	for f in text_file_list:
		text_file = open(f , "r")
		print("checking for file " + str(f) + "\n")
		checkEnc(text_file)



if __name__ == "__main__":
	main()
