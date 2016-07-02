mot = input("Ecrivez un MOT:")
nouveaumot = ""
ordre = {}
for i in range(26): 
    i_nouvelindice = (i + 3) % 26
    c_nouvelindice = chr(i_nouvelindice + ord('a'))
    c = chr(i + ord('a'))
    ordre[c] = c_nouvelindice
for c in mot:
    nouveaumot = nouveaumot + ordre[c]
print(nouveaumot)
