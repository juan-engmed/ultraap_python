from exceptions import NumeroNegativoException

def calc_fat(number):
    if number == 0 or number == 1:
        return 1
    return number * calc_fat(number - 1)       

def main():
    try:
        number = int(input('Digite um número para calcular seu fatorial'))
        if number < 0:
            raise NumeroNegativoException(number)
        
        result_fat = calc_fat(number)
        print(result_fat)
    except NumeroNegativoException as e:
        print(e)

    except ValueError as ve:
        print(f'Digite um número válido e inteiro, erro causado por: {ve}')


if __name__ == "__main__":
    main()