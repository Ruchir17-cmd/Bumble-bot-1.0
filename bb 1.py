import speech_recognition as sr
import pyttsx3
import pyautogui as py


import time


def bumble():
    def switch():
        py.keyDown("alt")
        py.press("tab")
        py.keyUp("alt")

    def swipe():
        py.press("down")
        time.sleep(2)
        py.press("down")
        time.sleep(2)
        py.press("right")
        time.sleep(1)
        py.press("down")

        time.sleep(1)

        py.press("down")
        time.sleep(1)

        time.sleep(2)
        py.press("left")
        time.sleep(1)
        py.press("down")
        time.sleep(1)

        py.press("down")
        time.sleep(1)

        time.sleep(2)
        py.press("left")
        time.sleep(1)
        py.press("down")
        time.sleep(1)

        py.press("down")
        time.sleep(1)

        time.sleep(2)
        py.press("right")
        time.sleep(1)
        py.press("down")
        time.sleep(1)

        py.press("down")
        time.sleep(1)

        time.sleep(2)
        py.press("left")
        time.sleep(1)
        py.press("down")
        time.sleep(1)

        py.press("down")
        time.sleep(1)

        time.sleep(2)

    def xit():
        py.keyDown("ctrl")
        py.press("w")
        py.keyUp("ctrl")

    switch()
    py.keyDown("ctrl")
    py.press("t")
    py.keyUp("ctrl")
    py.typewrite("b")
    py.press("enter")
    time.sleep(10)
    swipe()
    xit()


r = sr.Recognizer()


def st(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while 1:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)

            text = r.recognize_google(audio2)
            text = text.lower()

            print(text)

            if text == "bumble":
                st("opening bumble")
                bumble()
            else:
                st(text)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error")



