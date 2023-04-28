#  this file collects data for tests
# specific variables can be expanded by additional test sets (so different sets of test data
# will be used while running tests using parametrization)

class TestData:
    valid_login_credentials_admin = [{"admin@demo.com": "admin"}
                                     # ,{"client@demo.com": "client"}
                                     ]
    invalid_login_credentials_admin = [{"admi@demo.com": "admin"},
                                       {"client@demo.com": "clien"}]

    space_data = [
        {
            "title": "название пространства/раздела вики - тест",
            "desc": "описание пространства/раздела - тест",
            "category": "категория/тег - тест"
        }
    ]
