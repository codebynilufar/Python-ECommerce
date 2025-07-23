from models.product import Product



for product in Product.load_products():
    print(product.name, product.price)

