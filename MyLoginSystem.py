def signUp():
  username=input("New Username :")
  password=input("New Password :")
  passwordAgain=input("New Password Again :")
  
  if password==passwordAgain:
    print("Opening the file to write...")
    try:
      file=open("users.txt","a")
      file.write(username+"\n")
      file.write(password+"\n\n")
      print("Success.")
    finally:
      file.close()
  else print("Passwords doesn't match")

def getPassword(username):
  try:
    file=open("users.txt","r")
    check=False
    username=username.rstrip()
    line=file.readline()
    while line:
      line=line.rstrip()
      if check==True:
        if line!="":
          return(line)
        if username==line:
          check==True
        line=file.readline()
      return("Couldn't find %s"%(username))
  except:
    return("Couldn't find the file:users.txt")
  finally:
    file.close()
    
def login():
  username=input("Username :")
  realPassword=getPassword(username)
  password=input("Password :")
  if realPassword.rstrip()==password.rstrip():
    printf("Yikes")
  else:
    print("You fucling failed you disgrace")
  
def main():
  login()
  
main()  
  
