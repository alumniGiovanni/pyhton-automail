import pyautogui as pag
import pyperclip
import time

pag.PAUSE = 1

pag.press("win")
pag.write("chrome")
pag.press("enter")


pag.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pag.hotkey("ctrl", "v")
pag.press("enter")
time.sleep(5)

pag.press("c")

pag.write("giovanni.andrade9991@gmail.com")
pag.press("tab")
pag.press("tab")
pag.write("Email 1")
pag.press("tab")
pag.write("Email de teste")
pag.press("tab")
pag.press("enter")




#print(pag.size())
#print(pag.position())