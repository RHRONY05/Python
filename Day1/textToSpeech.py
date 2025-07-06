import pyttsx4

engine = pyttsx4.init()

# Set properties
rate = engine.getProperty('rate')
print(f"Current rate: {rate}")
engine.setProperty('rate', 125)

volume = engine.getProperty('volume')
print(f"Current volume: {volume}")
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Queue up speech
engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))

# Save speech to file
engine.save_to_file('Hello Shafayet, Fuck You', r'D:\Python\Day1\test2.wav')
engine.runAndWait()

engine.stop()
