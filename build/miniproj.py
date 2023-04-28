
import os
import time as t
import webbrowser


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
    t.sleep(1)
    os.system('git config --global user.mail')
def gituser():
    print('your username is: ')
    t.sleep(1)
    os.system('git config --global user.name')
def getcmtmsg(msg):
    os.system(f'git commit -m \"{msg}\"')
def gitsetuname(uname):
    os.system(f'git config --global user.name \"{uname}\"')
def gitsetmail(mailid):
    os.system(f'git config --global user.mail \"{mailid}\"')
def status():
    os.system(f'git status')
def initial():
    os.system("git init")
def filechange():
    f = open("Readme.md","+a")
    t = f.read()
    msgstr ="\ncommit made with :heart: by GitMeUp"
    if msgstr in t:
        pass
    else:
        f.write("<p align =\"center\">"+msgstr+"</p>")
def callback(url):
       webbrowser.open_new_tab(url)
def gitrmtadd(link):
    if ".git" in link:
        os.system(f"git remote add origin {link}")
        return "Git link added"
    else:
        return ".git not in link"