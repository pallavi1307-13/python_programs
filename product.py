class Product:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def display_info(self):
        print(f"product name: {self.name}, colour: {self.colour}")
class laptop(Product):
    pass
my_laptop = laptop('hp','blue')
my_laptop.display_info()


