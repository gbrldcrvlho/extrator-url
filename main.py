url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# Sanitizacao da URL
url = url.strip()

# Validacao da URL
if url == "":
    raise ValueError("A URL esta vazia")

# Separa base e os parametros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
print(url_base)
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parametro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)