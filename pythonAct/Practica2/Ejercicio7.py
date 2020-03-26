palabra=input('Ingrese palabra')
invertido=palabra[::-1]
print(invertido)
if palabra==invertido:
    print('Esta palabra es palindrome')
else:
    print('Esta palabra no es palindrome')