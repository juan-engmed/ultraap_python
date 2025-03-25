# Bônus: escreva um programa que implementa a função de distribuição acumulada (CDF) referente à variável aleatória exponencial. O programa deve imprimir o valor da função para um dado valor de entrada.
from math import exp

def calc_cdf(lambda_value, x):
    cdf = 1 - exp(-lambda_value * x)
    return cdf

def main():
    try:
        lambda_value = float(input('Digite o valor de Lambda'))
        if lambda_value <= 0:
            raise ValueError("O valor de lambda deve ser maior que zero.")

        x_value = float(input('Digite o valor de X'))
        if x_value < 0:
            raise ValueError("Se X < 0 a CDF será 0")

        result = calc_cdf(lambda_value,x_value)
        print(f'O resultado da CDF é: {result:.4f}')

    except ValueError as ve:
        print(f'Ocorreu um erro: {ve}')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    

if __name__ == "__main__":
    main()
