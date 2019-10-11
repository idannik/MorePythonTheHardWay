from unittest import TestCase
from unittest.mock import Mock, mock_open, patch

from cat.cat import Cat


class TestCat(TestCase):
    def test_get_lines(self):
        args = Mock()
        args.file = ['idan.txt']
        with patch('builtins.open', mock_open(read_data='idan'), create=True) as m:
            assert list(Cat(args).get_lines()) == ['idan']
