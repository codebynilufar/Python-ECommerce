import json
import os

DATA_PATH = "database/users.json"

class User:
    def __init__(self, username, password, phone, first_name, last_name, age, gender):
        self.username = username
        self.password = password
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "phone": self.phone,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "gender": self.gender
        }

    @classmethod
    def load_users(cls):
        if not os.path.exists(DATA_PATH):
            return []
        with open(DATA_PATH, "r") as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                return []

    @classmethod
    def save_users(cls, users):
        with open(DATA_PATH, "w") as file:
            json.dump(users, file, indent=4)

    @classmethod
    def create_user(cls):
        username = input("Username: ")
        password = input("Password: ")
        confirm = input("Confirm Password: ")

        if password != confirm:
            print("Parollar mos emas.")
            return

        phone = input("Phone: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = input("Age: ")
        gender = input("Gender: ")

        user = cls(username, password, phone, first_name, last_name, age, gender)
        users = cls.load_users()

        for u in users:
            if u["username"] == username:
                print("Bu username allaqachon mavjud.")
                return

        users.append(user.to_dict())
        cls.save_users(users)
        print("Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi.")

    @classmethod
    def login(cls, username, password):
        users = cls.load_users()
        for u in users:
            if u["username"] == username and u["password"] == password:
                return cls(**u)
        return None
