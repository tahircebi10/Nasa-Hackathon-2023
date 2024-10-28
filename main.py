import cv2
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment

# data
cap = cv2.VideoCapture('data/nasa-video-data.mp4')

# video check
if not cap.isOpened():
    print("Could not open video. Please check the file path.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
audio_data = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale and calculate brightness
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray_frame)

    # Adjust frequency based on brightness
    frequency = 200 + (brightness / 255) * 800
    duration = 1 / fps
    t = np.linspace(0, duration, int(duration * 44100), False)
    note_signal = np.sin(2 * np.pi * frequency * t)
    
    # Append audio data
    audio_data.append(note_signal)

cap.release()

# Concatenate audio data and normalize
audio_data = np.concatenate(audio_data)
audio_data = np.int16(audio_data / np.max(np.abs(audio_data)) * 32767)

# Save as WAV format
write('output/generated_audio.wav', 44100, audio_data)

# Convert WAV to MP3 format
audio = AudioSegment.from_wav('output/generated_audio.wav')
audio.export('output/generated_audio.mp3', format='mp3')

print("Audio file successfully created: output/generated_audio.mp3")