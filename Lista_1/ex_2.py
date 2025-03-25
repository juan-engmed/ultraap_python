# Escreva um programa que receba uma temperatura em Celsius e imprima a temperatura em Kelvin e em Fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*1.8 + 32)
    return fahrenheit

def convert_celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def main():
    try:
        celsius_str = float(input('Digite a temperatura em Celsius\n'))
        
        result_in_fahrenheit = convert_celsius_to_fahrenheit(float(celsius_str))
        result_in_kelvin = convert_celsius_to_kelvin(float(celsius_str))

        print(f'O valor de {float(celsius_str)} em Fahrenheit é: {result_in_fahrenheit:.1f}\n')
        print(f'O valor de {float(celsius_str)} em Kelvin é: {result_in_kelvin:.2f}\n')

    except ValueError:
        print('Digite um número válido')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')


if __name__ == "__main__":
    main()