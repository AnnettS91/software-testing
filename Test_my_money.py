mport unittest
import my_money


class TestATM(unittest.TestCase):
    def SetUp(self):

    def rise_money(self):
        self.assertEquals(my_money.Atm.rise_money(1000), 11000)

    def rise_money(self):
        self.assertEquals(my_money.Atm.rise_money(0), 11000)

    def pin_code(self):
        self.assertEquals(my_money.Atm.enter_pin(777), 777)

    def pin_code(self):
        self.assertEquals(my_money.Atm.enter_pin(777), 111)
        return "Incorrect Pin!!! try again!"
    def pin_code(self):
        self.assertTrue(my_money.Atm.enter_pin())


    @smoke
    def pin_attempts(self):
        attempts_1 = my_money.Atm.attempts(258)
        attempts_2 = my_money.Atm.attempts(333)
        self.assertEquals(my_money.Atm.attempts, 0)
        return "Attempts are over!!!"

    @smoke
    def pin_attempts(self):
        attempts_1 = my_money.Atm.attempts(258)
        attempts_2 = my_money.Atm.attempts(333)
        attempts_3 = my_money.Atm.attempts(458)
        self.assertEquals(my_money.Atm.attempts, 0)
