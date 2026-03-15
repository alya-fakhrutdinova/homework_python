import allure

def pytest_configure(config):
    allure.dynamic.title("Автоматизированные тесты")
