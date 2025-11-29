import pywhatkit as kit
import pyautogui
import time

kit.sendwhatmsg_instantly("+919053318341", "Hello! Auto message") # pyright: ignore[reportPrivateImportUsage]

time.sleep(5)   # WhatsApp load hone ka time
pyautogui.press("enter")   # SEND button auto press
