import locale
def tetando_Format():
    nome = "Shakira"
    print("Ohh louco, {}").format(nome)
    #separador
    print("Ohh! louco, {} você é {}".format(nome))
    #separador
    
    print(f"Ohh louco, {nome}!")
    print(f"OHH! louco, {nome} você é {elogio}!")
    #separador

#-----------------------RECIBO---------------------------
def mostrarRecibo():
    preco_unitario = 49.95
    quantidade = 32
    taxa_de_imposto = 0.065

    subtotal = preco_unitario * quantidade
    imposto = subtotal * taxa_de_imposto
    total = subtotal + imposto

    locale.setlocale(locale.LC_MONETARY,'pt_BR.UTF-8')
    vendas_final = f"""
    Subtotal: R$ {str(locale.currency(subtotal, grouping=True)).replace("R$","")}
    Imposto:  R$ {str(locale.currency(imposto, grouping=True)).replace("R$","")}
    Total:    R$ {str(locale.currency(total, grouping=True)).replace("R$","")}
    """

    print(vendas_final)
#----------------------EXECUÇÃO--------------------------
def main():
    mostrarRecibo()

main()
