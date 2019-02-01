# JsonArrayWriter
Write multiple json-style arrays in a json file.

## Usage
```python
from json_array_writer import JsonArrayWriter

with JsonArrayWriter("combined.json") as writer:
  writer.write({"a": 0})
  writer.write([{"b": 1}, {"c": 2}])

with open("combined.json", "r") as f:
  print(f.read())
```
Output:
```
[
    {
        "a": 0
    },
    {
        "b": 1
    },
    {
        "c": 2
    }
]
```
