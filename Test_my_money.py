import unittest
import my_money


class TestATM(unittest.TestCase):
    def SetUp(self):
        self.atm = my_money


    def rise_money(self):
        self.assertEquals(my_money.Atm.rise_money(1000), 11000)

    def rise_money(self):
        self.assertEquals(my_money.Atm.rise_money(0), 11000)

    def pin_code(self):
        self.assertEquals(my_money.Atm.enter_pin(777), 777)

    def pin_code(self):
        self.assertEquals(my_money.Atm.enter_pin(777), 111)
       
    def pin_code(self):
        self.assertTrue(my_money.Atm.enter_pin())

    def pin_attempts(self):
        attempts_1 = my_money.Atm.attempts(258)
        attempts_2 = my_money.Atm.attempts(333)
        self.assertEquals(my_money.Atm.attempts, 0)

       def pin_attempts(self):
        attempts_1 = my_money.Atm.attempts(258)
        attempts_2 = my_money.Atm.attempts(333)
        attempts_3 = my_money.Atm.attempts(458)
        self.assertEquals(my_money.Atm.attempts, 0)

    def get_money(self):
        self.assertEqual(my_money.Atm.get_money(10000),10000)

    def get_money(self):
        self.assertEqual(my_money.Atm.get_money(500),500)

    def get_money(self):
        self.assertEqual(my_money.Atm.get_money(10100),10000)

    def get_money(self):
        self.assertEqual(my_money.Atm.get_money(0), 0)

    def get_money(self):
        self.assertEqual(my_money.Atm.get_money(-1), -1)

    def atm_balanct(self):
        self.assertTrue(my_money.Atm.atm_balance())
