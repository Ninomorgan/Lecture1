from ordini import Ordine, OrdineSconto, RigaOrdine
#METODI GETTER - SETTER
#METODI PROTOCOL
#METODI DATACLASS
#SOTTOCLASSI E INHERITANCE

#METODI PER IMPORTARE
#1) from prodotti import ProdottoScontato
#2) from prodotti import ProdottoScontato as ps --> lo chiamo ps
#3) import prodotti

#1)
from prodotti import Prodotto, crea_prodotto_standar


p1= Prodotto("ebook", 120.0, 1, "AAA")
p2=crea_prodotto_standar("Tablet",750)

print(p1)

#2)
from prodotti import ProdottoScontato as ps
p3 = ps("cuffie", 230,1,"abc", 0.1)

#3)
import prodotti
p4 = prodotti.ProdottoScontato("mp3", 230,1," AAA",0.2)


# classe cliente con campi nome email e categoria(gold/silver/bronze) e metodo descrizione che restituisce una stringa con
# cliente fulvio bianchi (gold) - fulvio@gmail

from cliente import Cliente, ClienteRecord

c2= Cliente ("mario","mario@gmail.com", "Gold")



c1= ClienteRecord("Mario ROssi", "mariorossi@gmail.com", "Gold")
p3 = prodotti.ProdottoRecord("Laptop", 1200.0)
p4 = prodotti.ProdottoRecord("Mouse", 20)

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