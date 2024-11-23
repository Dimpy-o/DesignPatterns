class Customer:
    def __init__(self, ID, name, age, operator, bill, limiting_amount):
        self.ID = ID
        self.name = name
        self.age = age
        self.operator = operator
        self.bill = bill
        self.limiting_amount = limiting_amount

    def talk(self, minute, other):
        cost = self.operator.calculate_talking_cost(minute, self)
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} talked with {other.name} for {minute} minutes.")
        else:
            print("Action denied due to bill limit.")

    def message(self, quantity, other):
        cost = self.operator.calculate_message_cost(quantity, self, other)
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} sent {quantity} messages to {other.name}.")
        else:
            print("Action denied due to bill limit.")

    def connection(self, amount):
        cost = self.operator.calculate_network_cost(amount)
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} used {amount} MB data.")
        else:
            print("Action denied due to bill limit.")

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_operator(self, operator):
        self.operator = operator

    def get_operator(self):
        return self.operator

    def set_bill(self, bill):
        self.bill = bill

    def get_bill(self):
        return self.bill


class Operator:
    def __init__(self, ID, talking_charge, message_cost, network_charge, discount_rate):
        self.ID = ID
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    def calculate_talking_cost(self, minute, customer):
        cost = minute * self.talking_charge
        if customer.age < 18 or customer.age > 65:
            cost *= (1 - self.discount_rate / 100)
        return cost

    def calculate_message_cost(self, quantity, customer, other):
        cost = quantity * self.message_cost
        if customer.operator == other.operator:
            cost *= (1 - self.discount_rate / 100)
        return cost

    def calculate_network_cost(self, amount):
        return amount * self.network_charge

    def set_talking_charge(self, talking_charge):
        self.talking_charge = talking_charge

    def get_talking_charge(self):
        return self.talking_charge

    def set_message_cost(self, message_cost):
        self.message_cost = message_cost

    def get_message_cost(self):
        return self.message_cost

    def set_network_charge(self, network_charge):
        self.network_charge = network_charge

    def get_network_charge(self):
        return self.network_charge

    def set_discount_rate(self, discount_rate):
        self.discount_rate = discount_rate

    def get_discount_rate(self):
        return self.discount_rate


class Bill:
    def __init__(self, limiting_amount):
        self.limiting_amount = limiting_amount
        self.current_debt = 0

    def check(self, amount):
        return self.current_debt + amount <= self.limiting_amount

    def add(self, amount):
        self.current_debt += amount

    def pay(self, amount):
        self.current_debt -= amount
        print(f"Paid {amount}₴. Remaining debt: {self.current_debt}₴")

    def change_the_limit(self, amount):
        self.limiting_amount = amount

    def get_limiting_amount(self):
        return self.limiting_amount

    def get_current_debt(self):
        return self.current_debt


if __name__ == "__main__":
    operator = Operator(0, 1.5, 0.5, 2.0, 10)
    bill = Bill(100)
    customer1 = Customer(0, "John", 30, operator, bill, 100)
    customer2 = Customer(1, "Bob", 20, operator, bill, 50)

    customer1.talk(10, customer2)
    customer1.message(5, customer2)
    customer1.connection(50)
    customer1.bill.pay(20)
