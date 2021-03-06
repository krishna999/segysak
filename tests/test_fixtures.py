import pytest
import pathlib

TEMP_TEST_DATA_DIR = 'test_data_temp'

@pytest.fixture(scope="session")
def temp_dir(tmpdir_factory):
    tdir = tmpdir_factory.mktemp(TEMP_TEST_DATA_DIR)
    return pathlib.Path(str(tdir))