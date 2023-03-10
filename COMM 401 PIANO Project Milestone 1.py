import numpy as np # importing the numpy library
import matplotlib.pyplot as plt # importing the matplotlib.pyplot library
import sounddevice as sd # importing the sounddevice library
t = np.linspace(0 , 3 , 12 * 1024) # setting the time t of the signal
Fi = np.array([164.81, 164.81, 164.81, 174.61, 174.61, 164.81, 146.83, 146.83, 130.81, 130.81, 246.93, 246.93, 130.81, 164.81, 164.81, 146.83, 146.83, 130.81, 246.93, 164.81]) # the frequency of the 3rd octave (Left Hand)
fi = np.array([261.63, 261.63, 392, 392, 440, 440, 392, 349.23, 349.23, 329.63, 329.63, 293.66, 293.66, 261.63, 392, 392, 349.23, 349.23, 329.63, 329.63]) # the frequency of the 4th octave (Right Hand)
ti = 0 # setting the initial time to zero
Ti = np.array([0.2, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2]) # this is how long each note will last
signal = 0 # initializing the signal to zero
for i in range (0, 20): # number of pairs is 20 N = 20 pairs of notes.
    u = (t >= ti) * (t <= ti + Ti[i]) # creating the unit step function necessary to cut the function
    signal += (np.sin(2 * np.pi * Fi[i] * t) + np.sin(2 * np.pi * fi[i] * t)) * u # adjusting the signal with new frequencies for other notes with each iteration
    ti += Ti[i] + 0.05 # adjusting the initial time of each note
plt.plot(t, signal) # ploting the signal
plt.show() # showing the signal
sd.play(signal, 3 * 1024) # playing the sound generated by the signal.