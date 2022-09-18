import pytest
from deepclassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError

# TODO tox # will run the tox configuration

# TODO pytest -v
class Test_read_yaml:
    yaml_files = [r"tests\data\demo.yaml", r"tests\data\empty.yaml"]

    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):  # if it raises
            read_yaml(Path(self.yaml_files[1]))

    def test_read_yaml_out(self):
        response = read_yaml(Path(self.yaml_files[0]))
        assert isinstance(response, ConfigBox)

    @pytest.mark.parametrize("path_to_yaml", yaml_files)
    def test_read_yaml_bad_type(self, path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)
