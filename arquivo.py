import math

print(pow(2,3))
print(math.sqrt(16))

def equacao_2grau(a, b, c):
    delta= pow(b, 2) - 4*a*c
    if delta <0:
      return "raiz negativa, solucao é imaginaria"
    else:
      raiz_delta = math.sqrt(delta)
      x1 = (-b + raiz_delta)/2*a
      x2 = (-b -raiz_delta)/2*a
      resultado = x1, x2 #raizes armazenadas em tupla
      return resultado

#raizes_equacao= tupla com 2 elementos
raizes_equacao = equacao_2grau(2, 3, -1)
print("Resultado da equacao de segundo grau: ")
print("x1 = ", raizes_equacao[0])
print("x2 = ", raizes_equacao[1])