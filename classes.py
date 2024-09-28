import time

class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)    
        
flight = Flight(3)

people = ['Harry', 'Ron', 'Destine', 'Abu']
for person in people:
    print('----------------------------------------------')
    time.sleep(1)
    if flight.add_passenger(person):
        print(f"Added {person} to flight sucessfully.")
    else:
        print(f"No available seats for {person}")