prodottto1_nome = "laptop"
prodotto1_prezzo = 1200.0
prodotto1_quantita = 5

prodottto2_nome = "Mouse"
prodotto2_prezzo = 120
prodotto2_quantita = 15

valore_magazzino = prodotto1_quantita * prodotto1_prezzo + prodotto2_prezzo * prodotto2_quantita
print(f" valore:{valore_magazzino}")

#METODI GETTER - SETTER
#METODI PROTOCOL
#METODI DATACLASS
#SOTTOCLASSI E INHERITANCE




# classe cliente con campi nome email e categoria(gold/silver/bronze) e metodo descrizione che restituisce una stringa con
# cliente fulvio bianchi (gold) - fulvio@gmail

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


cliente1 = Cliente(name="Fulvio", email="fulvio@gmail.com", categoria="gold")
print(cliente1.descrizione())


#2) metodo getter del prodotto

#3)MODIFICAIMO CATEGORIA E FACCIAMO CHE ACCETTI SOLO CATEORIA GOLD SILVER E BRONZE

#INERITHANCE
#SOTTOCLASSE PRODOTTO

#DATACLASS -> genera in modo automatico queste cose
from dataclasses import dataclass
@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float
    #la classe avrà un costruttore automatico

@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria: str

#gestiamo ordini
@dataclass
class RigaOrdine:
    prodotto: ProdottoRecord
    quantita: int

    def totale_riga(self):
        return self.prodotto.prezzo_unitario*self.quantita

@dataclass
class Ordine: #lista di ordini
    righe: list[RigaOrdine]
    cliente: ClienteRecord
    iva=0.22

    def totale_netto(self):
        return sum(r.totale_riga() for r in self.righe)

    def totale_lordo(self):
        return self.totale_netto()*(1+self.iva)

    def numero_righe(self):
        return len(self.righe)

@dataclass
class OrdineSconto(Ordine):
    sconto_percento: float

    def totale_scontato(self):
        return (1-self.sconto_percento)*self.totale_lordo()

    #override method
    def totale_netto(self):
        netto_base= super().totale_netto() #PRENDIAMO IL METODO PRINCIPALE DALLA CLASSE PADRE
        return netto_base*(1-self.sconto_percento)


c1= ClienteRecord("Mario ROssi", "mariorossi@gmail.com", "Gold")
p3 = ProdottoRecord("Laptop", 1200.0)
p4 = ProdottoRecord("Mouse", 20)

ordine=Ordine([RigaOrdine(p3,2),RigaOrdine(p4,10)], c1)

ordine_scontato= OrdineSconto([RigaOrdine(p3,2),RigaOrdine(p4,10)], c1, 0.1 )

print (ordine)
print("Numero righe ordine: ", ordine.numero_righe())
print("Totale netto:" , ordine.totale_netto())
print ("Totale lordo:", ordine.totale_lordo())
print("---")
print(ordine_scontato)
print("totale scontato: ",ordine_scontato.totale_scontato())
print("totale loro: " , ordine_scontato.totale_lordo())






"""
import networkx as nx


#vendite -- fatture
from dataclasses import dataclass
@dataclass
class Fattura:
    ordine: "Ordine"
    numero_fattura: str
    data: date

    def genera_fattura(self):
        linee = [
            f"="*60,
            #intestazione fattura, data e numero
            f"Fattura n. {self.numero_fattura} del {self.data}"
            f"="*60,
            #dettagli del cliente
            f"cliente: {self.ordine.cliente.name}",
            f"categoria:  {self.ordine.cliente.categoria}",
            f"mail: {self.ordine.cliente.email}",

            f"DETTAGLIO ORDINE"
        ]
        for i,riga in enumerate (self.ordine.righe): #enumerate mi da sia indice che riga
            linee.append(
                f"{i}"
                f"{riga.prodotto.name}"
                f"quantità: {riga.quantita} x {riga.prodotto.prezzo_unitario} ="
                f"tot. {riga.totale_riga()}"

            )
        linee.extend(
            f"-"*60,
            f"Totale netto: {self.ordine.total_netto()}",
            f"IVA: {self.ordine.totale_netto()*0.22}",
            f" TOTALe lordo: {self.ordine.totale_lordo()}"
            f"="*60
        )
        return "\n".join(linee)

    def _test_modulo():
        p1 = ProdottoRecord:("Laptop",1200.0)
        p2= ProdottoRecord: ("MOuse", 20.0)

        cliente = CLiente("Mario Rossi", "mario.bianchi@gmail.com", "Gold")
        ordine= Ordine(righe= [
         RigaOrdine(p1,5), RigaOrdine(p2,5), RigaOrdine(p3,2)
        ], clinic=cliente)
        fattura = Fattura(ordine, "2026", date.today())

    if __name__ == "__main__":
        _test_modulo()
"""