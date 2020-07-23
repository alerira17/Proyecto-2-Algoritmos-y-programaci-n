

#Clase abstracta 
class Menu_Item:
    def __init__(self,name,price):
        self.name=name      
        self.price=price

    def show_item(self):
        return(f'''
        {self.name}
        {self.price}
        ''')                  

#Los objetos de clase Dish, Drink y Combo se veran especificados como tal en los dos menus de cada crucero
class Dish(Menu_Item):
    kind="Dish"
    def __init__(self, name, type, price):
        super().__init__(name, price)
        self.type=type
    
    def show_item(self):
        return {"name":f'{self.name}',"kind":f'{self.kind}',"type":f'{self.type}',"price":f'{self.price}'}    
        
class Drink(Menu_Item):
    kind="Drink"
    def __init__(self, name, size, price):
        super().__init__(name, price)
        self.size=size
    
    def show_item(self):
        return {"name":f'{self.name}',"kind":f'{self.kind}',"size":f'{self.size}',"price":f'{self.price}'}     

class Combo(Menu_Item):
    def __init__(self, name, products, price):
        super().__init__(name, price)
        self.products=products

    def show_item(self):
        return {"name":f'{self.name}',"products":f'{self.products}',"price":f'{self.price}'}   

#Funciones que permiten al usuario especificar todas las caracteristicas de cada nuevo item y agregar dicho item a su respectivo menu
def add_to_menu():


    new_name=input("Ingrese el nombre del nuevo elemento: ")
    new_price=input("Ingrese el precio del nuevo item: ")
    new_kind=input('''
    Seleccione el tipo: (Ingrese el numero correspondiente)
    
    1. Plato
    2. Bebida
    ''')
    if new_kind=="1":
        new_type=input('''
        Escoja el tipo de plato:
        
        1. Empaquetado
        2. Hecho a bordo
        ''')
        if new_type=="1":
            new_dish=Dish(f'{new_name}',"Empaquetado",f'{new_price}')
            return new_dish


        elif new_type=="2":
            new_dish=Dish(f'{new_name}',"hecho a bordo",f'{new_price}')
            return new_dish
        else:
            print('''
            Opcion no valida! Intente de nuevo
            ''')
               

    elif new_kind=="2":
        new_size=input('''
        Indique el tamano de la bebida:
        
        1. Small
        2. Medium
        3. Big
        ''')
        if new_size=="1":
            new_drink=Drink(f'{new_name}',"Small",f'{new_price}')
            return new_drink
            

        elif new_size=="2":
            new_drink=Drink(f'{new_name}',"Medium",f'{new_price}')
            return new_drink
            

        elif new_size=="3":
            new_drink=Drink(f'{new_name}',"Big",f'{new_price}')
            return new_drink
        else:
            print('''
            Opcion no valida! Intente de nuevo!
            ''')    
    
    else:
        print('''
        Opcion no valida! Intente de nuevo
        ''')
        


def add_to_combo():

    new_name=input("Ingrese el nombre del nuevo combo: ")
    new_price=input("Ingrese el precio del nuevo combo: ")
    new_combo=Combo(f'{new_name}',f'{new_name}',f'{new_price}')
    
    return new_combo






    














