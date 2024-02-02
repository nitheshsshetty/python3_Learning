from cryptography.fernet import Fernet

'''def write_key():
     key = Fernet.generate_key()
     with open("key.key","wb") as key_file:
          key_file.write(key)
'''

def load_key():
      file = open("key.key","rb")
      key=file.read()
      file.close()
      return key


#master_pw = input("Please enter the master password")
##write_key()
key = load_key() 
fer = Fernet(key)


def add():
    name = input("Account name :").lower()
    pw = input("Password")

    with open("Password.txt","a") as f:
              f.write(name + "|" + fer.encrypt(pw.encode()).decode() + "\n")
   

def view():
     with open("Password.txt","r") as f:
          for line in f.readlines():
               data = line.rstrip()#to eliminate the carriage return 
               name,pws=data.split("|")
               print(f"User :{name} \n Pw :{fer.decrypt(pws.encode()).decode()}") 
         
        
while True:

    mode = input("Do you want to view or add new password (add,view) or q to quit ! ==>")
    #write_key()
    if mode == "add":
        add()
        
    if mode == "view":
        view()
        
    if mode == "q":
        print("you choose to quit ")
        break
