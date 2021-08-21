import config
import pyautogui
import time

def sign_in(subject):
    meetingid = config.id[subject][0]
    pswd = config.id[subject][1]

    time.sleep(3)
    
    # Clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('Assets/join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # Type the meeting ID
    time.sleep(3)
    pyautogui.write(meetingid)

    # Disables both the camera and the mic
    media_btn = pyautogui.locateAllOnScreen('Assets/media_btn.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()

    # Hits the join button
    join_btn = pyautogui.locateCenterOnScreen('Assets/join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    
    time.sleep(5)
    # Types the password and hits enter
    pyautogui.write(pswd)
    pyautogui.press('enter')
