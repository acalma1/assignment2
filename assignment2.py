import sys
import crypt



def crackPass(usr, pw):
	#Parses through the password and determines the type of encryption hash
	#the salt and password
	en_type = usr.split("$")[1] 
	salt = usr.split("$")[2] 
	insalt = "$" + en_type + "$" + segment + "$"

	#Iterates through a simple english dictionary then uses the crypt function 
	#to encrypt every word, and if it finds a match then it displays the password
	#and if none are found, then it displays "No password found"
	with open("/usr/share/dict/american-english", "r") as eng_dict:
		for line in eng_dict.readlines():
			word = word.strip("\n")
			if (crypt.crypt(word, salt) ==  pw):
				print "Password found for user:\t " + usr + " and password is:\t" + word +"\n"
				sys.exit(0)
			else: 
				print "No password found"
				exit 			

def main():

	try:
		with open(sys.argv[2], "r") as f: #This allows the user to enter the username and filepath of the shadow file
			for line in f.readlines():	
				line = line.replace("\n","").split(":")
				if  not line[1] in ['*','!']:	
					usr = line[0] #the username is stored here
					pw = line[1]  #the user's unencrypted password 
					crackPass(usr, pw)

	#If the file isn't found, the user is thrown a file not found message and exits			
	except IOError:
		print ("File not found: " + sys.argv[2])
		exit(1)

if __name__ == "__main__":

	main()
