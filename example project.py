# Define the four classes  
  
class Tourist:  
    def __init__(self, name, email, phone):  
        self.name = name  
        self.email = email  
        self.phone = phone  
  
    def __str__(self):  
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"  
  
class Destination:  
    def __init__(self, name, description, location):  
        self.name = name  
        self.description = description  
        self.location = location  
  
    def __str__(self):  
        return f"Name: {self.name}, Description: {self.description}, Location: {self.location}"  
  
class TourPackage:  
    def __init__(self, name, description, destinations, price):  
        self.name = name  
        self.description = description  
        self.destinations = destinations  
        self.price = price  
  
    def __str__(self):  
        return f"Name: {self.name}, Description: {self.description}, Destinations: {[str(dest) for dest in self.destinations]}, Price: {self.price}"  
  
class TourismSystem:  
    def __init__(self):  
        self.tourists = []  
        self.destinations = []  
        self.tour_packages = []  
  
    def add_tourist(self, tourist):  
        self.tourists.append(tourist)  
  
    def add_destination(self, destination):  
        self.destinations.append(destination)  
  
    def add_tour_package(self, tour_package):  
        self.tour_packages.append(tour_package)  
  
    def list_destinations(self):  
        print("Destinations:")  
        for destination in self.destinations:  
            print(destination)  
  
    def list_tour_packages(self):  
        print("Tour Packages:")  
        for tour_package in self.tour_packages:  
            print(tour_package)  
  
    def register_tourist(self, tourist, tour_package):  
        print(f"Tourist {tourist.name} registered for {tour_package.name} tour package.")  
  
    def provide_travel_info(self, destination):  
        print(f"Travel Information for {destination.name}:")  
        print(f"Description: {destination.description}")  
        print(f"Location: {destination.location}")  
  
    def provide_guide(self, tour_package):  
        print(f"Guide for {tour_package.name} tour package:")  
        for destination in tour_package.destinations:  
            print(f"  - {destination.name}")  
  
# Create instances of the classes  
tourism_system = TourismSystem()  
  
# Add destinations  
destination1 = Destination("Paris", "The City of Light", "France")  
destination2 = Destination("Rome", "The Eternal City", "Italy")  
destination3 = Destination("Barcelona", "The Capital of Catalonia", "Spain")  
tourism_system.add_destination(destination1)  
tourism_system.add_destination(destination2)  
tourism_system.add_destination(destination3)  
  
# Add tour packages  
tour_package1 = TourPackage("European Getaway", "Explore the best of Europe", [destination1, destination2], 2000)  
tour_package2 = TourPackage("Mediterranean Cruise", "Relax on the Mediterranean coast", [destination2, destination3], 3000)  
tourism_system.add_tour_package(tour_package1)  
tourism_system.add_tour_package(tour_package2)  
  
# Add tourists  
tourist1 = Tourist("John Doe", "johndoe@example.com", "123-456-7890")  
tourist2 = Tourist("Jane Smith", "janesmith@example.com", "098-765-4321")  
tourism_system.add_tourist(tourist1)  
tourism_system.add_tourist(tourist2)  
  
# List destinations  
tourism_system.list_destinations()  
  
# List tour packages  
tourism_system.list_tour_packages()  
  
# Register tourist for a tour package  
tourism_system.register_tourist(tourist1, tour_package1)  
  
# Provide travel information  
tourism_system.provide_travel_info(destination1)  
  
# Provide guide  
tourism_system.provide_guide(tour_package1)  
