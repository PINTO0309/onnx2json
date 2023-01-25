# onnx2json
Exports the ONNX file to a JSON file and JSON dict. Click here for **[json2onnx](https://github.com/PINTO0309/json2onnx)**.

https://github.com/PINTO0309/simple-onnx-processing-tools

[![PyPI - Downloads](https://img.shields.io/pypi/dm/onnx2json?color=2BAF2B&label=Downloads%EF%BC%8FInstalled)](https://pypistats.org/packages/onnx2json) ![GitHub](https://img.shields.io/github/license/PINTO0309/onnx2json?color=2BAF2B) [![PyPI](https://img.shields.io/pypi/v/onnx2json?color=2BAF2B)](https://pypi.org/project/onnx2json/)

<p align="center">
  <img src="https://user-images.githubusercontent.com/33194443/170162575-4c3b9b62-a8f4-44a3-9240-856f9abdf460.png" />
</p>

## 1. Setup

### 1-1. HostPC
```bash
### option
$ echo export PATH="~/.local/bin:$PATH" >> ~/.bashrc \
&& source ~/.bashrc

### run
$ pip install -U onnx protobuf \
&& python3 -m pip install -U onnx_graphsurgeon --index-url https://pypi.ngc.nvidia.com \
&& pip install -U onnx2json
```
### 1-2. Docker
https://github.com/PINTO0309/simple-onnx-processing-tools#docker

## 2. CLI Usage
```
usage:
  onnx2json [-h]
  -if INPUT_ONNX_FILE_PATH
  -oj OUTPUT_JSON_PATH
  [-i JSON_INDENT]

optional arguments:
  -h, --help
      show this help message and exit

  -if INPUT_ONNX_FILE_PATH, --input_onnx_file_path INPUT_ONNX_FILE_PATH
      Input ONNX model path. (*.onnx)

  -oj OUTPUT_JSON_PATH, --output_json_path OUTPUT_JSON_PATH
      Output JSON file path (*.json) If not specified, no JSON file is output.

  -i JSON_INDENT, --json_indent JSON_INDENT
      Number of indentations in JSON. (default=2)
```

## 3. In-script Usage
```python
>>> from onnx2json import convert
>>> help(convert)

Help on function convert in module onnx2json.onnx2json:

convert(
  input_onnx_file_path: Union[str, NoneType] = '',
  onnx_graph: Union[onnx.onnx_ml_pb2.ModelProto, NoneType] = None,
  output_json_path: Union[str, NoneType] = '',
  json_indent: Union[int, NoneType] = 2
)

    Parameters
    ----------
    input_onnx_file_path: Optional[str]
        Input onnx file path.
        Either input_onnx_file_path or onnx_graph must be specified.
        Default: ''

    onnx_graph: Optional[onnx.ModelProto]
        onnx.ModelProto.
        Either input_onnx_file_path or onnx_graph must be specified.
        onnx_graph If specified, ignore input_onnx_file_path and process onnx_graph.

    output_json_path: Optional[str]
        Output JSON file path (*.json) If not specified, no JSON file is output.
        Default: ''

    json_indent: Optional[int]
        Number of indentations in JSON.
        Default: 2

    Returns
    -------
    onnx_json: dict
        Converted JSON dict.
```

## 4. CLI Execution
```bash
$ onnx2json \
--input_onnx_file_path NonMaxSuppression.onnx \
--output_json_path NonMaxSuppression.json \
--json_indent 2
```

## 5. In-script Execution
```python
from onnx2json import convert

onnx_json = convert(
  input_onnx_file_path="NonMaxSuppression.onnx",
  output_json_path="NonMaxSuppression.json",
  json_indent=2,
)

# or

onnx_json = convert(
  onnx_graph=graph,
)
```

## 6. Issues
https://github.com/PINTO0309/simple-onnx-processing-tools/issues
