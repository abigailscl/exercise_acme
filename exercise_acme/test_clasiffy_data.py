import unittest
from file import Controller, File

class TestControllerFile(unittest.TestCase):
    def test_classify_data(self):
        controller = Controller()
        file = open(r'C:\Users\Lenovo\Documents\EMPLEO\ACME\example_test.txt')
        content = file.readlines()
        file.close()  
        self.assertTrue(controller.classify_data(content))
        self.assertEqual(controller.classify_data([]), [])
        
    def test_compare_data_employee(self):
        controller = Controller()
        file = open(r'C:\Users\Lenovo\Documents\EMPLEO\ACME\example_test.txt')
        content = file.readlines()
        file.close()  
        list_employees = controller.classify_data(content)
        self.assertEqual(controller.compare_data_employee(list_employees), ['RENE-ASTRID: 2', 'RENE-ANDRES: 2', 'ASTRID-ANDRES: 3'])
        self.assertNotEqual(controller.compare_data_employee(list_employees), ['RENE-ASTRID: 2', 'RENE-ANDRES: 2', 'ASTRID-ANDRES: 5'])
        self.assertNotEqual(controller.compare_data_employee(list_employees), ['ASTRID-RENE: 2', 'RENE-ANDRES: 2', 'ASTRID-ANDRES: 3'])
    
    def test_compare_office(self):
        controller = Controller()
        file = open(r'C:\Users\Lenovo\Documents\EMPLEO\ACME\example_test.txt')
        content = file.readlines()
        file.close()  
        list_employees = controller.classify_data(content)
        self.assertEqual(controller.compare_office(list_employees[0], list_employees[0]), 'RENE-RENE: 5')
        self.assertEqual(controller.compare_office(list_employees[1], list_employees[2]), 'ASTRID-ANDRES: 3')
        self.assertEqual(controller.compare_office(list_employees[2], list_employees[0]), 'ANDRES-RENE: 2')
        
    def test_compare_schedule(self):
        controller = Controller()
        file = open(r'C:\Users\Lenovo\Documents\EMPLEO\ACME\example_test.txt')
        content = file.readlines()
        file.close()  
        list_employees = controller.classify_data(content)
        self.assertEqual(controller.compare_schedule(list_employees[2], list_employees[2], 0, 0), 1)
        self.assertEqual(controller.compare_schedule(list_employees[1], list_employees[2], 1, 2), 0)
        self.assertEqual(controller.compare_schedule(list_employees[1], list_employees[0], 1, 3), 0)
        self.assertEqual(controller.compare_schedule(list_employees[0], list_employees[2], 4, -1), 1)
                     
if __name__ == "__main__":
    unittest.main()