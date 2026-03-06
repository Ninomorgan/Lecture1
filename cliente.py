from dataclasses import dataclass


class Cliente:
    def __init__(self, name: str, email: str, categoria: str):
        self.name = name
        self.email = email
        self._categoria = None #MODIFICO CATEGORIA IN _CATEGORIA
        self.categoria = categoria #qua uso self.categoira

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria):  #SE NON RIENTRA IN QUESTA CATEGORIA SARà UGUALE A NONE
        categorie_valide = {"gold", "silver", "bronze"}
        if categoria not in categorie_valide:
           raise ValueError(f"Categoria invalida: scegliere fra gold silver bronze")
        #if categoria=="gold":
           # self._categoria = categoria
        #if categoria=="silver":
            #self._categoria = categoria
        #if =="bronze":
           # self._categoria = categoria




    def descrizione(self):
        return f"Cliente {self.name} ({self.categoria}) - {self.email}"

   # @classmethod  # estende i metodi a tutte le istanze (esempio scrivere dei costruttori alternaitivi)
   # def costruttore_con_quantita_1(cls, nome, email, categoria):
    #    cls(nome, email="no", categoria)


@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria: str

def _test_modulo():
    cliente1 = Cliente(name="Fulvio", email="fulvio@gmail.com", categoria="gold")
    print(cliente1.descrizione())


#2) metodo getter del prodotto

#3)MODIFICAIMO CATEGORIA E FACCIAMO CHE ACCETTI SOLO CATEORIA GOLD SILVER E BRONZE


if __name__ == "__main__":
    _test_modulo()
