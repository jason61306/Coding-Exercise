import pytest
import os

def pytest_addoption(parser):
    # ability to test API on different hosts
    parser.addoption("--host", action="store", default="http://localhost:5000")

@pytest.fixture(scope="session")
def host(request):
    return request.config.getoption("--host")

@pytest.fixture(scope="session")
def api(host):
    return os.path.join(host)


