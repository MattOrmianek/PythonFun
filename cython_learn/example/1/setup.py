from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("main", ["main.pyx"]),
    Extension("module1", ["module1.pyx"]),
    Extension("module2", ["module2.pyx"]),
]

setup(
    name='MyCythonApp',
    ext_modules=cythonize(extensions),
)

# to run python -c "import main; main.main()"
