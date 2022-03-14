from turtle import speed


class Car(object):
    def __init__(self, model, color, company, speedLimit) -> None:
        self.color = color
        self.company = company
        self.speedLimit = speedLimit
        self.model = model

    def start(self):
        print("started")
    
    def stop(self):
        print("stopped")
    
    def accellerate(self):
        print("accelerating.....")
    
    def change_gear(self, gearType):
        print("changed gear.....")

wmb = Car("B5", "neon-purple", "XarYZ", "420")