import unittest
import sqlite3 as s

class Mobileapp(unittest.TestCase):

    def setUp(self):
        self.Brand = "Samsung"
        self.Brand2 = "apple"
        self.snumber = "11"
        self.connection = s.connect("Mobile.db")

    def tearDown(self):
        self.Brand = ""
        self.Brand2 = ""
        self.snumber = ""
        self.connection.close()

    def test_case_1(self):
        res = self.connection.execute("SELECT BRAND FROM SMARTPHONES WHERE SERIAL_NUMBER="+self.snumber)
        for i in res:
            fetchbrand = i[0]

        self.assertEqual(fetchbrand, self.Brand)

    def test_case_2(self):
        res = self.connection.execute("SELECT BRAND FROM SMARTPHONES WHERE SERIAL_NUMBER="+self.snumber)
        for i in res:
            fetchbrand = i[0]

        self.assertNotEqual(fetchbrand, self.Brand2)


if __name__ == "__main__":
    unittest.main()


