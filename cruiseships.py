import requests
from restaurant import Dish,Drink,Combo

#Clase principal para el modulo de cruceros y restaurante. Cada crucero tiene nombre, ruta, info de habitaciones y su respectivo menu
class Cruiseship:
    owner="Saman Caribbean"

    def __init__(self,name,route,departure,price,rooms,capacity,food):
        self.name=name
        self.route=route
        self.departure=departure
        self.price=price
        self.rooms=rooms
        self.capacity=capacity
        self.food=food

    def show_attributes(self):
        route=[]
        for port in self.route:
            route.append(port)
        route.pop(0)
        route.pop(-1)    
        trip=enumerate(route,1)
        print(f'''
        Orgullosos de presentarles {self.name}, saliendo de {self.route[0]} el {self.departure.split("T")[0]}
        A bordo de {self.name} conocera las siguientes joyas del Caribe:
         ''')
        
        for harbor in list(trip):
            print(f'''           {harbor[0]}. {harbor[1]}''')
        
        return (f'''
        A bordo de esta maravillosa nave usted se puede hospedar en tres tipos de hermosas habitaciones:
        
        Camarotes simples: A bordo contamos con {(self.rooms["simple"][0])*(self.rooms["simple"][1])} camarotes simples,
        cada uno con una capacidad para {self.capacity["simple"]} personas.
        El camarote simple tiene un precio de {self.price["simple"]}$ por noche
        
        Camarotes premium: A bordo contamos con {(self.rooms["premium"][0])*(self.rooms["premium"][1])} camarotes premium,
        cada uno con una capacidad para {self.capacity["premium"]} personas.
        El camarote premium tiene un precio de {self.price["premium"]}$ por noche
        
        Camarotes VIP: A bordo contamos con {(self.rooms["vip"][0])*(self.rooms["vip"][1])} camarotes VIP,
        cada uno con una capacidad para {self.capacity["vip"]} personas.
        El camarote VIP tiene un precio de {self.price["vip"]}$ por noche
        ''')

   
    def create_full_menu(self):
        full_menu=[]
        combo_menu=[]
        for item in self.food:
            if item["name"]=="Coca Cola" or item["name"]=="Ron" or item["name"]=="Cerveza":
                beverage=Drink(f'{item["name"]}',"mediano",f'{item["price"]}')
                full_menu.append(beverage.show_item())
            if item["name"]=="Hamburguesa" or item["name"]=="Pizza" or item["name"]=="Pasta" or item["name"]=="Donas" or item["name"]=="Cofuta":
                main_dish=Dish(f'{item["name"]}',"hecho a bordo",f'{item["price"]}')
                full_menu.append(main_dish.show_item())
            if "&" in item["name"]:
                food_combo=Combo(f'{item["name"]}',f'{item["name"]}',f'{item["price"]}')
                combo_menu.append(food_combo.show_item())
        
        return full_menu,combo_menu        
    
    
    
    def show_menu(self):
        cruise_menu=self.create_full_menu()[0]
        cruise_combo_menu=self.create_full_menu()[1]
        print(f'''
        El menu de {self.name} es el siguiente:
        ''')
        for item in cruise_menu:
            if item["kind"]=="Drink":
                print(f'''
                {item["name"]}| {item["kind"]}| {item["size"]} | {float(item["price"])*1.16}$ (Incluye IVA)
                ''')
            if item["kind"]=="Dish":
                print(f'''
                {item["name"]}| {item["kind"]}| {item["type"]} | {float(item["price"])*1.16}$ (Incluye IVA)
                ''')
        print('''
        Combos disponibles:''')
        for item in cruise_combo_menu:
            print(f'''
            {item["name"]}| Productos: {item["products"]} | {float(item["price"])*1.16}$ (Incluye IVA)
            ''')
                           


#Funcion que accede al API para obtener la info de cada crucero y asi poder crear los 4 objetos de clase Cruiseship
def get_info():
    url="https://saman-caribbean.vercel.app/api/cruise-ships"

    response=requests.request("GET",url)
    return response.json()

#Funcion que utiliza la info obtenida del API y retorna el objeto crucero de clase Cruiseship correspondiente para su uso en el modulo de cruceros y de restaurante
def create_cruises(option):

    data=get_info()
    cruise_1=data[0]
    cruise_2=data[1]
    cruise_3=data[2]
    cruise_4=data[3]

    king_of_the_seas=Cruiseship(cruise_1["name"],cruise_1["route"],cruise_1["departure"],cruise_1["cost"],cruise_1["rooms"],cruise_1["capacity"],cruise_1["sells"])
    queen_elizabeth=Cruiseship(cruise_2["name"],cruise_2["route"],cruise_2["departure"],cruise_2["cost"],cruise_2["rooms"],cruise_2["capacity"],cruise_2["sells"])
    sea_liberator=Cruiseship(cruise_3["name"],cruise_3["route"],cruise_3["departure"],cruise_3["cost"],cruise_3["rooms"],cruise_3["capacity"],cruise_3["sells"])
    sabas_nieves=Cruiseship(cruise_4["name"],cruise_4["route"],cruise_4["departure"],cruise_4["cost"],cruise_4["rooms"],cruise_4["capacity"],cruise_4["sells"])

    if option=="1":
        return king_of_the_seas
    if option=="2":
        return queen_elizabeth
    if option=="3":
        return sea_liberator
    if option=="4":
        return sabas_nieves

#Funcion que ayuda en el modulo de cruceros para desplegar la info de cada crucero de forma ordenada y amigable.
def show_attributes(cruise):
    return cruise.show_attributes()



