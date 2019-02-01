import json
import os

class JsonArrayWriter(object):
    def __init__(self, file_name, new_file=False):
        """
        param file_name : str, name of the file to be written
        param new_file : bool, default False, forced to create a new file or not
        """
        self.file_name = file_name
        self.new_file = new_file
    
    def _write_item(self, item):
        data_string = json.dumps([item], indent=4)[2:-2]
        if not os.path.isfile(self.file_name) or self.new_file:
            with open(self.file_name, 'w') as f:
                f.write('[\n')
                f.write(data_string)
                self.new_file = False
        else:
            with open(self.file_name, 'a') as f:
                f.write(',\n')
                f.write(data_string)
    
    def write(self, obj):
        if isinstance(obj, list):
            for o in obj:
                self._write_item(o)
        else:
            self._write_item(obj)
    
    def close(self):
        if os.path.isfile(self.file_name):
            with open(self.file_name, 'a') as f:
                f.write('\n]')
    
    def __enter__(self):
        return self
                
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()