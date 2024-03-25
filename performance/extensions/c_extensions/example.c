#include <Python.h>

// Function declaration in C
static PyObject *add(PyObject *self, PyObject *args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a + b);
}

// Method definitions
static PyMethodDef ExampleMethods[] = {
    {"add",  add, METH_VARARGS, "Add two numbers"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

// Module definition
static struct PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "example",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    ExampleMethods
};

// Initialization function
PyMODINIT_FUNC PyInit_example(void) {
    return PyModule_Create(&examplemodule);
}
