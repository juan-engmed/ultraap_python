# Escreva um programa que calcule a distância entre dois pontos. As coordenadas dos pontos devem ser fornecidas pelo usuário.
import math

def calc_distance(pointA, pointB):
    x1, y1 = pointA
    x2, y2 = pointB
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    try:
        a_x = float(input("Digite a coordenada X do ponto A: "))
        a_y = float(input("Digite a coordenada Y do ponto A: "))
        a_coord = (a_x, a_y)

        b_x = float(input("Digite a coordenada X do ponto B: "))
        b_y = float(input("Digite a coordenada Y do ponto B: "))
        b_coord = (b_x, b_y)

        distance = calc_distance(a_coord, b_coord)

        print(f"\nPonto A: {a_coord}")
        print(f"Ponto B: {b_coord}")
        print(f"O módulo da distância entre os dois pontos é: {distance:.2f}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()