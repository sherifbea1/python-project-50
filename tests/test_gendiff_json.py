import json
from pathlib import Path
from gendiff.gendiff import generate_diff


def get_fixture_path(filename):
    return Path(__file__).parent / 'tests_data' / filename


def test_generate_diff_json():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')

    diff_json = generate_diff(file1, file2, 'json')

    
    parsed = json.loads(diff_json)
    assert isinstance(parsed, list)
    assert len(parsed) > 0


    for node in parsed:
        assert "key" in node
        assert "status" in node
        assert node["status"] in {"added", "removed", "updated", "unchanged", "nested"}


        if node["status"] == "updated":
            assert "old_value" in node
            assert "new_value" in node


        if node["status"] == "nested":
            assert "children" in node
            assert isinstance(node["children"], list)
