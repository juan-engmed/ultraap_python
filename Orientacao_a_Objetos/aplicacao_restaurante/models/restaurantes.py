#Self é referência da Instância
class Restaurant:
    def __init__(self, name, categoria):
        self.name = name
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'Nome: {self.name} | Categoria: {self.categoria} | Ativo: {self.ativo}'

restaurant_1 = Restaurant('Jobi', 'Bar')
restaurant_2 = Restaurant('Pizzaria Guanabara', 'Restaurant')

#Imprime o endereço na memória
restaurants = [restaurant_1, restaurant_2]
print(restaurants)

#Com o método __str__ implementado o Python realiza a conversão para String (Semelhante ao toString do Java)
print(restaurant_1)
