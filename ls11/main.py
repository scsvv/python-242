from uuid import uuid4

class Category:
    
    def __init__(
            self, 
            category_name, 
            description, 
            products_list
                 ) -> None:
        self.category_name = category_name
        self.description = description
        self.products_list = products_list

    def add_product(self, make, model, price, year):
        self.products_list.append(Product(make, model, price, year, self.category_name))

    def display(self):
        for el in self.products_list:
            print(el)

class Product:

    def __init__(
            self,
            make, 
            model, 
            price, 
            year, 
            category, 
            ) -> None:
        self.id = uuid4()
        self.make = make
        self.model = model
        self.year = year  
        self.price = price
        self.category = category
    
    def __str__(self) -> str:
        return f'{self.model}'

phones = Category('phones', '', [])
notebooks = Category('notebooks', '', [])

phones.add_product(
    "Samsung", 
    "A35",
    400,
    2024
)

notebooks.add_product(
    "Apple", 
    "MacBook",
    3300,
    2023
)

phones.display()