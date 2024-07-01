# Serie sumatoria de n

def sumatoria(n):
    suma = 0
    l=[]
    for i in range(1,n+1):
        suma += i
        l.append(suma)
    return l


#s Serie fibonacci 
def fibonacci(n):
    a = 1
    b = 1
    l=[]
    if(n==1):
        l.append(a)
    elif(n==2):
        l.append(b)
    else:
        a,b=b,a+b
        l.append(b)
    return l
    
# s Encontrar la moda en la serie --- Elkin Reinoso
def encontrar_moda(numeros):
    if not numeros:
        return None

    frecuencia = {}
    for num in numeros:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
    
    moda = max(frecuencia, key=frecuencia.get)
    return moda

# Prueba de la función encontrar_moda
numeros = [4, 1, 2, 2, 3, 3, 4, 4, 5, 4]
moda = encontrar_moda(numeros)
print(f"La moda de la serie de números {numeros} es: {moda}")
