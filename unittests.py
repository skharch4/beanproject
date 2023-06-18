import unittest
import database
from coffee_beans import prompt_add_new_bean, prompt_see_all_beans, prompt_find_bean_by_name, prompt_best_method, prompt_delete_bean, prompt_update_bean


class CoffeeAppTests(unittest.TestCase):
    def setUp(self):
        # Підготовка необхідних ресурсів або залежностей для ваших тестів
        self.connection = database.connect()
        database.create_tables(self.connection)

    def tearDown(self):
        # Завершення роботи з ресурсами після виконання тестів
        self.connection.close()

    def test_prompt_add_new_bean(self):
        #тест для перевірки чи працює додавання нового зерна
        pass

    def test_prompt_see_all_beans(self):
        #Тест для перевірки чи працює функція перегляду ВСІХ зерен
        pass

    def test_prompt_find_bean_by_name(self):
        #Тест для перевірки чи працює пошук зерна по назві
        pass

    def test_prompt_best_method(self):
        #тест для перевірки чи працює вибір кращого методу
        pass
    def test_prompt_deletete_bean(self):
        pass
    def test_edit_beans(self):
        pass


if __name__ == '__main__':
    unittest.main()
