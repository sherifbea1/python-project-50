from pathlib import Path
import sys
import os


sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')),
)

from gendiff.core import generate_diff


def get_fixture_path(filename):
    return Path(__file__).parent / 'tests_data' / filename


def read_file(filepath):
    return Path(filepath).read_text()


def test_generate_diff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file(get_fixture_path('expected.txt')).strip()
    assert generate_diff(file1, file2).strip() == expected


def test_generate_diff_yaml():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    expected = read_file(get_fixture_path('expected.txt')).strip()
    assert generate_diff(file1, file2).strip() == expected


def test_generate_diff_nested_json():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected = read_file(get_fixture_path('expected_nested.txt')).strip()
    assert generate_diff(file1, file2).strip() == expected


def test_generate_diff_nested_yaml():
    file1 = get_fixture_path('file1_nested.yml')
    file2 = get_fixture_path('file2_nested.yml')
    expected = read_file(get_fixture_path('expected_nested.txt')).strip()
    assert generate_diff(file1, file2).strip() == expected


def test_generate_diff_plain():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected = read_file(get_fixture_path('expected_plain.txt')).strip()
    assert generate_diff(file1, file2, 'plain').strip() == expected
