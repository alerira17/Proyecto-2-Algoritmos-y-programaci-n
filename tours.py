#Cada uno de los tours ofrecidos en cada puerto sera de clase Tour. Cada uno tiene nombre, precio, hora y sus respectivas limitaciones de cupo
class Tour:
    operator="Saman Caribbean Tours"

    def __init__(self,name,price,limit,capacity,time):
        self.name=name
        self.price=price
        self.limit=limit
        self.capacity=capacity
        self.time=time

    def make_reservation(self):
        print(f'''
        Apurate! Solo quedan {self.capacity} cupos disponibles!
        ''')

        id=input('''
        Ingrese el numero de su documento de identidad: 
        ''')
        amount_people=int(input('''
        Indique la cantidad de personas (Ingrese un digito): 
        '''))
        self.capacity-=amount_people
        return (f'''
        Listo! se han reservado {amount_people} cupo(s) para {self.name}

             Total: {self.price*amount_people}$

        Nos vemos a las {self.time} en el lobby del barco!
        ''')    

#Crea los cuatro tours que ofrece la compania en cada destino. Cada uno de estos tours seran los atributos de cada uno de los objetos Destination que representan a los puertos
def generate_tours():
    
    harbor_tour=Tour("Tour por el puerto",30,4,10,"7 am")
    food_tour=Tour("Degustacion local",100,2,100,"12 pm")
    jogging_tour=Tour("Trotar por el pueblo",0,0,1000,"6 am")
    historic_tour=Tour("Tour por casco historico",40,4,15,"10 am")
    return harbor_tour,food_tour,jogging_tour,historic_tour


#Cada destination tiene un nombre y sus respesctivos 4 tours, que a su vez son objetos de la clase Tour
class Destination:
    region="Caribbean"

    def __init__(self,name,harbor_tour,food_tour,jogging,historic_tour):
        self.name=name
        self.harbor_tour=harbor_tour
        self.food_tour=food_tour
        self.jogging=jogging
        self.historic_tour=historic_tour

    def show_tours(self):
        option=input(f'''
        En {self.name} ofrecemos los siguientes tours:

        1. Tour por el puerto
        2. Experiencia culinaria local
        3. Trotar por el puerto
        4. Tour por Casco Historico

        En cual deseas reservar cupo?
        ''')
        if option=="1":
            print(self.harbor_tour.make_reservation())
        if option=="2":
            print(self.food_tour.make_reservation())
        if option=="3":
            print(self.jogging.make_reservation())
        if option=="4":
            print(self.historic_tour.make_reservation())








    