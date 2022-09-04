import os
from cryptography.fernet import Fernet
path ="C:\\ransomTest\\"
list_of_files = []
key=Fernet.generate_key()

# drives=win32api.GetLogicalDriveStrings()
# drives=drives.split('\000')[:-1]
# for dri in drives:
#     path=dri
#     for root, dirs, files in os.walk(path):
# 	  for file in files:
# 		list_of_files.append(os.path.join(root,file))
#     for file in list_of_files:
#           os.path.isfile(file)
#           if file == 'encrypter.py' or file=='secretkey.key':
#              continue
#           with open("secretkey.key","rb") as key:
#             seckey=key.read()
#           with open(file,"rb") as thefile:
#                  contents=thefile.read()
#                  contents_decry=Fernet(seckey).decrypt(contents)
#           with open(file,"wb") as thefile:
#                 thefile.write(contents_decry)
#           print(f"Successfully decrypted {file}")

for root, dirs, files in os.walk(path):
	for file in files:
		list_of_files.append(os.path.join(root,file))
for file in list_of_files:
          os.path.isfile(file)
          if file == 'encrypter.py' or file=='secretkey.key':
             continue
          with open("secretkey.key","rb") as key:
            seckey=key.read()
          with open(file,"rb") as thefile:
                 contents=thefile.read()
                 contents_decry=Fernet(seckey).decrypt(contents)
          with open(file,"wb") as thefile:
                thefile.write(contents_decry)
          print(f"Successfully decrypted {file}")
