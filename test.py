import json
import os

from json_array_writer import JsonArrayWriter

def test_json_array_writer():
    test_file_name = '_test.txt'

    # test
    writer = JsonArrayWriter(test_file_name, new_file=True)
    writer.write({'a': 0})
    del writer
    writer = JsonArrayWriter(test_file_name)
    writer.write({'b': 1})
    writer.close()
    with open(test_file_name, 'r') as f:
        data = json.load(f)
    assert data[0] == {'a': 0}
    assert data[1] == {'b': 1}

    with JsonArrayWriter(test_file_name, new_file=True) as writer:
        writer.write([{'c': 2}, {'d': 3}])
        writer.write({'e': 4})
        writer.write({'f': 5})
    with open(test_file_name, 'r') as f:
        data = json.load(f)
    assert data[0] == {'c': 2}
    assert data[1] == {'d': 3}
    assert data[2] == {'e': 4}
    assert data[3] == {'f': 5}

    os.remove(test_file_name)

    print('====  JsonArrayWriter test finished successfully  ====')

test_json_array_writer()