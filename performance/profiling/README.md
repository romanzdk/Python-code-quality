1. Install `graphviz` and `htop`

- `brew install graphviz htop` or
- `sudo apt install graphviz htop` or
- `nix-shell -p graphviz htop`

2. Install required python packages

- `poetry add gprof2dot snakeviz line-profiler psutil memory-profiler`
