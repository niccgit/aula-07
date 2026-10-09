produto = "Mouse Gamer Wifi".lower()
# Se você digitar -> if produto = "Mouse", isso entregará "Falso", pois a informação da variável não está exatamente igual

if "mouse" in produto.lower():
    print("Produto encontrado!")
else:
    print("Produto não encontrado...")