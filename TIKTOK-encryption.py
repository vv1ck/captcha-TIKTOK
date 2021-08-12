def login():
  global user , pess
  print('username: '+user+' Password: '+pess)



def Information_encryption(key=5):
  global user , pess
  
  user = input('Enter username: ')
  #Username encryption
  user = ''.join([hex(int(x ^ key))[2:] for x in user.encode('utf-8')])
  
  pess = input('Enter password: ')
  # Password encryption
  pess = ''.join([hex(int(x ^ key))[2:] for x in pess.encode('utf-8')])
  
  login() # Login function
Information_encryption()
