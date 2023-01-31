class Bus:
    def __init__(self,route_number,destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self,person):
        self.passengers.remove(person)
    
    def empty(self):
        self.passengers = []
    
    def pick_up_from_stop(self, bus_stop):
        for person_in_queue in bus_stop.queue:
            self.pick_up(person_in_queue)
        
        bus_stop.clear() 
        

        

