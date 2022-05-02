#! /usr/bin/env python

import sys
import onnx
import json
from google.protobuf.json_format import MessageToJson
from typing import Optional
from argparse import ArgumentParser

class Color:
    BLACK          = '\033[30m'
    RED            = '\033[31m'
    GREEN          = '\033[32m'
    YELLOW         = '\033[33m'
    BLUE           = '\033[34m'
    MAGENTA        = '\033[35m'
    CYAN           = '\033[36m'
    WHITE          = '\033[37m'
    COLOR_DEFAULT  = '\033[39m'
    BOLD           = '\033[1m'
    UNDERLINE      = '\033[4m'
    INVISIBLE      = '\033[08m'
    REVERCE        = '\033[07m'
    BG_BLACK       = '\033[40m'
    BG_RED         = '\033[41m'
    BG_GREEN       = '\033[42m'
    BG_YELLOW      = '\033[43m'
    BG_BLUE        = '\033[44m'
    BG_MAGENTA     = '\033[45m'
    BG_CYAN        = '\033[46m'
    BG_WHITE       = '\033[47m'
    BG_DEFAULT     = '\033[49m'
    RESET          = '\033[0m'


def convert(
    input_onnx_file_path: Optional[str] = '',
    onnx_graph: Optional[onnx.ModelProto] = None,
    output_json_path: Optional[str] = '',
    json_indent: Optional[int] = 2,
):
    """
    Parameters
    ----------
    input_onnx_file_path: Optional[str]
        Input onnx file path.\n\
        Either input_onnx_file_path or onnx_graph must be specified.\n\
        Default: ''

    onnx_graph: Optional[onnx.ModelProto]
        onnx.ModelProto.\n\
        Either input_onnx_file_path or onnx_graph must be specified.\n\
        onnx_graph If specified, ignore input_onnx_file_path and process onnx_graph.

    output_onnx_file_path: Optional[str]
        Output onnx file path. If not specified, no ONNX file is output.\n\
        Default: ''

    json_indent: Optional[int]
        Number of indentations in JSON.\n\
        Default: 2

    Returns
    -------
    onnx_json: dict
        Converted JSON dict.
    """

    # Unspecified check for input_onnx_file_path and onnx_graph
    if not input_onnx_file_path and not onnx_graph:
        print(
            f'{Color.RED}ERROR:{Color.RESET} '+
            f'One of input_onnx_file_path or onnx_graph must be specified.'
        )
        sys.exit(1)

    if not onnx_graph:
        onnx_graph = onnx.load(input_onnx_file_path)

    s = MessageToJson(onnx_graph)
    onnx_json = json.loads(s)

    if output_json_path:
        with open(output_json_path, 'w') as f:
            json.dump(onnx_json, f, indent=json_indent)

    return onnx_json


def main():
    parser = ArgumentParser()
    parser.add_argument(
        '--input_onnx_file_path',
        type=str,
        required=True,
        help='Input ONNX model path. (*.onnx)'
    )
    parser.add_argument(
        '--output_json_path',
        type=str,
        required=True,
        help='Output JSON file path (*.json)'
    )
    parser.add_argument(
        '--json_indent',
        type=int,
        default=2,
        help='Number of indentations in JSON. (default=2)'
    )
    args = parser.parse_args()

    input_onnx_file_path = args.input_onnx_file_path
    output_json_path = args.output_json_path
    json_indent = args.json_indent

    # Convert onnx model to JSON
    onnx_graph = onnx.load(input_onnx_file_path)

    onnx_json = convert(
        input_onnx_file_path=None,
        onnx_graph=onnx_graph,
        output_json_path=output_json_path,
        json_indent=json_indent,
    )


if __name__ == '__main__':
    main()
