def encrypt(plain_text,key1,key2,cipher_text):
    #enumerate allows to keep track ofno of iteration in a loop
   for index,char in enumerate(plain_text):
       #isalpha() boolean function returns true or false
       if char.isalpha():
           shift = key1 if index % 2 == 0 else key2
           #ord() returns the number representing unicode code of character
           base = ord('A') if char.isupper() else ord('a')
           if char== " ":
               cipher_text+=" "    
           else:
               cipher_text+=chr((ord(char)+shift-base)%26+base)
       else:
           cipher_text+=char
   return cipher_text

#function for decryption using 2 keys
def decrypt(plain_text,key1,key2,cipher_text):
   for index,char in enumerate(cipher_text):
       if char.isalpha():
           shift = key1 if index % 2 == 0 else key2
           base = ord('A') if char.isupper() else ord('a')
           if char== " ":
               plain_text+=" "    
           else:
               plain_text+=chr((ord(char)+shift-base)%26-base)
       else:
            cipher_text+=char
   return plain_text

#enter the string you want to encrypt
plain_text=input("enter string:")
#keys are the integers
key1=int(input("enter key1:"))
key2=int(input("enter key2:"))
cipher_text=" "

e=encrypt(plain_text,key1,key2,cipher_text)
print("cipher_text(encrypted):",e)
d=decrypt(plain_text,key1,key2,cipher_text)
print("cipher_text(decrypt):",d)