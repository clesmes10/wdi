#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;


int encontrar_i(float x, float *x_original, int n)
{
	int i = 0;
	while (x > x_original[i])
	{
		i ++;
	}

	if (i>0)
	{
		i --;
	}
	return i;
}
int contemoslineas(){
  int lineas = 0;
  string line;
  ifstream myfile("datos.txt");
  while(getline(myfile, line)){
    ++lineas;
  }
  return lineas;
}

int carguemosdatos(float *x_original, float *y_original, int n){
  int i;
  ifstream in("datos.txt");
  for(i=0; i< n; ++i){
      in >> x_original[i] >> y_original[i];
    }
}
float creamosarreglo(float hache, float *xn, float *x_original, float *y_original, int i, int n){
  hache =(x_original[n-1] - x_original[0])/(n-1);
  xn[i] = {x_original[0]};
  for(i=1; i<n; ++i){
    xn[i] = xn[i-1] + hache;
  }
  return hache;
}
int interpolar(float *xn, float* yn, float *x_original, float *y_original, int j, int n, int i){
    int k;
    int nmax = 3;
    float x;
    float yj;
    float lj;
    int i_interp;
    float L;
    int i_polinomios;
    int i0;

	i_polinomios = 0;
    for (i_interp = 0; i_interp < n; ++i_interp)
    {
	    x = xn[i_interp];
	    L = 0;
	    i_polinomios = encontrar_i(x,x_original,n);

	    if (i_polinomios+nmax<n)
	    {
	    	i0 = i_polinomios;
	    }else
	    {
	    	i0 = n-nmax;
	    }

	    // Sumatoria
	    for (j = i0; j < i0+nmax; ++j)
	    {
	    	yj = y_original[j];
	    	lj = 1.0;

	    	// multiplicatoria
	    	for (i = i0; i < i0+nmax; ++i)
	    	{
	    		if (i!=j)
	    		{
	    			lj = lj*(x-x_original[i])/(x_original[j]-x_original[i]);
	    		}
	    	}

	    	L += yj*lj;
	    }
	    yn[i_interp] = L;

	    //cout << i0 << ' ' <<i0+nmax-1<< ' '<< xn[i_interp] << ' ' << yn[i_interp] << '\n';
	}
    return j;
}
  


// funcion main para la ejecucion del codigo
int main() {
	
	// contar lineas
	cout << "Starting the software\n";
	int n = contemoslineas();
    cout << "Number of lines: " << n << '\n';
	
    // cargar datos
    float x_original[n];
    float y_original[n];
    int i = carguemosdatos(x_original, y_original, n);

    // crear arreglo uniformemente espaciado
    float hache;
    float xn[n];
    hache = creamosarreglo(hache, xn, x_original, y_original, i, n);


    // Interpolar con lagrange
    float yn[n];
    int j = 0;
    j = interpolar(xn, yn, x_original, y_original, j, n, i);
   

	float Ygrande_r[n];
	float Ygrande_i[n];
	float Fgrande[n];
	float df;
	df = (0.5/hache)/(n/2);
	ofstream out("transformada.txt");

	cout << '\n' << hache << ' ' << df << '\n';

	// Fourier
	for ( i = 0; i < n; ++i )
	{
		for ( j = 0; j < n; ++j )
		{
			Ygrande_r[i] += yn[j]*cos(-2*3.14159*i*j/n);
			Ygrande_i[i] += yn[j]*sin(-2*3.14159*i*j/n);
		}
		if (i<=n/2)
		{
			Fgrande[i] = i*df;
		}
		else
		{
			Fgrande[i] = -(0.5/hache) + (i-n/2)*df;
		}

		out << Fgrande[i] << ' ' << Ygrande_r[i] << ' ' << Ygrande_i[i] << '\n';
	}



	cout << "\n\nEnd\n\n";

   return 0;
}
 
