class Product: 
    def __init__(
            self,
            name,
            make, 
            price, 
            desc, 
            ) -> None:
        self.name = name
        self.make = make
        self.price = price
        self.desc = desc
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_info(self):
        return f'{self.name} {self.price}'

class SaleProduct(Product):

    def __init__(self, name, make, price, desc, old_price) -> None:
        self.old_price = old_price
        super().__init__(name, make, price, desc)

p1 = Product(
    "MacBook M3 Pro", 
    "Apple", 
    "3200",
    "bla bla bla"
) 

p2 = SaleProduct(
    "Macbook M3 Air",
    "Apple", 
    "1000",
    "bla bla bla",
    "1200"
)

print(p1, p2)