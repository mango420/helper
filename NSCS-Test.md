## Ein link fällt aus, was verschickt OSPF nun an die Nachbarn? (Name=> drei Buchstaben und auch ausgeschrieben)

LSU - Link State Update


## Nenne den wesentlichen Vorteil von OSPF gegenüber EIGRP bzgl. der Berechnung von Backup-Routen:

OSPF unterstützt die parallele Berechnung von Backup-Routen, während EIGRP sequenzielle Berechnungen durchführt.


## Wie wird der DR ausgewählt (4 Schritte, Reihenfolge)

1. Zuerst wird ein Router ausgewählt, der die höchste Priorität für die DR-Rolle hat. Die Priorität kann konfiguriert werden und standardmäßig ist sie 1.
2. Wenn die Prioritäten gleich sind, wird der Router mit der höchsten Router-ID ausgewählt.
3. Wenn die Router-IDs auch gleich sind, wird der Router mit der höchsten IP-Adresse auf dem ausgewählten OSPF-Interface ausgewählt.
4. Der ausgewählte Router wird dann der Designated Router (DR) und der Router mit der nächsthöheren Router-ID wird der Backup Designated Router (BDR).