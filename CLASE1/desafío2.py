def mostrar_edad(nombre, edad): #agrego los parámetros que quiero trabajar, algo dinámico
    print("Hola", nombre + ", tenés", edad, "años.")
    #Las comas en print separan los elementos y 
    #los convierten automáticamente en texto. Python agrega espacios automáticamente entre ellos.
    #Es correcto porque se esta formando una sola cadena antes de imprimirla.

mostrar_edad("Lucas", 21)
mostrar_edad("Valentina", 18) 

#nombre es un string <---
# edad no es string
#El + se usa cuando se quiere unir dos strings manualmente.
#Las comas en print() ya hacen la conversión.
