from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "update_pixels",
        ["update_pixels.pyx"],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
    )
]

setup(
    name='parallel-image-processing',
    ext_modules=cythonize(ext_modules),
)

