import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
from scipy.signal import convolve2d


#imagen a procesar para suavizado gaussiano
imagencitapng = plt.imread("imagen.png")

#transformada de fourier para la imagen
fouriertransformalaimagen = fftpack.fft2(imagencitapng, axes = (0,1))
#def funciontransformafourierdosde(matriz):
    #(M, N) = matriz.size()
   #for a in range(M):
       # for b in range(N):
            #for c in range(M):
                #for d in range(N):
                    #ma = []
                   # A = ((-1j*np.pi*2)*((a*c)/M)*((b*d)/N))
                    #ma.append(A)
    #return ma
            

#gaussiana
m = np.linspace(-10,10,20)
gaussi = 1.0 - np.exp((m**2)*0.5)
gaussinor = gaussi/np.trapz(gaussi)

#creacion de kernel para poder realizar convolucion

kernelconvolucion = np.tile(gaussinor, (15,1))

#transformada de fourier para el kernel
fouriertransformaelkernel = fftpack.fft2(kernelconvolucion, shape = imagencitapng.shape[:2], axes = (0,1))

#convolucion
convo = fouriertransformalaimagen*fouriertransformaelkernel
convoinv = fftpack.ifft2(convo).real



