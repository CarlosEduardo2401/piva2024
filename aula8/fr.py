itens = ["Abacate", "Limão", "Tangerina", "Melancia", "Laranja da China"]
precos = [2.13, 0.19, 1.95, 0.87, 12.00]
len_precos = 10 # Coluna de precos tem 10 caracteres
# Achar a largura da coluna de itens
len_itens = len(itens[0])
for it in itens :
    len_itens = max(len_itens,len(it))
# Imprimir tabela de precos
print ("-"*(len_itens+len_precos))
print ("%-*s%*s"% (len_itens, "Item", len_precos, "Preço"))
print ("-"*(len_itens+len_precos))
for i in range(len(itens)):
     print ("%-*s%*.2f" % (len_itens, itens[i],len_precos, precos[i]))
