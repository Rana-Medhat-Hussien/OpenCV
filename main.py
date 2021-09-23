import keyboard
import numpy as np
import cv2

while True:
    if keyboard.read_key() == "p":
        print("You pressed p")
        path = r'C:\Users\DELL\r.png'
        # Reading an image in default mode
        img = cv2.imread(path)
        # Showing the output
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break

    if keyboard.is_pressed("o"):
        print("You pressed o")
        path = r'C:\Users\DELL\Orange.PNG'
        frame = cv2.imread(path)
        ## convert to hsv
        ORANGE_MIN = np.array([5, 50, 50], np.uint8)
        ORANGE_MAX = np.array([15, 255, 255], np.uint8)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, ORANGE_MIN, ORANGE_MAX)
        ##################################3333
        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('result', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if keyboard.is_pressed("g"):
        print("You pressed g")
        path = r'C:\Users\DELL\green.PNG'
        frame = cv2.imread(path)
        ## convert to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        ## mask of green (36,25,25) ~ (86, 255,255)
        # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
        mask = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))
        ##################################3333
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('result', result)

        cv2.waitKey(0)

        cv2.destroyAllWindows()


    if keyboard.is_pressed("b"):
        print("You pressed b")
        path = r'C:\Users\DELL\blueRed.PNGb'
        # Reading an image in default mode
        frame = cv2.imread(path)
        # _, frame = cap.read()
        # It converts the BGR color space of image to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Threshold of blue in HSV space
        lower_blue = np.array([60, 35, 140])
        upper_blue = np.array([180, 255, 255])

        # preparing the mask to overlay
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # The black region in the mask has the value of 0,
        # so when multiplied with original image removes all non-blue regions
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('result', result)

        cv2.waitKey(0)

        cv2.destroyAllWindows()



    if keyboard.is_pressed("r"):
        print("You pressed r")
        path = r'C:\Users\DELL\red.png'
        # Reading an image in default mode
        frame = cv2.imread(path)
        # _, frame = cap.read()
        # It converts the BGR color space of irmage to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Threshold of blue in HSV space
        lower_red = np.array([155, 25, 0])
        upper_red = np.array([179, 255, 255])

        # preparing the mask to overlay
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # The black region in the mask has the value of 0,
        # so when multiplied with original image removes all non-blue regions
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('result', result)

        cv2.waitKey(0)

        cv2.destroyAllWindows()

    if keyboard.is_pressed("esc"):
        print("You pressed esc")
        break




keyboard.on_press_key("r", lambda _: print("You pressed r"))



