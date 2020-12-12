import pyaudio
import json
from watson_developer_cloud import SpeechToTextV1

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

data_feed = b''.join(frames)

speech_to_text = SpeechToTextV1(
    username='secret',
    password='secret too',
    x_watson_learning_opt_out=False
)

result = speech_to_text.recognize(data_feed,
                                  content_type="audio/l16;rate=44100;channels=2",
                                  word_confidence=True,
                                  max_alternatives=4,
                                  word_alternatives_threshold=0.5,
                                  model="en-US_BroadbandModel",
                                  continuous=True)

j = json.dumps(result, indent=2)
print(j)