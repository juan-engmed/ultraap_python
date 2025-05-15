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

def print_summary(heights, height_bins):
    if not heights:
        print("Nenhuma altura válida foi registrada.")
        return

    media = sum(heights) / len(heights)
    print(f'\nAltura média: {media:.2f}m')

    total = len(heights)
    print("\nFaixa --- Percentual")
    for faixa in 'ABCDE':
        percentual = (height_bins.get(faixa, 0) / total) * 100
        print(f"{faixa} --- {percentual:.1f}%")

def main():
    heights = []
    height_bins = {faixa: 0 for faixa in 'ABCDE'}

    while True:
        try:
            code = input("Digite o código (0001 a 9999) ou -1 para sair: ").strip()
            if code == "-1":
                break

            if not is_valid_code(code):
                print("CARTÃO INVÁLIDO")
                continue

            age = input("Digite a idade (>= 18): ").strip()
            if not is_valid_age(age):
                print("IDADE FORA DA FAIXA. Pulando para o próximo código.")
                continue

            while True:
                try:
                    height_str = input("Digite a altura em metros (ex: 1.70): ").strip()
                    if not is_valid_height(height_str):
                        print("ALTURA INVÁLIDA")
                        continue

                    height = float(height_str)
                    heights.append(height)

                    faixa = classify_height(height)
                    if faixa:
                        height_bins[faixa] += 1
                    break  # altura válida → sair do while interno

                except Exception as e:
                    print(f"Erro ao ler altura: {e}")
                    continue

        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            continue

    print_summary(heights, height_bins)
    print("\nPrograma Finalizado.")
