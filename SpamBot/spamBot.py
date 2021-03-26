import pyautogui, time 

# 5 seconds to find target
time.sleep(5)

#file containing Shrek Movie Script 
f = open("shrek.txt", 'r')

#for loop to message each line from the file
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
