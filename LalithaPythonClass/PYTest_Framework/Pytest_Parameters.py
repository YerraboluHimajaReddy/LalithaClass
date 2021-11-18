import pytest

@pytest.mark.parametrize("username, password",
                         [
                             ("Himaja", "HimajaReddy"),
                             ("lalitha", "lalithamantri"),
                             ("Himaja", "HimajaYerrabolu")
                         ]

                         )

def test_login(username, password):
    print(username)
    print(password)


# C:\Users\Sony\PycharmProjects\LalithaClass\venv\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --target Pytest_Parameters.py::test_login
# Testing started at 7:30 AM ...
# Launching pytest with arguments Pytest_Parameters.py::test_login --no-header --no-summary -q in C:\Users\Sony\PycharmProjects\LalithaClass\LalithaPythonClass\PYTest_Framework
#
# ============================= test session starts =============================
# collecting ... collected 3 items
#
# Pytest_Parameters.py::test_login[Himaja-HimajaReddy] PASSED              [ 33%]Himaja
# HimajaReddy
#
# Pytest_Parameters.py::test_login[lalitha-lalithamantri] PASSED           [ 66%]lalitha
# lalithamantri
#
# Pytest_Parameters.py::test_login[Himaja-HimajaYerrabolu] PASSED          [100%]Himaja
# HimajaYerrabolu
#
#
# ============================== 3 passed in 0.20s ==============================
#
# Process finished with exit code 0