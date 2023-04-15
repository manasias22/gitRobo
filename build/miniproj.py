
import os

# defining function

def remote_link():
    pass
def Init():
    os.system("git init")
def gitadd():
    os.system('git add .')
def gitpush():
    try:
        os.system('git push -u origin main')
    except:
        os.system("git push")
def gitusmail():
    print('your mail id is: ')
    os.system('git config --global user.mail')
def gitusname():
    print('your username is: ')
    os.system('git config --global user.name')
def getcmtmsg():
    msg = input("Enter a commit msg:")
    os.system(f'git commit -m \"{msg}\"')
def gituser():
    uname = input("Enter your github username: ")
    os.system(f'git config --global user.name \"{uname}\"')
def gitmail():
    mailid = input("Enter mail id associated to your github acc: ")
    os.system(f'git config --global user.mail \"{mailid}\"')
def status():
    os.system(f'git status')
def chd():
    d = input("Enter the absolute path:")
    try:
        os.chdir(d)
    except (FileNotFoundError):
        os.mkdir(d)
        os.chdir(d)
    os.system("git init")
def gitrmtadd():
    link = input("Enter git link")
    if ".git" in link:
        os.system(f"git remote add origin {link}")
    else:
        print("incorrect link")