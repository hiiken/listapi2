x1 = -7
y1 = 1

x2 = float(input())
y2 = float(input())

def calcula_distancia_Chebyshev(x1, y1, x2, y2):
    maiorx = abs(x2 - x1)
    maiory = abs(y2 - y1)
    chebyshev = max(maiorx, maiory)
    return chebyshev


distChebyshev = calcula_distancia_Chebyshev(x1, y1, x2, y2)
print("distancia Chebyshev = {:.2f}".format(distChebyshev))