import json
import random
import argparse

# Codici ANSI per i colori
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

def carica_domande(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def porre_domanda(domanda):
    print(f"\n{BLUE}{domanda['domanda']}{ENDC}")
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
    parser.add_argument('file_domande', type=str, help="Il percorso del file JSON contenente le domande.")
    args = parser.parse_args()

    domande = carica_domande(args.file_domande)
    random.shuffle(domande)
    
    for domanda in domande:
        risposta = porre_domanda(domanda)
        verifica_risposta(domanda, risposta)

if __name__ == "__main__":
    main()

