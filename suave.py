import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
from scipy.signal import convolve2d


#imagen a procesar para suavizado gaussiano

imagencitapng = plt.imread("imagen.png") #arreglar, es imagen
imagencitapngnueva = imagencitapng[:,:,0]

#np.shape para obtener las dimensiones de la imagen

dimensionesi = np.shape(imagencitapng)
largoimagencita = dimensionesi[0]
anchoimagencita = dimensionesi[1]



mm = np.linspace(-10, 10 ,largoimagencita)
def gauss(lins):
    ga = 1.0-np.exp((lins**2)*-0.05) #ancho del 5%
    return ga
gausss = gauss(mm)

#integracion para gauss por trapecios

a= -10.0
b= 10.0
N= largoimagencita
total = 0.0
delta = (b-a)/N
for i in range(N):
    ar = (gauss(a)+gauss(b+delta))*(delta/2.0)
    total = total + ar

#normalizar gaussiana para kernel, dividiendo gauss por su integral

gaussnormali = gausss/total

#se hace el kernel a partir de gauss normalizada

kern = np.tile(gaussnormali, (anchoimagencita,1)).T


#dimensiones kernel

dimensionesk = np.shape(kern)
largok = dimensionesk[0]
anchok = dimensionesk[1]


#funcion para transformada de fourier en dos dimensiones para imagenes muy pequenias y el kernel, solo se toma parte real con coseno

def transformadapng(elemento, eme, ene):
    for a in range(eme):
        tr =0.0
        for b in range(ene):
            for c in range(eme):
                sr = 0.0
                for d in range(ene):
                    #r =elemento[:,:,0]
                    trans = np.exp(np.cos(-2.0*np.pi*(((a*c)/eme)+((b*d)/ene))))
                    sr += elemento*trans
            tr = sr /eme / ene
    return tr
transimagencita = transformadapng(imagencitapngnueva, largoimagencita, anchoimagencita)
transkerne =transformadapng(kern, largok, anchok)


#se multiplica la transformada obtenida para la imagen y la transformada obtenida para el kernel

convov = transkerne*transimagencita
dimco = np.shape(convov)
at = dimco[0]
bt = dimco[1]

#transformada inversa para la convolucion, se cambia signo de la ecuacion negativo a positivo

def transformadainv(convovo, eme, ene):
    for a in range(eme):
        for b in range(ene):
            sr= 0.0
            for c in range(eme):
                for d in range(ene):
                     trans = np.exp(np.cos(2.0*np.pi*(((a*c)/eme)+((b*d)/ene))))
                     sr += convovo*trans
            r = sr + 0.5
    return r

transformadainversaparaconvolu = transformadainv(convov, at, bt)
print transformadainversaparaconvolu
plt.imshow(transformadainversaparaconvolu)
plt.savefig("suave.png")

                     
                     
    
    



        
