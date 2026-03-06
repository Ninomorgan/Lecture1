from dataclasses import dataclass
from typing import Protocol


class Prodotto:
    iva = 0.22  # variabiebile di clasee fissa --> uguale per tutti

    def __init__(self, name: str, price: float, quantity: int, supplier=None):  # name: str,

        self.name = name
        self._price= None #si setta a none E POI SI PASSA IL SETTER
        self._price = price #per proteggere la variabile price --> definirla con _price oppure __price e non ci fa accede alla variabile
        self.quantity = quantity
        self.supplier = supplier

    #utiliziamo quindi _price e usiamo costrutti come GETTER E SETTER
    @property
    def price(self): #GETTER
        return self._price

    @price.setter
    def price(self, valore):
        if valore < 0:
            raise ValueError("Valore negativo") #MESSAGGIO DI ERRORE

        self._price = valore


    def valore(self):
        return self.price * self.quantity

    @staticmethod
    def sconto(prezzo, percentuale):  # non passo self e cls
        return prezzo * (1 - percentuale)

    def __str__(self): ##r  METODO PRINT TO STRING
        return f"nome è{self.name} - disponibili {self.quantity} pezzi a {self.price}"

    def __repr__(self): #serve per il debug
        return f"prodotto (name={self.name }, price = {self.price}, quantity = {self.quantity}, supplier = {self.supplier})"

    #CONFRONTO
    def __eq__(self, other): #conforntiamo con oggetto DIVERSI
        #o è uguale o diverso
        if not isinstance(other, Prodotto): #se non è un prodotto
            return NotImplemented
        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)

    def __lt__(self, other) -> bool: #ricevo un buleano
        return self.price < other.price #ORDINE

    def prezzo_finale(self) -> float:
        return self.price

class ProdottoScontato(Prodotto):
    def __init__(self, name: str, price: float, quantity: int, supplier:str, sconto_percento: float):
        #Prodotto.__init__():
        super().__init__(name,price,quantity,supplier)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self):
        return (self.valore()*(1-self.sconto_percento/100))

class Servizio(Prodotto):
    def __init__(self, name: str, tariffa_oraria, ore: int):
        super().__init__(name=name, price = tariffa_oraria, quantity=1, supplier=None)
        self.ore = ore

    def prezzo_finale(self) :
        return self.price*self.ore


class Abbonamento:
    def __init__(self, name: str, prezzo_mensile: float, mesi: int):
        self.name = name
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.prezzo_mensile * self.mesi

class HaPrezzoFinale(Protocol):
    def prezzo_finale(self) ->float:
        ... #indicano che non devo aggiungere codice --> il metodo prezzo finale viene gestito dalle singole classi
    #devo solo indicare quale metodo mi aspetto

@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float
    #la classe avrà un costruttore automatico
def _test_modulo():
    prodottto1_nome = "laptop"
    prodotto1_prezzo = 1200.0
    prodotto1_quantita = 5

    prodottto2_nome = "Mouse"
    prodotto2_prezzo = 120
    prodotto2_quantita = 15

    valore_magazzino = prodotto1_quantita * prodotto1_prezzo + prodotto2_prezzo * prodotto2_quantita
    print(f" valore:{valore_magazzino}")

    myproduct1 = Prodotto(name="Laptop", price=1200, quantity=12, supplier="ABC")
    print(f"nome prodottor: {myproduct1.name}")
    print(f"prezzo : {myproduct1.price}")

    myproduct2 = Prodotto(name="mouse", price=10, quantity=10, supplier="CDE")
    print(f"nome prodottor: {myproduct2.name}")
    print(f"prezzo : {myproduct2.price}")

    print(f"il prezzo scontato è {Prodotto.sconto(myproduct1.price, percentuale=0.15)}")
    print(myproduct1)
    p_a= Prodotto(name="Laptop", price=1200, quantity=12, supplier="ABC")
    p_b= Prodotto(name="mouse", price=10, quantity=14, supplier="CDE")

    print ("myproduct1==p_a?", myproduct1 == p_a)#aspetto true
    print("p_a==p_b?",  p_a==p_b) #false

    #FACCIAMO UN SORT
    mylist= [p_a, p_b, myproduct1]
    mylist.sort()

    print("lista prodotti ordinate")
    for p in mylist:
        print(f"-{p}") #VIENE ORDINATO PER PREZZO

    #INERITHANCE
    #SOTTOCLASSE PRODOTTO


    #CLASSE SERVIZIO SOTTOCLASSE DI PRODOTTO



    my_prod_scontato=ProdottoScontato(name = "auricolari", price = 320, quantity = 1, supplier = "ABC", sconto_percento = 10)
    my_service= Servizio(name="Consulenza", tariffa_oraria=100, ore=3)

    mylist.append(my_service)
    mylist.append(my_prod_scontato)

    for e in mylist:
        print(e.name, "-->", e.prezzo_finale)
    print(f"-"*60)

    #definiamo una classe Abbonamento con attributti: nome,prezzo_mensile, mesi;
    #con metodo per calcolo prezo finale = prezzo mensile*mesi
    #



    abb1= Abbonamento ("Spotify", 25.0, 3)
    mylist.append(abb1)
    for e in mylist:
        print(e.name, "-->", e.prezzo_finale())

    def calcola_totale(elementi): #non si inresessa del tipo di oggetot
        tot = 0
        for e in elementi:
            tot += e.prezzo_finale()

        return tot

    print(f"il totale è: {calcola_totale(mylist)}")

    print(f"-"*60)
    print("dataclass")

    #PROTOCOLLO --> CI PERMETTE DI SPECIFICARE QUALI SONO I METODI CHE CI ASPETTIAMO CHE QUESTI CLASSI ABBIANO
    #Posso dire che in elementi ci devono stare solo classi che hanno elemento prezzo_finale()

    from typing import Protocol



    def calcola_totale(elementi: list[HaPrezzoFinale]) -> float:
        return sum(e.prezzo_finale() for e in elementi)

max_quantita=1000

def crea_prodotto_standar(nome:str,prezzo:float):
        return Prodotto(nome,prezzo,1, supplier=None,)

if __name__ == "__main__":
    _test_modulo()