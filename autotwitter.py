import mouse,random,time,sys,os,pyautogui,keyboard

i = 0

#You will need to be logged in already to use this script


sendable_messages = ["Enter Your Messages Here",
]



def tweet_post():
    fullmessage = random.choice(sendable_messages)
    time.sleep(random.uniform(2, 4))
    pyautogui.moveTo(420,825)
    time.sleep(random.uniform(2, 4))
    pyautogui.click()
    time.sleep(random.uniform(2, 4))
    keyboard.press_and_release('ctrl+a')  # Select all text
    time.sleep(0.5)
    keyboard.press_and_release('backspace')  # Delete selected text
    time.sleep(random.uniform(2, 4))
    tweet_content = (
        f"{fullmessage}\n\n"
    )
    keyboard.write(tweet_content)  
    time.sleep(random.uniform(2, 4))
    pyautogui.moveTo(1190,709)
    time.sleep(random.uniform(2, 4))
    #pyautogui.click(x=1268, y=851)
    time.sleep(1)
    #pyautogui.click(x=1268, y=851)
    #pyautogui.click(x=1268, y=851)
    #pyautogui.click(x=1268, y=851)
    time.sleep(1)
   # pyautogui.click(x=1268, y=709)
    time.sleep(1)
    pyautogui.click(x=1268, y=605)
    pyautogui.click(x=1268, y=605)
    time.sleep(1)
    #pyautogui.click(x=1268, y=533)
    time.sleep(1)
    #pyautogui.click(x=1268, y=368)
    time.sleep(1)
    time.sleep(random.uniform(10, 3000))
    tweet_post()

while True:
    tweet_post()
    print(mouse.get_position())

#Post Button
#420,875
#Post Tweet Button
#1190,368