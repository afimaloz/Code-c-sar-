# Initialisation 
mot = input("Ecrivez un MOT:")
nouveaumot = ""
ordre = {}

# Boucle 
for i in range(26): 
    # Exemple utilisation 3 % 26 
    i_nouvelindice = (i + 3) % 26
    c_nouvelindice = chr(i_nouvelindice + ord('a'))
    c = chr(i + ord('a'))
    ordre[c] = c_nouvelindice
    
for c in mot:
    nouveaumot = nouveaumot + ordre[c]
    
#Affiche votre mot crypté
print(nouveaumot)
