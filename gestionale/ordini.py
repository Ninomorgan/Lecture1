
#DATACLASS -> genera in modo automatico queste cose

from dataclasses import dataclass

from gestionale.cliente import ClienteRecord
from prodotti import ProdottoRecord


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





