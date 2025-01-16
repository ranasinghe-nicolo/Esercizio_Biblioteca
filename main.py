import libriBiblioteca


###################################################################### Dizionari #####################################################################################

############################################################### Dizionario libriBiblioteca ###########################################################################
libriBiblioteca = {
    "titolo0": {"autore": "autore0", "annoPubblicazione": "2000", "disponibile": False },
    "titolo1": {"autore": "autore1", "annoPubblicazione": "2001", "disponibile": True },
    "titolo2": {"autore": "autore2", "annoPubblicazione": "2002", "disponibile": False },
    "titolo3": {"autore": "autore3", "annoPubblicazione": "2003", "disponibile": True },
    "titolo4": {"autore": "autore4", "annoPubblicazione": "2004", "disponibile": True },
    "titolo5": {"autore": "autore5", "annoPubblicazione": "2005", "disponibile": True },
    "titolo6": {"autore": "autore6", "annoPubblicazione": "2006", "disponibile": True },
    "titolo7": {"autore": "autore7", "annoPubblicazione": "2007", "disponibile": False },
    "titolo8": {"autore": "autore8", "annoPubblicazione": "2008", "disponibile": False },
    "titolo9": {"autore": "autore9", "annoPubblicazione": "2009", "disponibile": False },
    "titolo10": {"autore": "autore10", "annoPubblicazione": "2010", "disponibile": False },
}


################################################################ Dizionario utentiBiblioteca #########################################################################
utentiBiblioteca = {
    "user0":{"cognome": "user_surname0", "libriPrestati": ["libro10","libro9","libro8"]},
    "user1":{"cognome": "user_surname1", "libriPrestati": ["libro1","libro7"]},
    "user2":{"cognome": "user_surname2", "libriPrestati": ["libro2"]},
    "user3":{"cognome": "user_surname3", "libriPrestati": []},
}

################################################################# Fine dizionari ######################################################################################



################################################################### Funzioni ##########################################################################################
##Funzione Aggiungi libro  
def aggiungiLibro (titolo,autore,anno):
    for libro in libriBiblioteca:
        if libro == titolo:
            return ("Libro già presente")
        else:
            libriBiblioteca[titolo] = {"autore": autore , "annoPubblicazione": anno , "disponibile": True}
            return ("Libro aggiunto")

##Funzione rimuovi libro
def rimuoviLibro(titolo):
    if titolo in libriBiblioteca:
        del libriBiblioteca[titolo]
        return ("Libro rimosso")
    else:
        return ("Libro non trovato")
  
##Funzione cerca libro
def cercaLibro(titolo):   
    for libro in libriBiblioteca:
        if libro == titolo:
            autore = libriBiblioteca[libro]["autore"]
            annoPubblicazione = libriBiblioteca[libro]["annoPubblicazione"]

            disponibile = libriBiblioteca[libro]["disponibile"]
            if disponibile == True:
                disponibile = "Si"
            else:
                disponibile = "No"

            return "\nLibro trovato!!\n\nAutore: " + autore + "\nAnno di pubblicazione: " + annoPubblicazione + "\nDisponibile: " + str(disponibile)
    return ("Libro non trovato!!")

##Funzione prendere in prestito un libro
def prendiInPrestito(titolo):
    if titolo in libriBiblioteca:
        if libriBiblioteca[titolo]["disponibile"] == True:
            libriBiblioteca[titolo]["disponibile"] = False
            return ("Libro prenotato")
        else:
            return ("Libro non disponibile")


##Funzione restituire un libro
def restituisciLibro(titolo):
    if titolo in libriBiblioteca:
        if libriBiblioteca[titolo]["disponibile"] == False:
            libriBiblioteca[titolo]["disponibile"] = True
            return ("Libro restituito")
        else:
            return ("Libro già disponibile")


######################################################################## Fine funzioni Libro ##############################################################################



######################################################################## Funzioni User #####################################################################################

def aggiungiUtente(cognome):
    if cognome in utentiBiblioteca:
        return ("Utente già presente")
    else:
        utentiBiblioteca[cognome] = {"cognome": cognome, "libriPrestati": []}
        return ("Utente aggiunto")
def rimuoviUtente(cognome):
    if cognome in utentiBiblioteca:
        del utentiBiblioteca[cognome]
        return ("Utente rimosso")
    else:
        return ("Utente non trovato")

def cercaUtente(cognome):
    if cognome in utentiBiblioteca:
        libriPrestati = utentiBiblioteca[cognome]["libriPrestati"]
        return ("\nUtente trovato!!\n\nLibri in prestito: " + str(libriPrestati))
    else:
        return ("Utente non trovato")



######################################################################## Fine funzioni User ################################################################################





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




