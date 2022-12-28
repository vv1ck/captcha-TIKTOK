class TikTok_encryption:
	def __init__(self):
		self.Lists = []
		self.Starts_encryption()
	
	def decode(self,msg):
		try:
			for J in range(0,len(msg),2):
				set = 5 ^ ord(bytes.fromhex(msg[J:J+2]).decode());self.Lists.append(chr(set))
			return "".join(self.Lists)
		except ValueError:print('[!] Sorry, the message you entered is not encrypted or not affiliated with TikTok , Try again\n====\n');return self.Starts_encryption()
			
	def Information_encryption(self,key=5):
		JN=input('[?] Choose: \n\t-1- Encrypting login_information( username,password)\n\t-2- Encrypt a message\n=== : ')
		if (JN=='1'):
			
			#Username encryption
			username = input('Enter username: ')
			username= ''.join([hex(int(x ^ key))[2:] for x in username.encode('utf-8')])
			
			# Password encryption
			password = input('Enter password: ')
			password = ''.join([hex(int(x ^ key))[2:] for x in password.encode('utf-8')])
			
			print ('\n [%] done successfully:\n-----\nusername:'+username+' Password:'+password+'\n-----')
		elif (JN=='2'):
			#to encrypt messages
			MSG=''.join([hex(int(x ^ key))[2:] for x in input('[?] Enter the message to encrypt it: ').encode('utf-8')]);print('\n [%] done successfully\n---'+MSG+'---')
	
	def Starts_encryption(self):
		QTR=input('1- Information encryption \n2- decryption \n[+] Choose :')
		if (QTR=='1'):self.Information_encryption()
		elif (QTR=='2'):print(self.decode(input('=====\n[$] Enter the message to decrypt : ')))
TikTok_encryption()
