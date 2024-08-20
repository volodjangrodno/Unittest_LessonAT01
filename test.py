import unittest
from main import add, subtract, multiply, divide, check, divide2


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, 7), 9)
        self.assertNotEqual(add(3, 7), 9) # в этом случае не выдаст ошибку при тесте, мак как мы изменили условие теста

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(subtract(4, 2), 1)
        self.assertNotEqual(subtract(4, 2), 1) # в этом случае не выдаст ошибку при тесте, мак как мы изменили условие теста

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)
        self.assertNotEqual(multiply(2, 5), 12) # в этом случае не выдаст ошибку при тесте, мак как мы изменили условие теста

    def test_divide(self):
        self.assertEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)
        self.assertNotEqual(divide(4, 2), 3) # в этом случае не выдаст ошибку при тесте, мак как мы изменили условие теста

class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        self.assertTrue(not check(1)) # в этом слуае не будет выдавать ошибку при тесте так как мы изменили условие вместо check поставили not check
        self.assertTrue(not check(3)) # в этом слуае не будет выдавать ошибку при тесте так как мы изменили условие вместо check поставили not check
        self.assertTrue(not check(57)) # в этом слуае не будет выдавать ошибку при тесте так как мы изменили условие вместо check поставили not check

        self.assertFalse(check(1))  # в этом слуае не будет выдавать ошибку при тесте так как мы изменили условие вместо .assertTrue поставили .assertFalse
        self.assertFalse(check(3))  # в этом слуае не будет выдавать ошибку при тесте так как мы изменили условие вместо .assertTrue поставили .assertFalse
        self.assertFalse(check(57))  # в этом слуае не будет выдавать ошибку при тесте так как мы изменили условие вместо .assertTrue поставили .assertFalse

class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide2(10, 2), 5)
        self.assertEqual(divide2(6, 3), 2)
        self.assertEqual(divide2(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide2, 6, 0)
        self.assertRaises(TypeError, divide, 6, 0) # В этом случае при запуске кода будет выдаваться ошибка, так как тестирование прописано именно на выброс ошибки ValueError


if __name__ == '__main__':
	unittest.main()