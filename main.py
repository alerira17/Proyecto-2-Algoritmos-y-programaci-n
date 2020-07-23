from cruiseships import Cruiseship,create_cruises,show_attributes
from restaurant import Dish,Drink,Combo,add_to_menu,add_to_combo
from tours import Tour,Destination,generate_tours

#Funcion que llama a otra funcion que genera los 4 cruceros y muestra todos los atributos (Nombre, fecha de salida, ruta y habitaciones)
def cruiseships():
    
    option=input(f'''
    En Saman Caribbean contamos con 4 hermosas joyas que recorren los rincones mas hermosos del Caribe
    
    Ingresa el numero correspondiente para ver mas informacion sobre ese crucero:
    
    1. El Dios de Los Mares
    2. La Reina Isabel
    3. El Libertador del Oceano
    4. Sabas Nieves

    5. Volver a menu
    
    ''')
    
    if option=="1" or option=="2" or option=="3" or option=="4":
        cruise=create_cruises(option)
        print(show_attributes(cruise))
        cruiseships()

    elif option=="5":
        main()

    else:
        print('''
        Opcion no valida, intente de nuevo''')
        cruiseships()        

#Permite ver el menu de los 4 cruceros y que, de querer realizar modificaciones, llama a la funcion que le permite al usuario agregar o eliminar items del menu
def menu_options(menu,combos):
    
    
    count=0
    count_2=0

    print(f'''
        El menu de este crucero es el siguiente:
        ''')
    for item in menu:
        count+=1
        if item["kind"]=="Drink":
            print(f'''
           {count}. {item["name"]}| {item["kind"]}| {item["size"]} | {float(item["price"])*1.16}$ (Incluye IVA)
            ''')
        elif item["kind"]=="Dish":
            print(f'''
           {count}. {item["name"]}| {item["kind"]}| {item["type"]} | {float(item["price"])*1.16}$ (Incluye IVA)
            ''')
    print('''
    Combos disponibles:''')
    for item in combos:
        count_2+=1
        print(f'''
        {count_2}. {item["name"]}| Productos: {item["products"]} | {float(item["price"])*1.16}$ (Incluye IVA)
        ''')

    option=input('''
    Que desea hacerle al menu?
    Ingrese el numero correspondiente

    1. Agregar item
    2. Eliminar item
    
    3. Volver a gestion de restaurantes
    ''')
    if option=="1":
        option_2=input('''
        A cual menu?
        Ingrese el numero correspondiente:
        
        1. Menu regular
        2. Combos 
        ''')
        if option_2=="1":
            new_item=add_to_menu()
            menu.append(new_item.show_item())
            print('''

            Plato anadido exitosamente!
            ''')
            menu_options(menu,combos)

        elif option_2=="2":
            new_combo=add_to_combo()
            combos.append(new_combo.show_item())
            print('''

            Combo anadido exitosamente!
            ''')
            menu_options(menu,combos)
        
    


    elif option=="2":
        option_2=input('''
        A cual menu?
        Ingrese el numero correspondiente:
        
        1. Menu regular
        2. Combos

        ''')
        if option_2=="1":
            choose_item=int(input('''
            Ingrese el numero del item que desea eliminar como aparece en el menu: 
            '''))
            menu.pop(choose_item-1)
            print('''
            Item eliminado exitosamente!
            ''')
            menu_options(menu,combos)

        elif option_2=="2":
            choose_combo=int(input('''
            Ingrese el numero del combo que desea eliminar como aparece en el menu: 
            '''))
            combos.pop(choose_combo-1)
            print('''
            Combo eliminado exitosamente!
            ''')
            menu_options(menu,combos)    
    
    elif option=="3":
        restaurant()
    
    else:
        print('''
        Opcion no valida! Intente de nuevo!
        ''')
        menu_options(menu,combos)


#Menu principal que dirige al usuario al menu de alguno de los 4 cruceros
def restaurant():
    
    
    option=input('''
    Bienvenido al sistema de gestion de restaurantes de cruceros Saman Caribbean!
    Seleccione un crucero para administrar su respectivo restaurante:
    
    Ingrese el numero correspondiente:
    
    1. El Dios de los Mares
    2. La Reina Isabel
    3. El Libertador del Oceano
    4. Sabas Nieves

    5. Volver al menu principal
    
    ''')

    if option=="1" or option=="2" or option=="3" or option=="4":
        cruise=create_cruises(option)
        menus=cruise.create_full_menu()
        menu_options(menus[0],menus[1])
        

    elif option=="5":
        main()
    else:
        print('''
        Opcion no valida! Intente de nuevo!
        ''')
        restaurant()                    

#Funcion que permite a los usuarios ver todos los destinos de su crucero y los correspondientes tours de cada uno de dichos destinos    
def tours():
    option=input('''
    
    Bienvenido a Saman Caribbean Tours!
    Ofrecemos los mejores tours en cada uno de nuestros destinos para que tu experiencia sea inolvidable!
    
    Escoge tu crucero para ver los tours disponibles!
    
    1. El Dios de los Mares
    2. La Reina Isabel
    3. El Libertador del Oceano
    4. Sabas Nieves

    5. Volver a menu principal
    
    Ingresa el numero correspondiente:
    
    ''')
    if option=="1" or option=="2" or option=="3" or option=="4":
        cruise=create_cruises(option)        
        destinations=cruise.route
        destinations.pop(0)
        destinations.pop(-1)
        all_tours=generate_tours()
        list_full_destination_objects=[]
        count=0
        print(f'''
        {cruise.name} ofrece tours en los siguientes destinos: ''')
        for harbor in destinations:
            count+=1
            full_destination=Destination(f'{harbor}',all_tours[0],all_tours[1],all_tours[2],all_tours[3])
            list_full_destination_objects.append(full_destination)
            print(f'''
            {count}. {harbor}
            ''')
        option_2=input('''
        En cual destino deseas reservar un tour?
        Ingresa el numero correspondiente: 
        
        ''')
        if option_2=="1":
           harbor=list_full_destination_objects[0]
           harbor.show_tours()
           tours()
        elif option_2=="2":
           harbor=list_full_destination_objects[1]
           harbor.show_tours()
           tours()
        elif option_2=="3":
           harbor=list_full_destination_objects[2]
           harbor.show_tours()
           tours()
        elif option_2=="4":
           harbor=list_full_destination_objects[3]
           harbor.show_tours()
           tours()
        else:
            print('''
            Opcion no valida! Intente de nuevo!
            ''')
            tours()   
    
    elif option=="5":
        main()
    else:
        print('''
        Opcion no valida! Intente de nuevo!
        ''')       
        tours()

def rooms():
    print('''
    Lo lamentamos! Ya estan reservados todos las camarotes para los barcos zarpando esta semana! 
    Vuelve pronto!
    ''')    
       

def main():
    option=input('''
    Hola! Bienvenido a Saman Caribbean!
    Que deseas hacer? (Ingresa el numero correspondiente)

    1. Ver cruceros
    2. Ver habitaciones
    3. Ver tours
    4. Gestionar restaurante
    
    5. Salir
    
    ''')

    if option=="1":
        cruiseships()

    elif option=="2":
        rooms()

    elif option=="3":
        tours()

    elif option=="4":
        restaurant()

    elif option=="5":
        print('''
        Hasta luego! Nos vemos en el Caribe!
        ''')
    else:
        print('''
        Opcion no valida! Intente de nuevo!
        ''')
        main()          


main()    