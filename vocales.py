def eliminar_vocales(cadena):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    resultado = ''.join([letra for letra in cadena if letra not in vocales])
    return resultado

#Pedir que el usuario digite el texto.
texto = input("Ingresa un texto: ")
texto_sin_vocales = eliminar_vocales(texto)
print(texto_sin_vocales)  # Imprimirá el texto sin vocales.
