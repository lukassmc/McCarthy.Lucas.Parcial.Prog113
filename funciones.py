from os import system
import re
from random import randint
import json

def validar_lista(lista):
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")


def getpathactual(nombre_archivo):
    import os
    
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)


def mapear_campo(campo, lista: list) -> list:
    validar_lista(lista)
    lista_retorno = []
    for el in lista :
        lista_retorno.append(campo(el))
    return lista_retorno

def mapear_dos_campos(campo1, campo2, lista: list) -> list:
    validar_lista(lista)
    lista_retorno = []
    for el in lista :
        lista_retorno.append(campo1(el))
        lista_retorno.append(campo2(el))
    return lista_retorno


def filtrar_lista(filtro, lista:list)->list:
    validar_lista(lista)
    
    lista_retorno = []
    for el in lista:
        if filtro(el):
            lista_retorno.append(el)
    return lista_retorno

def totalizar_lista(lista: list)-> int:
    validar_lista(lista)
    total= 0
    for el in lista:
        total += el
        
    return total


def calcular_promedio_lista(lista: list)-> float:
   
   
   if isinstance (lista, list):
      cant= len(lista)
      if cant == 0:
         raise ValueError("El promedio de una lista no puede ser definido.")
      promedio= totalizar_lista(lista) / cant
   
      return promedio 
      
   raise ValueError("Esto no es una lista") 

def swap_lista(lista, i: int, j: int)-> None:
         aux= lista[i]
         lista[i]= lista[j]
         lista[j]= aux


def ordenar_empleados_doble_criterio_ascendente(lista: list, campo1, campo2):
    validar_lista(lista)
    tam = len(lista)
    for i in range(0, tam-1):
        for j in range(i + 1, tam):
            
            if lista[i][campo1] == lista[j][campo1]:
                
                if lista[i][campo2] > lista[j][campo2]:
                    
                    swap_lista(lista, i, j)
                    
            elif lista[i][campo1] > lista[j][campo1]:
                
                swap_lista(lista, i, j)
    
    return lista
                

def escritor_json(path: str, lista: list):
    validar_lista(lista)
    
    with open(path, "w") as archivo:
        json.dump(lista, archivo, indent=4)
        
"------------------------------------------------- Lectura de CSV --------------------------------------------"
def lista_cargada_csv():
    lista_bicicletas= []
    with open(getpathactual("bicicletas.csv"), "r", encoding= "utf-8") as archivo:
        for linea in archivo:
            diccionario={}
            split= re.split(",|\n", linea)
            
            diccionario["id_bike"] = split[0]
            diccionario["nombre"] = split[1]
            diccionario["tipo"] = split[2]
            diccionario["tiempo"] = split[3]
            lista_bicicletas.append(diccionario)
            
    return lista_bicicletas

lista_bicicletas= lista_cargada_csv()
"---------------------------------------Mostrar lista del csv ------------------------------------"
print(lista_bicicletas)

"---------------------------------------Asignar valor de tiempo ----------------------------------"
def asignar_valor_tiempo():
    tiempo_bicicletas= mapear_campo(lambda tiempo: tiempo["tiempo"], lista_bicicletas)
    print(tiempo_bicicletas)

    for bici in range(len(lista_bicicletas)):
        valor_de_tiempo= randint(50,120)
        lista_bicicletas[bici]["tiempo"] = lista_bicicletas[bici]["tiempo"] = valor_de_tiempo
        
    print(lista_bicicletas)

"------------------------------------------------- Bicicleta ganadora  ----------------------------------------"

def ganador_bicicleta(lista: list, campo_a_comparar, campo_a_comparar_2):
    validar_lista(lista)
   
    
    menor_tiempo = lista[0]
    
    for elemento in lista:
        if float(elemento[campo_a_comparar]) <= float(menor_tiempo[campo_a_comparar]):
            menor_tiempo = elemento
            
    

    return menor_tiempo

print(ganador_bicicleta(lista_bicicletas, "tiempo", "nombre"))

print("***************************************************************************************")
print()
"------------------------------------------------------Filtrar por tipo ----------------------------------"
def filtrar_por_tipo(tipo: str):
    tipo= tipo
    tipos_bicicleta= {
        "nombre": "",
        "tipo": ""
    }
    tipos_bicicleta= mapear_dos_campos(lambda nombre: nombre["nombre"], lambda tipo: tipo["tipo"], filtrar_lista(lambda tipos: tipos["tipo"] == tipo , lista_bicicletas))
    print(tipos_bicicleta)

"------------------------------------------------------Promedio por tipo -----------------------------------"
def promedio_por_tipo():
    tipos_de_bicicleta= list(set(mapear_campo(lambda tipo: tipo["tipo"], filtrar_lista(lambda tipo_de_bici: tipo_de_bici["tipo"] != "tipo" ,lista_bicicletas))))    

    for tipo in tipos_de_bicicleta:
        
        corredores_por_tipo= filtrar_lista(lambda tipo: tipo["tipo"], filtrar_lista(lambda bicicleta: bicicleta["tipo"] == tipo , lista_bicicletas))
        tiempo= mapear_campo(lambda tiempo: tiempo["tiempo"], corredores_por_tipo)
        
        promedio= calcular_promedio_lista(tiempo)
        print(f"El promedio de tiempo del tipo {tipo} es: {round(promedio), 2} minutos")
    
"-----------------------------------------------------Mostrar posiciones ---------------------------------"
def mostrar_posiciones():
    bicicletas_ordenadas= ordenar_empleados_doble_criterio_ascendente(lista_bicicletas, "tipo", "tiempo")
    print("-------------------------------------------------------")
    print(bicicletas_ordenadas)
    return bicicletas_ordenadas

"------------------------------------------------Guardar posiciones --------------------------------------"
def guardar_posiciones_json():
    escritor_json(getpathactual("bicicletas.json"), mostrar_posiciones())
    
    