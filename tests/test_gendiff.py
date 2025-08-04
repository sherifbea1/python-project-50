from gendiff.scripts.gendiff import generate_diff
from pathlib import Path


def get_fixture_path(filename):
    return Path(__file__).parent / 'tests_data' / filename


def read_file(filepath):
    return Path(filepath).read_text()


def test_generate_diff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file(get_fixture_path('expected.txt')).strip()
    assert generate_diff(file1, file2).strip() == expected
