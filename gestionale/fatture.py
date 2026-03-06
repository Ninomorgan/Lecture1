from datetime import date

#vendite -- fatture
from dataclasses import dataclass

from gestionale.cliente import  ClienteRecord
from gestionale.ordini import Ordine, RigaOrdine
from gestionale.prodotti import ProdottoRecord


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
        linee.extend([
            f"-"*60,
            f"Totale netto: {self.ordine.totale_netto()}",
            f"IVA: {self.ordine.totale_netto()*0.22}",
            f" TOTALe lordo: {self.ordine.totale_lordo()}"
            f"="*60]
        )
        return "\n".join(linee)

def _test_modulo():
        p1 = ProdottoRecord("Laptop",1200.0)
        p2= ProdottoRecord ("MOuse", 20.0)
        p3= ProdottoRecord ("tablet", 200)

        cliente1 = ClienteRecord("Mario Rossi", "mario.bianchi@gmail.com", "Gold")
        ordine= Ordine(righe= [
         RigaOrdine(p1,5), RigaOrdine(p2,5), RigaOrdine(p3,2)
        ], cliente=cliente1)
        fattura = Fattura(ordine, "2026", date.today())

if __name__ == "__main__":
        _test_modulo()