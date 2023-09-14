# This program was conceived and crafted by Víctor Duarte Melo on 14/09/2023 - Brazil. If you intend to use or modify it, please provide proper credits. 
# Building the structure and coding this project wasn't an easy task; it involved countless hours of testing and an entire night of planning. Please use it responsibly.
#Contact: victormeloasm@gmail.com



import hashlib
import pyaudio
import cv2
import numpy as np
import random
import os
import wave
import time

while True:
    try:
        min_range = int(input("Enter the minimum value for random integers (0 or greater): "))
        if min_range < 0:
            raise ValueError("Minimum range must be 0 or greater")
        break
    except ValueError:
        print("Invalid input. Please enter a valid minimum range.")

while True:
    try:
        max_range = int(input("Enter the maximum value for random integers (up to 512-bit integer): "))
        if max_range < 0:
            raise ValueError("Maximum range must be greater than or equal to 0")
        break
    except ValueError as e:
        print(e)

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=44100)
cap = cv2.VideoCapture(0)
cv2.namedWindow("Webcam")
cv2.namedWindow("Highlighted Image")

random_bytes = os.urandom(1024)

for i in range(10):
    audio_data = stream.read(44100)
    _, frame = cap.read()
    timestamp = int(time.time())
    random_integer = random.randint(min_range, max_range)
    random_integer_bytes = random_integer.to_bytes(64, byteorder='big', signed=False)
    combined_data = (
            audio_data + frame.tobytes() + random_bytes +
            timestamp.to_bytes(8, byteorder='big', signed=False) + random_integer_bytes
    )
    sha512 = hashlib.sha512()
    sha512.update(combined_data)
    hash_bytes = sha512.digest()
    hash_integer = int.from_bytes(hash_bytes, byteorder="big")
    result_integer = min_range + (hash_integer % (max_range - min_range + 1))
    print("Calculated Integer within Range:", result_integer)

    frame_copy = frame.copy()
    cv2.putText(frame_copy, f"Value: {result_integer}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.setWindowProperty("Highlighted Image", cv2.WND_PROP_TOPMOST, 1)
    cv2.imshow("Highlighted Image", frame_copy)
    cv2.waitKey(1000)

stream.stop_stream()
stream.close()
audio.terminate()
cap.release()
cv2.destroyAllWindows()
