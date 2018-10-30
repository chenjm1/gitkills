class NotEnough(Exception):
    pass
class BankAccout(object):
    def __init__(self):
        self._balance=0
    def get_balance(self):
        return self._balance

    def set_balance(self,value):
        if value<0:
            raise NotEnough
        self._balance=value
    def withdraw(self,value):
        self._balance-=value
    def deposit(self,value):
        self._balance+=value
    balance=property(get_balance,set_balance)

import unittest
class testBankAccount(unittest.TestCase):

    def _get_account(self):
        return BankAccout
    def _makeone(self,*args,**kwargs):
        return self._get_account()(*args,**kwargs)

    def test_get_balance(self):
        target=self._makeone()
        self.assertEqual(target.balance,0)
    def test_withdraw(self):
        target=self._makeone()
        target.set_balance(100)
        target.withdraw(20)
        self.assertEqual(target.balance,81)
    def test_set_balance_enough(self):
        target=self._makeone()
        try:
            target.set_balance(-1)
            self.fail()
        except NotEnough:
            print('---------')


if __name__=="__main__":
    # b=BankAccout()
    # print(b.balance)
    # b.set_balance(50)
    # print(b.balance)
    unittest.main()