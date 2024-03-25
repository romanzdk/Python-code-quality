#!/usr/bin/env bash
python -m cProfile -o profile.out performance/profiling/cprofile_test.py
gprof2dot -f pstats profile.out | dot -Tpng -o call_graph.png
snakeviz profile.out