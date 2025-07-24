from models.user import User
from models.product import Product
from models.order import Order
from models.order_item import OrderItem
import json
import os

cart = []

def register():
    User.create_user()

def login():
    username = input("Username: ")
    password = input("Parol: ")
    user = User.login(username, password)
    if user:
        print(f"Xush kelibsiz, {username}!")
    else:
        print("Login yoki parol noto‘g‘ri.")
    return user

def after_login_menu(user):
    while True:
        print("Bosh menyu:")
        print("1. Mahsulotlarni ko‘rish")
        print("2. Savatga mahsulot qo‘shish")
        print("3. Savatni ko‘rish")
        print("4. Chiqish")

        choice = input("Tanlang (1-4): ")

        if choice == "1":
            Product.show_products()

        elif choice == "2":
            product_id = input("Mahsulot ID sini kiriting: ")
            product = Product.get_by_id(product_id)
            if product:
                cart.append(product)
                print(f"{product.name} savatga qo‘shildi.")
            else:
                print("Bunday IDdagi mahsulot topilmadi.")

        elif choice == "3":
            print("Savatingiz:")
            if not cart:
                print("Savat bo‘sh.")
            else:
                for p in cart:
                    print(f"- {p.name} - {p.price} so'm")

        elif choice == "4":
            print("Kabinetdan chiqildi.")
            break

        else:
            print("Noto‘g‘ri tanlov.")

def main_menu():
    while True:
        print("== E-Commerce dasturi ==")
        print("1. Ro‘yxatdan o‘tish")
        print("2. Login qilish")
        print("3. Chiqish")

        choice = input("Tanlang (1-3): ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()
            if user:
                after_login_menu(user)

        elif choice == "3":
            print("Dasturdan chiqildi.")
            break

        else:
            print("Noto‘g‘ri tanlov.")

if __name__ == "__main__":
    main_menu()
