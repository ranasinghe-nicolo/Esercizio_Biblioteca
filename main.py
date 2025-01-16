## Imports da file esterni
from datetime import datetime # importa funzione per data e tempo
from libriBiblioteca import aggiungiLibro, rimuoviLibro, cercaLibro, prendiInPrestito, restituisciLibro # importa funzioni per libro 
from userBiblioteca import aggiungiUtente, rimuoviUtente, cercaUtente # importa funzioni per utente

#################################################################### console output and input UI ##########################################################################

print(" \n\n                             Biblioteca SAMBA \n\n")  ## Titolo della console
while True: 
    try:
        userInput = int(input("|| Cosa vuoi fare? \n Premi digita un numero che corrisponde all'azione che vuoi svolgere \n   1: Aggiungi un libro \n   2: Rimuovi Libro \n   3: Cerca Libro \n   4: Prendi in prestito un libro \n   5: Restituisci un libro \n   6: Esci dal programma \n :"  ))
        try:
            if userInput >= 1 and userInput <= 6: # Se l'input è compreso tra 1 e 6 type error log
                if userInput == 1: ## Console Aggiungi  libro
                    print(" Hai scelto di aggiungere un libro")
                    titolo = input("Inserisci il titolo del libro: ")
                    autore = input("Inserisci l'autore del libro: ")
                    annoPubblicazione = input("Inserisci l'anno di pubblicazione del libro: ")
                    log = aggiungiLibro(titolo,autore,annoPubblicazione)
                    print(log) # log stampato

                elif userInput == 2:  ## Console Rimuovere  libro
                    print(" Hai scelto di rimuovere un libro")
                    titolo = input("Inserisci il titolo del libro: ")
                    log = rimuoviLibro(titolo)
                    print(log) # log stampato

                elif userInput == 3: ## Console Cerca libro
                    print(" Hai scelto di cercare un libro")
                    titolo = input("Inserisci il titolo del libro da cercare: ")
                    log = cercaLibro(titolo)
                    print("\n",log,"\n") # log stampato

                elif userInput == 4: ## Console Prendi in prestito un libro
                    print(" Hai scelto di prendere in prestito un libro")
                    titolo = input("Inserisci il titolo del libro da prendere in prestito: ")
                    log = prendiInPrestito(titolo)
                    print("\n",log,"\n")  # log stampato

                elif userInput == 5: ## Console Restituisci un libro
                    print(" Hai scelto di restituire un libro")
                    titolo = input("Inserisci il titolo del libro da restituire: ")
                    log = restituisciLibro(titolo)
                    print("\n",log,"\n") # log stampato

                elif userInput == 6: ## Console Esci dal programma
                    exit = input(" Sei sicuro di  voler uscire dal programma? \n s/n : ")
                    if exit == "s": ## Conferma se l'utente vuole uscire dal programma
                        print(" !Sei uscito dal programma! \n \n               Grazie per aver usato il nostro programma !!") # log stampato
                        break 
                    elif exit == "n":
                        print(" !Hai scelto di non uscire dal programma!\n") # log stampato
                        continue
                    else:
                        continue
            else:
               print(" Log: Hai inserito un numero non valido solo interi compresi fra 1 e 6") # ERROR LOG se l'utente inserisce un numero non valido che è fuori range
               continue
        except: 
            print("\n Log: ATTENZIONE !! Hai inserito un valore non intero") # ERROR LOG se l'utente inserisce un numero non intero
    except ValueError:
        print("\n Log: ATTENZIONE !! Hai inserito un valore non intero") # ERROR LOG se l'utente inserisce un numero non intero
           
 

############################################################ Fine console output and input UI ##########################################################################




