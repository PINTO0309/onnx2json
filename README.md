# onnx2json
Exports the ONNX file to a JSON file.

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