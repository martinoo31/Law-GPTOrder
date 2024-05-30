# Law&GPTOrder

Questo programma permette di allenarti al meglio per l'esame di Diritto di Ingegneria Informatica.

Si premette che le domande sono state generate automaticamente in base alla teoria del corso. Nessuna domanda è stata reperita da qualche prova di esame.

Ci sono due metodi di invocazione del programma che permettono di esercitarsi in maniera differente:
- generazione delle domande di un intero capitolo
- generazione delle domande su un argomento specifico di un capitolo

## Per scaricare
```
git clone https://github.com/martinoo31/Law-GPTOrder
```
## Per allenarti su un argomento specifico
```
python3 claudia.py NomeCartellaCapitolo/NomeFileArgomento.json
```
## Per allenarti su tutte le domande di una cartella
```
python3 claudia.py NomeCartellaCapitolo
```

## Formato JSON delle domande
```
[
  {
    "domanda": "Quale delle seguenti città è conosciuta come la Città Eterna?",
    "scelte": [
      "Atene, famosa per la sua antica Acropoli",
      "Roma, con la sua storia millenaria e i monumenti antichi",
      "Parigi, la città delle luci e dell'amore",
      "Londra, con il suo Big Ben e il Palazzo di Buckingham",
      "Berlino, rinomata per la sua Porta di Brandeburgo"
    ],
    "corretta": 1,
    "spiegazione": "Roma è conosciuta come la Città Eterna per la sua storia millenaria e i numerosi monumenti antichi."
  }
]
```
