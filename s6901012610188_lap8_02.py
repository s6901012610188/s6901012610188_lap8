class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
    def show(self):
        print("Name :",self.name)
        print("Price :",self.price)
        print("Quantity :",self.quantity)

def read_products(filename):
    products = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            name, price, quantity = line.split(",")
            products.append(Product(name, price, quantity))
    return products
def most_value():
    i = 0
    s = 0
    most_value = 0
    while i < len(products):
        value = products[i].price * products[i].quantity
        if value > most_value:
            most_value = value
            s = i
        i += 1
    return most_value,s

products = read_products("product_data.txt")
most_value,item = most_value()
print(f"Most valuable product value is {products[item].name} {most_value} THB")