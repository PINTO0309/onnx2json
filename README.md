# onnx2json
Exports the ONNX file to a JSON file.  
  
[![PyPI - Downloads](https://img.shields.io/pypi/dm/onnx2json?color=2BAF2B&label=Downloads%EF%BC%8FInstalled)](https://pypistats.org/packages/onnx2json) ![GitHub](https://img.shields.io/github/license/PINTO0309/onnx2json?color=2BAF2B) [![PyPI](https://img.shields.io/pypi/v/onnx2json?color=2BAF2B)](https://pypi.org/project/onnx2json/)

## 1. Install

```
$ pip install onnx2json --upgrade
```

## 2. Usage

```
onnx2json [-h] \
  --model_path MODEL_PATH \
  [--json_path JSON_PATH] \
  [--json_indent JSON_INDENT]

optional arguments:
  -h, --help
                        show this help message and exit
  --model_path MODEL_PATH
                        Input onnx model path (*.onnx)
  --json_path JSON_PATH
                        Output JSON file path (*.json)
  --json_indent JSON_INDENT
                        Number of indentations in JSON (default=2)
```

## 3. Sample

```
$ onnx2json --model_path aaa.onnx --json_path aaa.json --json_indent 2
```
