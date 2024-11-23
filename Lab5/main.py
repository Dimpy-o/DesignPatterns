import hashlib


class CreditCard:
    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = self.encrypt(cvv)

    def encrypt(self, value):
        return hashlib.sha256(value.encode()).hexdigest()

    def decrypt(self, value):
        return self._cvv == hashlib.sha256(value.encode()).hexdigest()

    @property
    def cvv(self):
        return "Захищено"

    @cvv.setter
    def cvv(self, value):
        self._cvv = self.encrypt(value)

    def give_details(self):
        return {
            "client": self.client,
            "account_number": self.account_number,
            "credit_limit": self.credit_limit,
            "grace_period": self.grace_period,
            "cvv": "Захищено"
        }


class BankInfo:
    def __init__(self, bank_name, holder_name, accounts_number, credit_history=None):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = accounts_number
        self.credit_history = credit_history or {}

    def transaction_list(self, account_number):
        return self.credit_history.get(account_number, [])


class BankCustomer:
    def __init__(self, personal_info, bank_details):
        self.personal_info = personal_info
        self.bank_details = bank_details

    def give_details(self):
        return {
            "personal_info": self.personal_info,
            "bank_details": {
                "bank_name": self.bank_details.bank_name,
                "holder_name": self.bank_details.holder_name,
                "accounts_number": self.bank_details.accounts_number,
                "transaction_list": {
                    acc: self.bank_details.transaction_list(acc) for acc in self.bank_details.accounts_number
                }
            }
        }

class GoldenCreditCard(CreditCard):
    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        super().__init__(client, account_number, credit_limit, grace_period, cvv)
        self.bonus_points = 0

    def earn_points(self, amount):
        self.bonus_points += amount // 10


class VIPCustomer(BankCustomer):
    def __init__(self, personal_info, bank_details, vip_level):
        super().__init__(personal_info, bank_details)  # Call parent class __init__
        self.vip_level = vip_level

    def give_details(self):
        details = super().give_details()  # Call parent class method
        details["vip_level"] = self.vip_level
        return details


if __name__ == "__main__":
    card = CreditCard("John Doe", "123456789", 5000.0, 30, "123")
    print("CreditCard Details:", card.give_details())

    print("CVV correct:", card.decrypt("123"))

    bank_info = BankInfo("National Bank", "John Doe", ["123456789"], {"123456789": ["Purchase: $50", "ATM Withdrawal: $200"]})

    customer = BankCustomer(personal_info={"name": "John Doe", "age": 30}, bank_details=bank_info)

    print("BankCustomer Details:", customer.give_details())

    golden_card = GoldenCreditCard("John Doe", "123456789", 10000.0, 60, "123")
    golden_card.earn_points(500)
    print("GoldenCreditCard Details:", golden_card.give_details())
    print("Bonus points:", golden_card.bonus_points)

    vip_customer = VIPCustomer({"name": "Alice", "age": 45}, bank_info, "Platinum")
    print("VIPCustomer Details:", vip_customer.give_details())
