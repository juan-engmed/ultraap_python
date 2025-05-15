def is_valid_code(code):
    return code.isdigit() and 1 <= int(code) <= 9999

def is_valid_age(age_str):
    return age_str.isdigit() and int(age_str) >= 18

def is_valid_height(height_str):
    try:
        return float(height_str) >= 1.0
    except ValueError:
        return False

def classify_height(height):
    if 1.00 <= height <= 1.34:
        return 'A'
    elif 1.35 <= height <= 1.54:
        return 'B'
    elif 1.55 <= height <= 1.74:
        return 'C'
    elif 1.75 <= height <= 1.94:
        return 'D'
    elif height >= 1.95:
        return 'E'
    return None

def cadastrar_dado(heights, height_bins):
    try:
        code = input("Digite o código (0001 a 9999): ").strip()
        if not is_valid_code(code):
            print("CARTÃO INVÁLIDO")
            return

        age = input("Digite a idade (>= 18): ").strip()
        if not is_valid_age(age):
            print("IDADE FORA DA FAIXA. Registro ignorado.")
            return

        while True:
            height_str = input("Digite a altura em metros (ex: 1.70): ").strip()
            if not is_valid_height(height_str):
                print("ALTURA INVÁLIDA. Tente novamente.")
                continue

            height = float(height_str)
            heights.append(height)

            faixa = classify_height(height)
            if faixa:
                height_bins[faixa] += 1
            break  # altura válida → sair do while interno

    except Exception as e:
        print(f"Erro inesperado ao cadastrar: {e}")

def mostrar_media(heights):
    if not heights:
        print("Nenhuma altura válida registrada.")
        return
    media = sum(heights) / len(heights)
    print(f"\nAltura média: {media:.2f}m")

def mostrar_percentual(heights, height_bins):
    if not heights:
        print("Nenhuma altura válida registrada.")
        return
    total = len(heights)
    print("\nFaixa --- Percentual")
    for faixa in 'ABCDE':
        percentual = (height_bins.get(faixa, 0) / total) * 100
        print(f"{faixa} --- {percentual:.1f}%")

def main():
    heights = []
    height_bins = {faixa: 0 for faixa in 'ABCDE'}

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("[1] Cadastrar código, idade e altura")
        print("[2] Ver média das alturas")
        print("[3] Ver percentual por faixa")
        print("[4] Ver ambos")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\nPrograma Finalizado.")
            break
        elif opcao == "1":
            cadastrar_dado(heights, height_bins)
        elif opcao == "2":
            mostrar_media(heights)
        elif opcao == "3":
            mostrar_percentual(heights, height_bins)
        elif opcao == "4":
            mostrar_media(heights)
            mostrar_percentual(heights, height_bins)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
