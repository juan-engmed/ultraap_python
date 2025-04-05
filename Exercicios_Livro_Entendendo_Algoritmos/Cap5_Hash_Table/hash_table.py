#Iniciando uma hash table

restaurants = {}
restaurants.update({'Jobi':'Bar', 'Belmonte': 'Bar'})

print(restaurants)

#Usando get, o valor default caso não exista será None (que é do tipo Falsy, podendo usar em condicionais)
#Mas o ideal é usar if key in dict O(1)
tipo = restaurants.get('Jobi')
print(tipo)

if 'Jobi' in restaurants:
    print('Jobi está na lista')


restaurantes = {
    'restaurante1': {
        'nome': 'Sabor Caseiro',
        'endereco': 'Rua das Flores, 123',
        'avaliacao': 4.8
    },
    'restaurante2': {
        'nome': 'Delícias do Mar',
        'endereco': 'Av. Oceânica, 456',
        'avaliacao': 4.5
    }
}
#for key, value in dict.items()
for id_restaurante, dados in restaurantes.items():
    print(id_restaurante)
    print(dados)

votantes = {}
votantes['juan'] = True
if 'juan' in votantes:
    print('Ja votou')
#Por debaixo dos panos o set implementa uma Hash Table, com Keys, porém sem value
votantes_set = set()
votantes_set.add('juan')
if 'juan' in votantes:
    print('Ja votou')