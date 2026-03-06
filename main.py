

from gestionale.ordini import Ordine, OrdineSconto, RigaOrdine
#METODI GETTER - SETTER
#METODI PROTOCOL
#METODI DATACLASS
#SOTTOCLASSI E INHERITANCE

#METODI PER IMPORTARE
#1) from prodotti import ProdottoScontato
#2) from prodotti import ProdottoScontato as ps --> lo chiamo ps
#3) import prodotti

#1)
from gestionale.prodotti import Prodotto, crea_prodotto_standar, ProdottoRecord

p1= Prodotto("ebook", 120.0, 1, "AAA")
p2=crea_prodotto_standar("Tablet",750)

print(p1)

#2)
from gestionale.prodotti import ProdottoScontato as ps
p3 = ps("cuffie", 230,1,"abc", 0.1)

#3)
from gestionale import prodotti

p4 = prodotti.ProdottoScontato("mp3", 230, 1, " AAA", 0.2)


# classe cliente con campi nome email e categoria(gold/silver/bronze) e metodo descrizione che restituisce una stringa con
# cliente fulvio bianchi (gold) - fulvio@gmail

from gestionale.cliente import Cliente, ClienteRecord

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



import networkx as nx   #IMPORTA LA LIBRERIA NETWORKX
