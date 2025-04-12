from models.restaurantes import Restaurant

restaurant_1 = Restaurant('Jobi', 'Bar')
restaurant_2 = Restaurant('Pizzaria Guanabara', 'Restaurant')

restaurant_1.alterar_estado()

restaurant_1.receber_avaliacao('Juan',10)
restaurant_1.receber_avaliacao('Beatrice',9)

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()