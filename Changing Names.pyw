#-------------------------------------------------------------------------------
# Name:        this screws with the google bing lady
# Purpose:
#
# Author:      layonthehorn
#
# Created:     09/03/2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# before use you must change the $user to the users name
import shutil, re, os, random


hiddenfold = 'C:\\filestomove'
desktoppath = 'C:\\Users\\$user\\Desktop'



filelistdesk = os.listdir(desktoppath)
filelistinstore = os.listdir(hiddenfold)

numberfiles = len(filelistinstore)
randomfile = random.randrange(0,numberfiles-1)
#print(randomfile)

filetomovedesk = filelistinstore[randomfile]
#print(filetomovedesk)



for file in filelistdesk:
    if re.search('googlebing',file):
        filetomove = os.path.join(desktoppath,file)
        shutil.move(filetomove,hiddenfold)


replacementfile = os.path.join(hiddenfold,filetomovedesk)
shutil.move(replacementfile, desktoppath)

