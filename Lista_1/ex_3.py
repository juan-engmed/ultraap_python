# Escreva um programa que imprime a área e a circunferência de um círculo cujo raio é fornecido pelo usuário.

from math import pi, pow

def calc_area_by_radius(radius):
    return pi*pow(radius,2)

def calc_circ_by_radius(radius):
    return 2*pi*radius

def main():
    try:
        radius = float(input("Digite o raio para calcular a área e a circuferência\n"))
        area = calc_area_by_radius(radius)
        circ = calc_circ_by_radius(radius)

        print(f'Raio: {radius:.2f} | Área: {area:.2f} | Circunferência: {circ:.2f}')

    except ValueError:
        print('Digite um número válido')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

                     
if __name__ == "__main__":
    main()