import hashlib
import pyaudio
import cv2
import numpy as np
import random
import os
import wave
import time
import pywifi



def capturar_ruido():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  

    iface.scan()
    time.sleep(2)  

    # Obtenha as redes Wi-Fi próximas
    scan_results = iface.scan_results()

    if not scan_results:
        print("Nenhuma rede Wi-Fi encontrada.")
        return None

   
    rede_aleatoria = random.choice(scan_results)
    noise = rede_aleatoria.signal
    return noise


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

for i in range(10):
    audio_data = stream.read(44100)
    _, frame = cap.read()
    timestamp = int(time.time())
    random_integer = random.randint(min_range, max_range)
    random_integer_bytes = random_integer.to_bytes(64, byteorder='big', signed=False)

    # Capturar o ruído da antena Wi-Fi
    wifi_noise = capturar_ruido()

    # Usar o ruído da antena Wi-Fi como parte dos dados
    if wifi_noise is not None:
        wifi_noise = wifi_noise & 0xFFFF  # Garanta que o valor seja positivo e caiba em 2 bytes
        combined_data = (
                audio_data + frame.tobytes() + os.urandom(1024) +
                timestamp.to_bytes(8, byteorder='big', signed=False) +
                random_integer_bytes +
                wifi_noise.to_bytes(2, byteorder='big', signed=False)
        )
    else:
        # Em caso de falha na captura do ruído, continue sem incluí-lo
        combined_data = (
                audio_data + frame.tobytes() + os.urandom(1024) +
                timestamp.to_bytes(8, byteorder='big', signed=False) +
                random_integer_bytes
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
    cv2.waitKey(100)

stream.stop_stream()
stream.close()
audio.terminate()
cap.release()
cv2.destroyAllWindows()
