'PARCIAL 1 '
import csv
from funciones import *



def pausar():
    system("pause")

def limpiar_terminal():
    system("cls")

def menu_bicicletas()-> str:
    """Menu de opciones para obtener datos.

    Returns:
        str: Devuelve el dato de la opción elegida. 
    """
    limpiar_terminal()
    print("     Menu de opciones")
    print("A- Cargar archivos .CSV .")
    print("B- Mostrar lista de bicicletas.")
    print("C- Asignar tiempos .")
    print("D- Informar ganador")
    print("E- Filtrar por tipo de bicicleta")
    print("F- Mostrar posiciones por tipo y tiempo.")
    print("G- Guardar posiciones en JSON")
    print("H- Salir")
    
    return obtener_opcion("Ingrese una opcion:  ").lower()


def confirmar_salida(mensaje: str)-> bool:
    """Le pregunta al usuario si desea salir o no.

    Args:
        mensaje (str): Mensaje para preguntar si desea salir

    Returns:
        bool: Devuelve True si la opción es "Si"
    """
    respuesta= input(mensaje).lower()
    
    return respuesta == "si"



def es_texto(entrada)-> bool:
    """Verifica si es str

    Args:
        entrada (_type_): Valor de entrada

    Returns:
        bool: devuelve true si es str
    """
    return isinstance(entrada, str)



def obtener_opcion(mensaje):
    """Valida que la opción ingresada esté dentro de las opciones validas.

    Args:
        mensaje (_type_): mensaje para pedir el dato

    Returns:
        _type_: -
    """
    
    lista_opciones= ["a","b","c","d","e","f","g","h","i","j"]
    
    while True:
        
        entrada = input(mensaje)
        if entrada in lista_opciones:
            
            return entrada
        else:
            print("Entrada inválida. Por favor, ingrese una opción válida.")


def menu_tipos():
    
    limpiar_terminal()
    print("     Menu de tipos de bicicleta")
    print("A- BMX .")
    print("B- MTB.")
    print("C- PASEO .")
    print("D- PLAYERA")
    
    
    return obtener_opcion("Ingrese una opcion:  ").lower()




while True:
    
    match menu_bicicletas():
        
        case "a":
            
            lista_bicicletas= lista_cargada_csv()
            print("Lista cargada con exito!!")
            
        
        case "b":
            
            print(lista_bicicletas)    
            
        case "c":
            
            print("Valores asignados con Exito!")   
            print(asignar_valor_tiempo)
            
        case "d":
            
            print(f"La bicicleta ganadora es {ganador_bicicleta(lista_bicicletas, "tiempo", "nombre")}")    
            
           
            
        case "e":
            
            match menu_tipos():
                case "a":
                    tipo= "BMX"
                    print(filtrar_por_tipo(tipo))
                case "b":
                    tipo= "MTB"
                    print(filtrar_por_tipo(tipo))
                case "c":
                    tipo= "PASEO"
                    print(filtrar_por_tipo(tipo))
                case "d":
                    tipo= "PLAYERA"
                    print(filtrar_por_tipo(tipo))

            
              
        case "f":
            print(promedio_por_tipo())
            
        case "g":
            print(mostrar_posiciones)
            
        case "h":
                print("Guardado en json con exito!")
                guardar_posiciones_json()
                
   
        case "h":
            
            if confirmar_salida("Desea salir?\n "):
                break
            else:
                continue
        
    pausar()       
            
print("Fin del programa") 