# Escreva um programa que calcule as raízes de uma equação do segundo grau. Os coeficientes devem ser fornecidos pelo usuário. Exiba o resultado com três casas decimais.

from math import sqrt

def calc_delta(a,b,c):
   return b**2 -4*a*c

def calc_roots(a,b,delta):
   if delta < 0:
        raise ValueError("A equação não possui raízes reais.")
   
   x1 = (-b + sqrt(delta)) / (2 * a)
   x2 = (-b - sqrt(delta)) / (2 * a)

   return (x1,x2)
   

def main():
    try:
       coef_a = float(input('Digite o coefieciente a: '))

       if coef_a == 0:
            raise ValueError("O coeficiente 'a' não pode ser zero (não é equação do 2º grau).")
       
       coef_b = float(input('Digite o coefieciente b: '))
       coef_c = float(input('Digite o coefieciente c: '))

       delta = calc_delta(coef_a, coef_b, coef_c)
       roots = calc_roots(coef_a, coef_b, delta)

       print(f'As raízes da equação são: x1 = {roots[0]:.3f} | x2 = {roots[1]:.3f}')

    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()