from html_generator import content

class ProductList: 

    def __init__(self) -> None:
        self.product_list = []

    def add_product(self, name, category, price, url=None, photo_url = ''):
        if url is None:
            url = f'{name}_{category}'
        
        for el in self.product_list: 
            if el.name == name:
                return
        
        product = Product(
            name=name,
            category=category,
            price=price,
            url=url,
            photo_url=photo_url
        )

        self.product_list.append(product)
    
    def __str__(self) -> str:
        _str = ''
        for el in self.product_list:
            _str += f'{el.name }'

        return _str
    
    def create_store(self):
        main_content = str('')

        for el in self.product_list:
            main_content += f"""<div> <a href="./{el.url}.html">{el.name}</a> - {el.price}: <button>Buy</button></div>"""

            product_page = f"""<div> <h1">{el.name}</h1> <h2>{el.price}</h2> <a href="./index.html">Go to Home</a></div>"""
            content(product_page, el.url)
        content(main_content, 'index')

class Product:

    def __init__(
            self, 
            name,
            category,
            price, 
            url,
            photo_url
            ) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.url = url
        self.photo_url = photo_url
    
    def __str__(self) -> str:
        return self.name

products = ProductList()

products.add_product(
    name="Apple", 
    category="fruits",
    price=12.2,
    url="apples", 
    photo_url=''
)

products.add_product(
    name="Banana", 
    category="fruits",
    price=16.2,
    url="banana", 
    photo_url=''
)

products.add_product(
    name="Grapefruit", 
    category="fruits",
    price=18.2,
    url="grape", 
    photo_url=''
)

print(products)
products.create_store()