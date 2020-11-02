import pyautogui
import time
import os

def onClick(filename):
    Click_button = pyautogui.locateCenterOnScreen(filename)
    pyautogui.moveTo(Click_button)
    pyautogui.click()

def onType(filename, field):
    meeting_id_btn = pyautogui.locateCenterOnScreen(filename)
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(field)

def sign_in(meetingID, passCode):
    print("Opening Zoom.")
    
    time.sleep(3)

    print(f"Meeting id: {meetingID}")
    print(f"Password: {passCode}")

    time.sleep(1)
    
    os.chdir("C:\\Users\\my pc\\AppData\\Roaming\\Zoom\\bin")
    os.startfile("Zoom.exe")
    os.chdir("C:\\Users\\my pc\\Desktop\\MeetFox")
    
    time.sleep(10)
    
    onClick('join_button.png')
    
    time.sleep(5)
    
    onType('meeting_id_button.png', meetingID)
    onClick('disconnect_audio.png')
    onClick('join_meet.png')

    time.sleep(5)
    onType('meeting_password_button.png', passCode)
    onClick('start_meet.png')

os.system('title MeetFox')
os.system('color fc')
sign_in("347 539 8797", "mlzs")
