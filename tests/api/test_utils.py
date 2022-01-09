from os.path import exists
from unittest.mock import patch

from hive.api.utils import print_qr_label


@patch('hive.api.utils.check_call', lambda x: None)
def test_print_qr_label():
    print_qr_label('upc', 'description')
    assert exists('label.pdf')
