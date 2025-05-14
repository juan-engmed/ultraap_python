from models.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self._description = description