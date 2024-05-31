import json
import random
import argparse
import os

# Codici ANSI per i colori
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'
#GOLD = '\033[33m'
GOLD = '\033[38;5;136m'

def carica_domande(file_path):
    domande = []
    if os.path.isdir(file_path):
        for filename in os.listdir(file_path):
            if filename.endswith('.json'):
                full_path = os.path.join(file_path, filename)
                with open(full_path, 'r', encoding='utf-8') as file:
                    domande.extend(json.load(file))
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            domande = json.load(file)
    return domande

def porre_domanda(domanda, numero_domanda, totale_domande):
    print(f"\nDomanda {GOLD}{numero_domanda}{ENDC} di {GOLD}{totale_domande}{ENDC}")
    print(f"{BLUE}{domanda['domanda']}{ENDC}")
    for idx, scelta in enumerate(domanda['scelte']):
        print(f"{idx + 1}. {scelta}")
    
    while True:
        try:
            risposta = int(input("Inserisci il numero della tua risposta: ")) - 1
            if 0 <= risposta < len(domanda['scelte']):
                return risposta
            else:
                print("Per favore, inserisci un numero valido.")
        except ValueError:
            print("Per favore, inserisci un numero valido.")

def verifica_risposta(domanda, risposta):
    if risposta == domanda['corretta']:
        print(f"{GREEN}Risposta corretta!{ENDC}")
        if 'spiegazione' in domanda:
            print(f"Spiegazione: {domanda['spiegazione']}")
        return True
    else:
        print(f"{RED}Risposta sbagliata.{ENDC}")
        print(f"La risposta corretta era: {domanda['scelte'][domanda['corretta']]}")
        if 'spiegazione' in domanda:
            print(f"Spiegazione: {domanda['spiegazione']}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Applicazione di quiz a scelta multipla.")
    parser.add_argument('file_domande', type=str, help="Il percorso del file JSON o della cartella contenente i file JSON con le domande.")
    args = parser.parse_args()

    domande = carica_domande(args.file_domande)
    random.shuffle(domande)

    counter = 0
    counterTot = len(domande)
    
    for i, domanda in enumerate(domande):
        risposta = porre_domanda(domanda, i + 1, counterTot)
        res = verifica_risposta(domanda, risposta)
        if res:
            counter += 1

    voto = int(counter * 33 / counterTot)
    if voto > 30:
        voto = "30L"
    
    print(f"\n-----------------------------------------------")
    print(f"\nHai risposto correttamente a {GOLD}{counter} domande su {counterTot}.{ENDC}")
    print(f"Il tuo punteggio è del{GOLD} {counter / counterTot * 100:.2f}%.{ENDC}")
    print(f"All'esame il tuo voto sarebbe: {GOLD}{voto}{ENDC}")
    print(f"Grazie per aver partecipato al quiz!")
    print(f"\n-----------------------------------------------\n")

if __name__ == "__main__":
    main()
