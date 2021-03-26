from distutils.core import setup

setup(
    name="ascii-cheat-sheets",
    version="1.0",
    py_modules=["main"],
    data_files=[("config", ["requirements.txt"])],
    url="https://github.com/render1980/ascii-cheat-sheets",
    author="render1980",
    license="Apache-2.0 License",
    author_email="render1980@gmail.com",
)
