#!/usr/bin/python
import os, getpass, os.path
from random import randint

file_path = "/usr/local/bin/terminal-notifier"

if not os.path.exists(file_path):
    print "Terminal-Notifier not installed."
    if getpass.getuser() == "root":
        os.system("gem install terminal-notifier")
    else:
        print "Must be ran as root to install terminal-notifier."
    exit(0)

x = randint(0, 3)

y = randint(1, 3)

phrases = ['I\'m Sorry','I forgive you','I love you','Thank you']

os.system('terminal-notifier -message "%s" -title "Ho\'oponopono" -appIcon ./bunny%s.png' % (phrases[x],y))
