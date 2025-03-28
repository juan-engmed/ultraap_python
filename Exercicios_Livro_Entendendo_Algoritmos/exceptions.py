class NumeroNegativoException(ValueError):
    def __init__(self, valor):
        super().__init__(f"Valor negativo não permitido: {valor}")