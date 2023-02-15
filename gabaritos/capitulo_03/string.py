# Declare uma variável do tipo string
texto = "Estou estudando Python no 'LinkedIn Learning'"

# Imprima apenas os primeiros 3 caracteres da sua string
print(texto[:4])

# Converta toda a string para letras minúsculas
texto.lower()

# Converta toda a string para letras maiúscilas
texto.upper()

# Formate a string para que tenha apenas a primeira letra maiúscula
texto.title()

# Formate a string para que a primeira letra de cada palavra seja maiúscula
texto.capitalize()

# Inverta o case de todas as letras da string
texto.swapcase()

# Formate uma string usando string format

a = 10
b = 3

print('A divisão de {} por {} é {:.3f}'.format(a, b, a/b))