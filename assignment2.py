import sys
import crypt


def crackPass(usr, pw):
	en_type = usr.split("$")[1]
	segment = usr.split("$")[2]
	salt = "$" + en_type + "$" + segment + "$"


	with open("/usr/share/dict/american-english", "r") as eng_dict:
		for line in eng_dict:
			word = word.stip("\n")
			if (crypt.crypt(word, salt) ==  pw):
				print "Password found for user:\t " + usr + " and password is:\t" + word +"\n"
				sys.exit(0)
			else: 
				print "No password found"
				exit 
				
def main():

	
	try:
		for line in open(sys.argv[2], "r") readlines():
			line = line.replace("\n","").split(":")
			if  not line[1] in ['*','!']:	
				usr = line[0]
				pw = line[1]
				crackPass(usr, pw)
					
	except IOError:
		print ("File not found: "sys.argv[2])
		exit(1)
	
			


				 

if __name__ == "__main__":
	main()