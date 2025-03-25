# Escreva um programa que receba um nome completo (nome e sobrenome) e imprima uma mensagem de boas-vindas.

def validar_nome(nome: str) -> bool:
    return nome.isalpha()

def main():
    try:
        user_name = input('Digite seu nome:\n').strip()
        if not user_name:
            raise ValueError("Nome não pode estar vazio.")
        if not validar_nome(user_name):
            raise ValueError("Nome não pode conter números ou caracteres especiais.")

        user_last_name = input('Digite seu sobrenome:\n').strip()
        if not user_last_name:
            raise ValueError("Sobrenome não pode estar vazio.")
        if not validar_nome(user_last_name):
            raise ValueError("Sobrenome não pode conter números ou caracteres especiais.")

        print(f'\nBem-vindo, {user_name} {user_last_name}!')
    except Exception as e:
        print(f'Erro: {e}')

if __name__ == "__main__":
    main()
