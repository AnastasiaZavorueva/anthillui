UI testing project for AH. (a web App for teams to track issues and manage projects)

Includes test scenarios to check UI functionality on such pages: 

- login page
- wiki page
- calendar page
- chat page

Tests can be run with different sets of test data by using parametrization. 

The project supports execution of specific tests by using Pytest markers. 

Allure Report framework is added to the project, so that reports of test(s) execution in a more clear way can be generated.

The project is created as a part of an educational course by QALearning School.

▶️ To run all tests at once use command "pytest tests" in the Terminal. Or use a command "pytest ./tests/[test_filename.py]" to run a specific test

▶️ To run test(s) with generating a report by Allure, firstly use command "pytest tests --alluredir results" (for all tests) or "pytest ./tests/[test_filename.py] --alluredir results" for specific test in the Terminal of Pycharm. Then in Terminal navigate to the folder of the project and run command “allure serve results” to open the generated report.

▶️ To run only some tests (with Pytest markers "smoke", "regression" or "flaky") use this format of the command: "pytest -m [mark] tests"
