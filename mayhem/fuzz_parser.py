#!/usr/bin/env python3
import atheris
import sys
import tempfile

with atheris.instrument_imports():
    import pyshark


@atheris.instrument_func
def TestOneInput(data):
    with tempfile.NamedTemporaryFile() as f:
        f.write(data)
        f.flush()
        pyshark.FileCapture(f.name)


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()


