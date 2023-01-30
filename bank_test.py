import pytest

class Bank:
    def __init__(self):
        self.amount = 0
    def add_money(self, money):
        self.amount += money
    def withdraw_money(self, money):
        if money > self.amount:
            raise NotEnoughCash('Nie mam tyle w kasie')
        self.amount -= money
        return money
class NotEnoughCash(Exception):
    pass

class TestBank:
    def test_create_bank(self):
        bank = Bank()
        assert bank.amount == 0
        assert isinstance(bank, Bank)

    def test_add_money(self):
        bank = Bank()
        bank.add_money(100)
        assert bank.amount == 100

    def test_add_money_twice(self):

        bank = Bank()
        bank.add_money(100)
        bank.add_money(100)

        assert bank.amount == 200

    def test_withdraw_money(self):
        bank = Bank()
        bank.add_money(100)

        money = bank.withdraw_money(100)
        assert bank.amount == 0
        assert money == 100

    def test_withdraw_over_amount(self):
        with pytest.raises(NotEnoughCash):
            bank = Bank()
            bank.withdraw_money(200)


