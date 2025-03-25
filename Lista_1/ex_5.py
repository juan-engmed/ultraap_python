# Escreva um programa que imprima a média ponderada de três valores numéricos dados pelo usuário. Os pesos de cada valor podem ser definidos no programa ou fornecidos pelo usuário.

def calc_weighted_average(array):
    sum_grade_weight = 0
    sum_weight = 0
    for grade, weight in array:
        sum_grade_weight += grade*weight
        sum_weight += weight

    return sum_grade_weight/sum_weight
    
def main():
    tuple_test = []
    try:
        value_test_1 = float(input("Digite a nota da Prova 1"))
        weight_test_1 = int(input("Digite o peso da Prova 1"))

        tuple_test.append((value_test_1, weight_test_1))

        value_test_2 = float(input("Digite a nota da Prova 2"))
        weight_test_2 = int(input("Digite o peso da Prova 2"))

        tuple_test.append((value_test_2, weight_test_2))

        value_test_3 = float(input("Digite a nota da Prova 3"))
        weight_test_3 = int(input("Digite o peso da Prova 3"))

        tuple_test.append((value_test_3, weight_test_3))

        result = calc_weighted_average(tuple_test)
        print(f'O resultado da média ponderada é: {result:.2f}')

    except ValueError:
        print("Por favor, digite apenas números válidos.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()