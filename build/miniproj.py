
import os
import time as t
import webbrowser
import subprocess

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
    return_txt = subprocess.check_output("git config --global user.mail",shell=True,universal_newlines=True)
    return return_txt
def gituser():
    ret_txt = subprocess.check_output("git config --global user.name",shell=True,universal_newlines=True)
    return ret_txt
        # os.system('git config --global user.name')
def getcmtmsg(msg):
    os.system(f'git commit -m \"{msg}\"')
def gitsetuname(uname):
    os.system('git config --global user.name'+uname)
def gitsetmail(mailid):
    os.system('git config --global user.mail'+mailid)
def status():
    os.system(f'git status')
def initial():
    os.system("git init")
def filechange():
    f = open("Readme.md","+a")
    t = f.read()
    gmu ="GitMeUp"
    if gmu in t:
        pass
    else:
        f.write("<p align =\"center\">Commit made with :heart: by <a href=\"https://github.com/Aditya-Lawate-codez/gitRobo\">GitMeUp</a>\</p>")
def callback(url):
       webbrowser.open_new_tab(url)
def gitrmtadd(link):
    if ".git" in link:
        os.system(f"git remote add origin {link}")
        return "Git link added"
    else:
        return ".git not in link"