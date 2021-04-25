#!/bin/bash

rm -rf build/
rm -rf dist/
rm -rf onnx2json.egg-info/
python3 setup.py sdist bdist_wheel