from anketa import app, new_zapis
import unittest

class TestAnketa(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.fio = 'Test Student'
        self.group = 'Test Group'
        self.question = 'yes'

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_form_submit(self):
        response = self.app.post('/', data=dict(fio=self.fio, group=self.group, question=self.question))
        self.assertIn('Спасибо за ваш ответ', response.data.decode())

    def test_new_zapis(self):
        i = 1
        new_zapis()
        with open("text.txt", "r") as file:
            lines = file.readlines()
            self.assertIn("Запись №1\n", lines)
            self.assertIn("ФИО студента: " + self.fio + '\n', lines)
            self.assertIn("Группа: " + self.group + '\n', lines)
            self.assertIn("Доволен ли своими оценками? " + self.question + '\n', lines)

    def tearDown(self):
        with open("text.txt", "w") as f:
            pass

if __name__ == '__main__':
    unittest.main()


