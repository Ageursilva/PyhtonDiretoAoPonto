valores = [2,3,7,4,1,8,15,200,4613,46464,846134,64,98840]
desordenado = True
while desordenado:
    desordenado = False
    for i in range(len(valores)-1):
        if valores[i] > valores [i+1]:
            valores[i],valores[i+1] = valores[i+1],valores[i]
            desordenado =  True
            print(valores)