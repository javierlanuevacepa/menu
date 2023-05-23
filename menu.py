
#Menu con diccionario como '''''''base de datos'''''''


numerocompra=0
churrasco=1500
cantidad_chur=0 
completo=1000 
cantidad_comple=0
vegetariano=2000 
cantidad_vege=0
barros_Luco=3000
cantidad_barro=0
lop=0
lop2=0
total=0
descontadototal=0
veceslista=0
nombres = []
nombresclientes = {"Nombres" : nombres }
lop3=0
totalchurrascos=0
totalvegetarianos=0
totalbarros=0
totalcomple=0
clienteventa = {}
cosascompradas = ""
totalrecaudado=0
#{}


print("--- Bienvenido a la sanduicheria ---")

while lop==0:
    cosascompradas = ""

    lop3=0
    print("***SANDUICHERIA***")
    print("(1) Realizar Venta")
    print("(2) Ver Base de datos")
    election=input("Elige tu opcion:")
    if election not in ("1" , "2"):
        print("Elige una opcion valida! ")
    if election=="1":

        nombre=input("Ingrese el nombre del cliente: ")
        veceslista+=1
        
        nombres.insert(veceslista , nombre)
        
        lop2=0
        while lop2==0:
            print("Que pedido quiere realizar")
            print("(1) Churrasco      1.500-----------")
            print("(2) Completo       1.000-----------")
            print("(3) Vegetariano    2.000-----------") 
            print("(4) Barros luco    3.000-----------")
            print("(5) Ver total compra+imprimir------")
            print("(6) Salir del programa-------------")
            eleccion=input("Elija su eleccion: ")
            
            if eleccion not in ("1" , "2" , "3" , "4" , "5" , "6"):
                print("Ingrese un caracter valido. ")
    
            if eleccion=="1":
             
                cosascompradas=cosascompradas+"Churrasco "
                total=total+churrasco
                cantidad_chur=cantidad_chur+1
                totalchurrascos+=1
                print("Usted ordeno un churrasco. 1.500 ")
            if eleccion=="2":
                
                cosascompradas=cosascompradas+"Completo "
                total=total+completo
                cantidad_comple=cantidad_comple+1
                totalcomple+=1
                print("Usted ordeno un Completo 1.000 ")
            if eleccion=="3":
               
                cosascompradas=cosascompradas+"Vegetariano "
                total=total+vegetariano
                cantidad_vege=cantidad_vege+1
                totalvegetarianos+=1
                print("Usted ordeno un Vegetariano 2.000 ")
            if eleccion=="4":
           
                cosascompradas=cosascompradas+"Barros Luco "
                total=total+barros_Luco
                cantidad_barro=cantidad_barro+1
                totalbarros+=1
                print("Usted ordeno un Barros luco 3.000 ")
            if eleccion=="5":
                
                print("-----------El total de su compra es-----------: ", total)
                numerocompra=numerocompra+1
                if cantidad_chur>0:
                    print(f"-----------Usted ordeno {cantidad_chur} Churrascos-----------")
                if cantidad_barro>0:
                    print(f"-----------Usted ordeno {cantidad_barro} Barros luco-----------")
                if cantidad_vege>0:
                    print(f"-----------Usted ordeno {cantidad_vege} Vegetarianos----------- ")
                if cantidad_comple>0:
                    print(f"-----------Usted ordeno {cantidad_comple} Completos----------- ")
                elige=input("Desea aplicar 10% de descuento a cliente?(1)Si (2)No: ")
                if elige not in ("1" , "2"):
                    print("Elige una opcion valida !! ")
                if elige=="1":
                    totalrecaudado=totalrecaudado+descontadototal
                    descontado=total/10
                    descontadototal=total-descontado
                    
                    print("-----------El total de su compra es-----------: ", descontadototal)
                if elige=="2":
                    totalrecaudado=totalrecaudado+total
                    print("-----------El total de su compra es-----------: ", total)
                #{}
                boleta=(f"Nombre cliente:{nombre} \nChurrascos: {cantidad_chur}\nBarros luco:{cantidad_barro}\nVegatarianos:{cantidad_vege}\nCompletos:{cantidad_comple}\nTotal:{total}\nDescon:{descontadototal}")
                



                clienteventa.update({f"{nombre}" : f"{cosascompradas}"})
        
                print("Se guardaran los datos de la compra!!!!")
                with open(f'venta{numerocompra}.txt' , 'w') as file:
                    file.write(boleta)
    
                cantidad_chur=0
                cantidad_barro=0
                cantidad_vege=0
                cantidad_comple=0
                total=0
                descontadototal=0
    
                lop2=lop2+1
    

    
            if eleccion=="6":
                print("-----------Gracias por usar el sistema de ventas. !-----------")
                lop2=lop2+1
    if election=="2":
        while lop3==0:

            print("--*BASE DE DATOS SANDUICHERIA*--")
            print("(1) Ver Clientes ")
            print("(2) Clientes y sus compras ")
            print("(3) Total de hoy")
            print("(4) Volver al menu anterior ")
            eligir=input("Elige: ")
            if eligir not in ("1" , "2" , "3" , "4"):
                print("Ingresa un caracter valido ! ")
            if eligir=="1":
                print(nombresclientes["Nombres"])
            if eligir=="2":
                print("********Clientes que han comprado*******")
                print(nombresclientes)
                eligre=input("Escribe de quien quieres ver la compra: ")

                if eligre not in clienteventa:
                    print("No se a encontrado nada en la base de datos.")
                else:

                    print(clienteventa[eligre])


            if eligir=="3":
                print("Total de cosas vendidas hoy: ")
                print(f"Churrasco                 :{totalchurrascos}")
                print(f"Completo                  :{totalcomple}")
                print(f"Vegetariano               :{totalvegetarianos} ") 
                print(f"Barros luco               :{totalbarros}")
                print(f"Total de dinero recaudado :{totalrecaudado}")
            
            if eligir=="4":
                lop3+=1
                print("Volviendo al menu anterior ")
















