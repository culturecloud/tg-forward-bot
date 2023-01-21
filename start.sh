#!/bin/bash

if [ ! -d "venv" ]; then
    python3.10 -m venv venv --upgrade-deps \
    && venv/bin/pip3.10 install --no-cache-dir wheel \
    && venv/bin/pip3.10 install --no-cache-dir -Ur requirements.txt \
    && reset
fi

source venv/bin/activate \
&& python3.10 -Bc "import pathlib; import shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]" \
&& python3.10 -m app
