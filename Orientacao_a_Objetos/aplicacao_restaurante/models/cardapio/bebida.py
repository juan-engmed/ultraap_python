from models.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self._volume = volume