CPF_DIGITS = 11
FREE_ASSENT_VALUE = ['Livre', '000']
NUMBER_OF_ASSENTS_PER_LINE = 6
LETTERS_OF_ASSENTS_PER_LINE = 'ABCDEF'

def initial_departure_tickets():
    assentos = []
    for number in range(1, NUMBER_OF_ASSENTS_PER_LINE + 1):
        for letter in LETTERS_OF_ASSENTS_PER_LINE:
            assentos.append(f'{number}{letter}')
    return dict.fromkeys(assentos, FREE_ASSENT_VALUE)

def is_flight_full(departure_tickets):
    return FREE_ASSENT_VALUE not in departure_tickets.values()

def is_valid_name(name):
    return len(name.strip()) >= 2

def is_valid_cpf(cpf):
    return cpf.isdigit() and len(cpf) == CPF_DIGITS

def get_full_name():
    try:
        full_name = input("Digite seu nome completo: ").strip()
        if not is_valid_name(full_name):
            print("Nome inválido")
            return get_full_name()
        return full_name
    except Exception as e:
        print(f"Erro inesperado ao cadastrar o nome completo: {e}")
        return get_full_name()

def get_cpf():
    try:
        cpf = input("Digite seu CPF (ex: 12345678900): ").strip()
        if not is_valid_cpf(cpf):
            print("CPF Inválido")
            return get_cpf()
        return cpf
    except Exception as e:
        print(f"Erro inesperado ao cadastrar o cpf: {e}")
        return get_cpf()

def associate_ticket_client(departure_tickets, client):
    for key, value in departure_tickets.items():
        if value == FREE_ASSENT_VALUE:
            departure_tickets[key] = client
            print(f"Assento reservado: {key}")
            break

def print_percentual_occuped_assents(departure_tickets):
    total = len(departure_tickets)
    ocupados = sum(1 for v in departure_tickets.values() if v != FREE_ASSENT_VALUE)
    percentual = (ocupados / total) * 100
    print(f'{percentual:.1f}% dos Assentos Ocupados')

def print_all_departure_tickets(departure_tickets):
    print('\nListagem dos Assentos Ocupados/Livres')
    for k, v in departure_tickets.items():
        status = 'Livre' if v == FREE_ASSENT_VALUE else f'Passageiro: {v[0]} | CPF: {v[1]}'
        print(f'Assento: {k} | {status}')

def main():
    departure_tickets = initial_departure_tickets()

    while True:
        if is_flight_full(departure_tickets):
            print("Vôo está lotado! Encerrando o programa...")
            break

        print("\n=== MENU PRINCIPAL ===")
        print("Digite 1 para Realizar Reserva")
        print("Digite 2 para Encerrar o Programa.")
        option_input = input('').strip()

        if option_input == '2':
            break
        elif option_input == "1":
            full_name = get_full_name()
            cpf = get_cpf()
            associate_ticket_client(departure_tickets, [full_name, cpf])
        else:
            print("Opção inválida. Tente novamente.")

    print('\n=== Resumo Final ===')
    print_percentual_occuped_assents(departure_tickets)
    print_all_departure_tickets(departure_tickets)

if __name__ == "__main__":
    main()