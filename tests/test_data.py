#  this file collects data for tests

class TestData:
    valid_login_credentials_admin = [{"admin@demo.com": "admin"},
                                     {"client@demo.com": "client"}]
    invalid_login_credentials_admin = [{"admi@demo.com": "admin"},
                                       {"client@demo.com": "clien"}]
    space_data = [["space title test", "space description test"]]
