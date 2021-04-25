#! /usr/bin/env python

import onnx
import json
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import Parse
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, required=True, help='Input onnx model path (*.onnx)')
    parser.add_argument('--json_path', type=str, default='', help='Output JSON file path (*.json)')
    parser.add_argument('--json_indent', type=int, default=2, help='Number of indentations in JSON (default=2)')
    args = parser.parse_args()

    # Convert onnx model to JSON
    model_file_path, model_ext = os.path.splitext(args.model_path)
    onnx_model = onnx.load(args.model_path)
    s = MessageToJson(onnx_model)
    onnx_json = json.loads(s)

    output_json_path = ''
    if args.json_path:
        output_json_path = args.json_path
    else:
        output_json_path = f'{model_file_path}.json'

    with open(output_json_path, 'w') as f:
        json.dump(onnx_json, f, indent=args.json_indent)

if __name__ == '__main__':
    main()