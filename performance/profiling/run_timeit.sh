#!/usr/bin/env bash
python -m timeit "'-'.join(str(n) for n in range(100))"