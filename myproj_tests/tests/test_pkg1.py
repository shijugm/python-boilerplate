import pytest
import myproj_tests.shared.myproj_test_settings as myproj_test_settings
import myproj.common.settings as settings
from myproj_tests.shared import common
from myproj.pkg1.mod1inpkg1 import dummyinmod1pkg1 as dummyinmod1pkg1

@pytest.fixture(scope="module" , autouse = True)
def initialize_testmodule():
    settings.init()
    myproj_test_settings.init()

@pytest.fixture(scope="function")
def setup_function():
    common.cleanup_db()



@pytest.mark.usefixtures("setup_function")
def test_first_test_pkg1():
    # load initial data
    common.load_table_from_csv('table_name', 'csvfile')
    # run the code
    dummyinmod1pkg1()
    # result data
    result = common.read_from_table('table_name', 'COLUMN_NAME1, COLUMN_NAME2')

    # expected output
    expected = common.load_list_from_csv('csvfilename')
    
    assert result == expected