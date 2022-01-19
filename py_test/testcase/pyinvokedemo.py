# content of myinvoke.py
import pytest
import sys


class MyPlugin:
    def pytest_configure(config):
        config.addinivalue_line(
            "markers", "env(name): mark test to run only on named environment"
        )

    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")



if __name__ == "__main__":
    retcode = pytest.main()
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))