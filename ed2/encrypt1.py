# The same function is used to encrypt and 
# decrypt 
def encryptDecrypt(inpString): 
  
    # Define XOR key 
    # Any character value will work 
	xorKey = 'P'; 
  
    # calculate length of input string 
	length = len(inpString); 
  
    # perform XOR operation of key 
    # with every caracter in string 
	for i in range(length): 
		print("inpString ", inpString[:i])
		inpString = (inpString[:i] + 
			chr(ord(inpString[i]) ^ ord(xorKey)) +
				inpString[i + 1:]); 
		print(inpString[i], end = ""); 
      
	return inpString; 

def main():
	sampleString = "GritGeeksforGeeks"; 
  
    # Encrypt the string 
	print("Encrypted String: ", end = ""); 
	sampleString = encryptDecrypt(sampleString); 
	print("\n"); 
  
    # Decrypt the string 
	print("Decrypted String: ", end = ""); 
	encryptDecrypt(sampleString); 
  
# This code is contributed by Princi Singh 
if __name__ == '__main__': 
	main()
    
