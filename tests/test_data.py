#  this file collects data for tests
# specific variables can be expanded by additional test sets (so different sets of test data
# will be used while running tests using parametrization)

from datetime import datetime
from datetime import timedelta


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

    current_datetime = datetime.now()

    event_data = [{"title": "Митинг AntHill",
                   "type": "event",  # type of events: event, meeting, personal, task
                   "start_datetime": current_datetime + timedelta(days=1),
                   # by that we assign datetime as current daytime +1 day
                   "end_datetime": current_datetime + timedelta(days=2),
                   # by that we assign datetime as current daytime +2 day
                   "place": "Париж",
                   "desc": "На встречу надеть теплую шапку"
                   }
                  ]
