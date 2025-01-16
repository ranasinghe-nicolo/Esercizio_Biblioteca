utentiBiblioteca = {
    "user0":{"cognome": "user_surname0", "libriPrestati": ["libro10","libro9","libro8"]},
    "user1":{"cognome": "user_surname1", "libriPrestati": ["libro1","libro7"]},
    "user2":{"cognome": "user_surname2", "libriPrestati": ["libro2"]},
    "user3":{"cognome": "user_surname3", "libriPrestati": []},
}


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
