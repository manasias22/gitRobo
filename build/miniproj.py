
import os, time

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
    time.sleep(1)
    os.system('git config --global user.mail')
def gituser():
    print('your username is: ')
    time.sleep(1)
    os.system('git config --global user.name')
def getcmtmsg(msg):
    os.system(f'git commit -m \"{msg}\"')
def gitsetuname(uname):
    os.system(f'git config --global user.name \"{uname}\"')
def gitsetmail(mailid):
    os.system(f'git config --global user.mail \"{mailid}\"')
def status():
    os.system(f'git status')
def chd():
    os.system("git init")
def filechange():
    f = open("Readme.md","+a")
    t = f.read()
    msgstr ="\ncommit made with :heart: by GitMeUp"
    if msgstr in t:
        pass
    else:
        f.write(msgstr)
def gitrmtadd(link):
    if ".git" in link:
        os.system(f"git remote add origin {link}")
    else:
        print("incorrect link")