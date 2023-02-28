import numpy as np # importing the numpy library
import matplotlib.pyplot as plt # importing the matplotlib.pyplot library
import sounddevice as sd # importing the sounddevice library
from scipy.fftpack import fft # importing fft from the scipy.fftpack package
t = np.linspace(0 , 3 , 12 * 1024) # setting the time t of the signal
Fi = np.array([164.81, 164.81, 164.81, 174.61, 174.61, 164.81, 146.83, 146.83, 130.81, 130.81, 246.93, 246.93, 130.81, 164.81, 164.81, 146.83, 146.83, 130.81, 246.93, 164.81]) # the frequency of the 3rd octave (Left Hand)
fi = np.array([261.63, 261.63, 392, 392, 440, 440, 392, 349.23, 349.23, 329.63, 329.63, 293.66, 293.66, 261.63, 392, 392, 349.23, 349.23, 329.63, 329.63]) # the frequency of the 4th octave (Right Hand)
ti = 0 # setting the initial time to zero
Ti = [0.2, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2] # this is how long each note will last
signal = 0 # initializing the signal to zero
for i in range (0, 20): # number of pairs is 20 N = 20 pairs of notes.
    u = (t >= ti) * (t <= ti + Ti[i]) # creating the unit step function necessary to cut the function
    signal += (np.sin(2 * np.pi * Fi[i] * t) + np.sin(2 * np.pi * fi[i] * t)) * u # adjusting the signal with new frequencies for other notes with each iteration
    ti += Ti[i] + 0.05 # adjusting the initial time of each note
plt.subplot(3, 2, 1) # creating a subplot of 3 rows and 2 colomns
plt.plot(t, signal) # ploting the signal in the time domain
N = 3 * 1024 # setting the number of samples N to be the duration of the song multiplied by 1024
f = np.linspace(0, 512, int(N/2)) # setting the frequency array with a range from 0 to 512 with a sample size of the integere division of N / 2
x_f = fft(signal) # taking the fourier transfrom of the original signal and assinging it to x_f
x_f = 2/N * np.abs(x_f [0:int(N/2)]) # we take the first N / 2 elements then we take their absolute value to allow for plotting
# then we multiply it by 2 because  because the spectrum returned by fft is symmetric about the DC component (f=0).
# then we divide by N because each point of the FFT transform is the result of a sum over a time interval of N samples
plt.subplot(3, 2, 2) # placing the plot of the x_f in the subplot
plt.plot(f, x_f) # ploting the signal in the frequency domain
max = np.max(x_f)
Fn = np.random.randint(0, 512, 2) # creating an array of size two with two random frequencies to be used in generating the noise
nt = np.sin(2 * np.pi * Fn[0] * t) + np.sin(2 * np.pi * Fn[1] * t) # creating the noise function n(t) using the frequencies generated previously
signalnt = signal + nt # creating the signal signaln(t) and assigning it the value of the original signal with the noise function n(t) added to it
plt.subplot(3, 2, 3) # placing the signal signalnt in the subplot
plt.plot(t, signalnt) # ploting the signalnt in the time doamin
x_f2 = fft(signalnt) # taking the fourier transfrom of the signal with noise and assinging it to x_f2
x_f2 = 2/N * np.abs(x_f2 [0:int(N/2)]) # we take the first N / 2 elements then we take their absolute value to allow for plotting
# then we multiply it by 2 because  because the spectrum returned by fft is symmetric about the DC component (f=0).
# then we divide by N because each point of the FFT transform is the result of a sum over a time interval of N samples
plt.subplot(3, 2, 4) # placing the signal x_f2 in the subplot
plt.plot(f, x_f2) # ploting the signal x_f2 in the frequency domain
toBeCancelled = x_f2 - x_f # getting a signal in the frequency domain that contins the noise frequencies only
frequencies = [0,0] # instantiating an array of size two called frequencies which is empty or contains zeros
j = 0 # instantiating a counter for the frequencies array
i = 0 # instantiating a counter for the while loop used to loop through the toBeCancelled signal
while(i < len(toBeCancelled)): # looping over the toBeCancelled signal
    if(toBeCancelled[i] > max): # checking to see if any of the signals has an amplitud of more than 1.5, which means that this is a noise frequency
        frequencies[j] = f[i] # if true we take the frequency, which is the x axis, of the of the corresponding signal toBeCancelled[i]
        j += 1 # incrementing the frequencies array counter by one
    i += 1 # incrementig the while loop counter by one
finalSignal = signalnt - (np.sin(2 * np.pi * np.round(frequencies[0]) * t) + np.sin(2 * np.pi * np.round(frequencies[1]) * t)) # creating a final signal which is the result of subtracting the noise frequencies from the signal with noise signalnt
plt.subplot(3, 2, 5) # placing the graph of the finalSignal in the subplot
plt.plot(t, finalSignal) # ploting the finalSignal in the time domain
x_f1 = fft(finalSignal) # taking the fourier transfrom of the signal with noise and assinging it to x_f1
x_f1 = 2/N * np.abs(x_f1 [0:int(N/2)]) # we take the first N / 2 elements then we take their absolute value to allow for plotting
# then we multiply it by 2 because  because the spectrum returned by fft is symmetric about the DC component (f=0).
# then we divide by N because each point of the FFT transform is the result of a sum over a time interval of N samples
plt.subplot(3, 2, 6) # placing the graph of x_f1 in the subplot
plt.plot(f, x_f1) # ploting the graph of x_f1 in the frequency domain
plt.show() # showing the plot
sd.play(finalSignal,3*1024) # playing the finalSignal, which is the song.