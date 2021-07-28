import pywhatkit
import pyautogui
import webbrowser
import time
import datetime

def timewhat():
    x = datetime.datetime.now()
    current_hr= x.strftime("%H")
    current_min = x.strftime("%M")

    # print(current_hr,current_min)
    current_hr = int(current_hr)*60
    total_min = int(current_hr) + int(current_min)
    # print(total_min)

    send_hr=int(input("Enter the hours at which message to be sent:"))
    send_min=int(input("Enter the minutes at which message to be sent:"))

    send_hr = send_hr*60
    total_send_min = send_hr + send_min
    # print(total_send_min)

    left_min = total_send_min - total_min
    # print(left_min)

    left_secs = left_min*60
    # print(left_secs)
    print(f"Your message will be sent in {left_min} minutes")
    return left_secs

def use(timewhat,person_name,message):
    time.sleep(timewhat)
    webbrowser.open('https://web.whatsapp.com/')
    time.sleep(10)
    
    #click on search bar
    pyautogui.click(275,186)
    pyautogui.typewrite(f"{person_name}")

    time.sleep(5)

    #click on person
    pyautogui.click(204,313)
    time.sleep(3)

    #click on chat
    pyautogui.click(719,692)

    time.sleep(5)
    #type chat
    pyautogui.typewrite(f"{message}")

    #msg send click
    time.sleep(5)
    pyautogui.click(1329,691)

x = int(input("Enter 1 for sending msg to phone no.:\n2 for sending to saved contact:\n3 for sending to a group:"))
if x==1:
    person_no=int(input("Enter the phone no.:"))
    person_no = str(person_no)
    message = input("Enter the message to be sent: ")
    y=int(input("Enter hours:"))
    z=int(input("Enter minutes:"))
    pywhatkit.sendwhatmsg(f"+91 {person_no}",message,y,z)


elif x==2:
    person_name = input("Enter the name of the person to send the msg'(case sensitive):")
    message = input("Enter the message to be sent: ")
    use(timewhat(),person_name,message)



if x==3:
    grp = input("Enter the group name(case sensitive):")
    message = input("Enter the message to be sent: ")
    webbrowser.open('https://web.whatsapp.com/')

    time.sleep(10)

    # click on search bar
    pyautogui.click(346,188)
    pyautogui.typewrite(f"{grp}")

    time.sleep(5)

    #click on person

    pyautogui.click(172,318)
    time.sleep(3)

    #click on chat

    pyautogui.click(719,692)
    time.sleep(5)

    #type chat
    pyautogui.typewrite(f"{message}")

    #msg send click
    time.sleep(5)
    pyautogui.click(1329,691)



