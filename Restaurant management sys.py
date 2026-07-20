from restaurant import Restaurant
from customer import Customer

restaurant = Restaurant()

while True:

    print("\n========== RESTAURANT MANAGEMENT SYSTEM ==========")
    print("1. Display Menu")
    print("2. Display Customers")
    print("3. Display Employees")
    print("4. Search Customer")
    print("5. Add Customer")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        restaurant.display_menu()

    elif choice == "2":

        restaurant.display_customers()

    elif choice == "3":

        restaurant.display_employees()

    elif choice == "4":

        customer_id = input("Enter Customer ID: ")

        customer = restaurant.search_customer(customer_id)

        if customer:
            customer.display()
        else:
            print("Customer not found.")

    elif choice == "5":

        customer_id = input("Enter Customer ID: ")
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        address = input("Enter Address: ")

        customer = Customer(
            customer_id,
            name,
            phone,
            address
        )

        restaurant.add_customer(customer)

        restaurant.save_customers()

    elif choice == "6":

        restaurant.save_all()

        print("Thank You!")

        break

    else:

        print("Invalid Choice.")

            import pandas as pd

    from menu import Menu
    from menu_item import MenuItem
    from customer import Customer
    from chef import Chef
    from waiter import Waiter
    from cashier import Cashier


    class Restaurant:

        def __init__(self):

            self.menu = Menu()
            self.customers = []
            self.employees = []
            self.orders = []
            self.payments = []

            self.load_menu()
            self.load_customers()
            self.load_employees()

        def load_menu(self):

            df = pd.read_csv("menu.csv")

            for index, row in df.iterrows():

                item = MenuItem(
                    row["Item_ID"],
                    row["Item_Name"],
                    row["Category"],
                    row["Price"],
                    row["Available"]
                )

                self.menu.add_item(item)

        def load_customers(self):

            df = pd.read_csv("customers.csv")

            for index, row in df.iterrows():

                customer = Customer(
                    row["Customer_ID"],
                    row["Name"],
                    row["Phone"],
                    row["Address"]
                )

                self.customers.append(customer)

        def load_employees(self):

            df = pd.read_csv("employees.csv")

            for index, row in df.iterrows():

                if row["Role"] == "Chef":

                    employee = Chef(
                        row["Employee_ID"],
                        row["Name"],
                        row["Phone"],
                        row["Salary"]
                    )

                elif row["Role"] == "Waiter":

                    employee = Waiter(
                        row["Employee_ID"],
                        row["Name"],
                        row["Phone"],
                        row["Salary"]
                    )

                elif row["Role"] == "Cashier":

                    employee = Cashier(
                        row["Employee_ID"],
                        row["Name"],
                        row["Phone"],
                        row["Salary"]
                    )

                self.employees.append(employee)

        def display_menu(self):
            self.menu.display_menu()

        def display_customers(self):

            if len(self.customers) == 0:
                print("No customers found.")
                return

            for customer in self.customers:
                customer.display()
                print()

        def display_employees(self):

            if len(self.employees) == 0:
                print("No employees found.")
                return

            for employee in self.employees:
                employee.display()
                print()

        def search_customer(self, customer_id):

            for customer in self.customers:
                if customer.get_customer_id() == customer_id:
                    return customer

            return None

        def search_menu_item(self, item_id):
            return self.menu.search_item(item_id)

        def add_customer(self, customer):

            if self.search_customer(customer.get_customer_id()) is not None:
                print("Customer already exists.")
                return

            self.customers.append(customer)
            print("Customer added successfully.")

        def place_order(self, order):

            self.orders.append(order)

            print("Order placed successfully.")
            print("Total Bill : Rs.", order.get_total())

        def update_order_status(self, order_id, status):

            for order in self.orders:

                if order.get_order_id() == order_id:

                    order.set_status(status)

                    print("Order status updated successfully.")
                    return

            print("Order not found.")

        def save_customers(self):

            data = []

            for customer in self.customers:

                data.append({
                    "Customer_ID": customer.get_customer_id(),
                    "Name": customer.get_name(),
                    "Phone": customer.get_phone(),
                    "Address": customer.get_address()
                })

            df = pd.DataFrame(data)
            df.to_csv("customers.csv", index=False)

        def save_orders(self):

            data = []

            for order in self.orders:

                waiter_id = ""

                data.append({
                    "Order_ID": order.get_order_id(),
                    "Customer_ID": order.get_customer().get_customer_id(),
                    "Waiter_ID": waiter_id,
                    "Status": order.get_status(),
                    "Total": order.get_total()
                })

            df = pd.DataFrame(data)
            df.to_csv("orders.csv", index=False)

        def save_order_items(self):

            data = []

            for order in self.orders:

                for item in order.get_order_items():

                    data.append({
                        "Order_ID": order.get_order_id(),
                        "Item_ID": item.get_menu_item().get_item_id(),
                        "Quantity": item.get_quantity(),
                        "Subtotal": item.get_subtotal()
                    })

            df = pd.DataFrame(data)
            df.to_csv("order_items.csv", index=False)

        def save_payments(self):

            data = []

            for payment in self.payments:

                data.append({
                    "Payment_ID": payment.get_payment_id(),
                    "Order_ID": payment.get_order_id(),
                    "Amount": payment.get_amount(),
                    "Method": payment.get_method(),
                    "Status": payment.get_status()
                })

            df = pd.DataFrame(data)
            df.to_csv("payments.csv", index=False)

        def add_payment(self, payment):

            self.payments.append(payment)

            print("Payment recorded successfully.")

        def save_all(self):

            self.save_customers()
            self.save_orders()
            self.save_order_items()
            self.save_payments()

            print("All data saved successfully.")

            from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, employee_id, name, phone, salary):

        self.__employee_id = employee_id
        self.__name = name
        self.__phone = phone
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_salary(self):
        return self.__salary

    def set_phone(self, phone):
        self.__phone = phone

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("Employee ID :", self.__employee_id)
        print("Name :", self.__name)
        print("Phone :", self.__phone)
        print("Salary :", self.__salary)

    @abstractmethod
    def perform_duty(self):
        pass

    from employee import Employee


class Waiter(Employee):

    def __init__(self, employee_id, name, phone, salary):
        super().__init__(employee_id, name, phone, salary)

    def perform_duty(self):
        print(self.get_name(), "is serving customers.")

    def take_order(self, customer_name):
        print(self.get_name(), "is taking order from", customer_name)

    def deliver_order(self, order_id):
        print(self.get_name(), "delivered Order", order_id)

        from employee import Employee


class Cashier(Employee):

    def __init__(self, employee_id, name, phone, salary):
        super().__init__(employee_id, name, phone, salary)

    def perform_duty(self):
        print(self.get_name(), "is receiving payments.")

    def generate_bill(self, amount):
        print("Total Bill: Rs.", amount)

    def receive_payment(self, amount, method):
        print(self.get_name(), "received Rs.", amount, "via", method)

        from employee import Employee


class Chef(Employee):

    def __init__(self, employee_id, name, phone, salary):
        super().__init__(employee_id, name, phone, salary)

    def perform_duty(self):
        print(self.get_name(), "is preparing food.")

    def prepare_order(self, order_id):
        print(self.get_name(), "is preparing Order", order_id)

        class Customer:

    def __init__(self, customer_id, name, phone, address):

        self.__customer_id = customer_id
        self.__name = name
        self.__phone = phone
        self.__address = address

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_address(self, address):
        self.__address = address

    def display(self):
        print("Customer ID :", self.__customer_id)
        print("Name :", self.__name)
        print("Phone :", self.__phone)
        print("Address :", self.__address)

        from menu_item import MenuItem


class Menu:

    def __init__(self):
        self.__items = []

    def add_item(self, menu_item):
        self.__items.append(menu_item)

    def remove_item(self, item_id):
        for item in self.__items:
            if item.get_item_id() == item_id:
                self.__items.remove(item)
                print("Item removed successfully.")
                return

        print("Item not found.")

    def search_item(self, item_id):
        for item in self.__items:
            if item.get_item_id() == item_id:
                return item

        return None

    def display_menu(self):

        if len(self.__items) == 0:
            print("Menu is empty.")
            return

        print("----------- MENU -----------")

        for item in self.__items:
            item.display()
            print()

    def get_items(self):
        return self.__items
    
    class MenuItem:

    def __init__(self, item_id, item_name, category, price, available):

        self.__item_id = item_id
        self.__item_name = item_name
        self.__category = category
        self.__price = price
        self.__available = available

    def get_item_id(self):
        return self.__item_id

    def get_item_name(self):
        return self.__item_name

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def get_available(self):
        return self.__available

    def set_price(self, price):
        self.__price = price

    def set_available(self, available):
        self.__available = available

    def display(self):
        print("Item ID :", self.__item_id)
        print("Item Name :", self.__item_name)
        print("Category :", self.__category)
        print("Price : Rs.", self.__price)
        print("Available :", self.__available)

        from customer import Customer
from order_item import OrderItem


class Order:

    def __init__(self, order_id, customer):

        self.__order_id = order_id
        self.__customer = customer
        self.__order_items = []
        self.__status = "Pending"
        self.__total = 0

    def get_order_id(self):
        return self.__order_id

    def get_customer(self):
        return self.__customer

    def get_order_items(self):
        return self.__order_items

    def get_status(self):
        return self.__status

    def get_total(self):
        return self.__total

    def set_status(self, status):
        self.__status = status

    def add_item(self, order_item):
        self.__order_items.append(order_item)
        self.calculate_total()

    def calculate_total(self):
        self.__total = 0

        for item in self.__order_items:
            self.__total += item.get_subtotal()

    def display(self):
        print("Order ID :", self.__order_id)
        print("Customer :", self.__customer.get_name())
        print("Status :", self.__status)

        print("\nItems:")

        for item in self.__order_items:
            item.display()
            print()

        print("Total Bill : Rs.", self.__total)

        from menu_item import MenuItem


class OrderItem:

    def __init__(self, menu_item, quantity):

        self.__menu_item = menu_item
        self.__quantity = quantity
        self.__subtotal = menu_item.get_price() * quantity

    def get_menu_item(self):
        return self.__menu_item

    def get_quantity(self):
        return self.__quantity

    def get_subtotal(self):
        return self.__subtotal

    def set_quantity(self, quantity):
        self.__quantity = quantity
        self.__subtotal = self.__menu_item.get_price() * quantity

    def display(self):
        print("Item :", self.__menu_item.get_item_name())
        print("Quantity :", self.__quantity)
        print("Subtotal : Rs.", self.__subtotal)

        class Payment:

    def __init__(self, payment_id, order_id, amount, method, status):

        self.__payment_id = payment_id
        self.__order_id = order_id
        self.__amount = amount
        self.__method = method
        self.__status = status

    def get_payment_id(self):
        return self.__payment_id

    def get_order_id(self):
        return self.__order_id

    def get_amount(self):
        return self.__amount

    def get_method(self):
        return self.__method

    def get_status(self):
        return self.__status

    def set_method(self, method):
        self.__method = method

    def set_status(self, status):
        self.__status = status

    def make_payment(self):
        self.__status = "Paid"
        print("Payment Successful!")

    def display(self):
        print("Payment ID :", self.__payment_id)
        print("Order ID :", self.__order_id)
        print("Amount : Rs.", self.__amount)
        print("Method :", self.__method)
        print("Status :", self.__status)