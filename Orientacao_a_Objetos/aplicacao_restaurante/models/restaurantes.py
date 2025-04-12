#Self é referência da Instância
from models.avaliacao import Avaliacao
class Restaurant:

    restaurants = []
    def __init__(self, name, categoria):
        self._name = name.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao_list = []
        #Inserindo o novo restaurante instanciado na lista de restaurants
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'Nome: {self._name} | Categoria: {self._categoria} | Estado: {self._ativo}'
    
    @classmethod
    def list_restaurants(cls):
        for restaurant in cls.restaurants:
            print(f'Nome: {restaurant._name} | Categoria: {restaurant._categoria} | Estado: {restaurant._ativo} | Avaliação {restaurant.media_avaliacoes}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'
    
    def alterar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, client, nota):
        avaliacao = Avaliacao(client, nota);
        self._avaliacao_list.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao_list:
            return 0
        
        soma_das_notas =  sum(avaliacao._nota for avaliacao in self._avaliacao_list)
        quantidade_de_avaliacoes = len(self._avaliacao_list)
        media = round((soma_das_notas / quantidade_de_avaliacoes), 1)
        return media
            