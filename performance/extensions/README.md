1. Install rust

- https://rustup.rs/

2. Install required packages

- `poetry add cython maturin`

3. Build extensions

- `python setup.py build_ext --inplace` for Cython and C
- `maturin develop` for Rust
