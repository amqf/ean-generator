import random

def generate_ean13():
    # Gerar os primeiros 12 dígitos aleatoriamente
    ean = [random.randint(0, 9) for _ in range(12)]
    
    # Calcular o dígito verificador
    soma_pares = sum(ean[i] for i in range(1, 12, 2)) * 3
    soma_impares = sum(ean[i] for i in range(0, 12, 2))
    total = soma_pares + soma_impares
    digito_verificador = (10 - (total % 10)) % 10
    ean.append(digito_verificador)
    
    return ''.join(map(str, ean))

# Gerar e exibir o código EAN-13
codigo_ean13 = generate_ean13()
print(f"Código EAN-13 gerado: {codigo_ean13}")

