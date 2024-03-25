use pyo3::prelude::*;

#[pyfunction]
fn fibonacci(n: u32) -> PyResult<u64> {
    fn fib(n: u32) -> u64 {
        match n {
            0 => 0,
            1 => 1,
            _ => fib(n - 1) + fib(n - 2),
        }
    }

    Ok(fib(n))
}

#[pymodule]
fn rust_extension(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    Ok(())
}
