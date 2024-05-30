# Law&GPTOrder

## Per scaricare
```
git clone https://github.com/martinoo31/Law-GPTOrder
```
## Per usare solo un file di domande all'interno di una cartella
```
python3 claudia.py Nomecartella/Nomedelfile.json
```
## Per usare tutte le domande di una cartella
```
python3 claudia.py Nomecartella
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
