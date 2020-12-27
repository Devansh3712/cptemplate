# cptemplate

Module for creating a pre-defined competitive programming template for python

View on PyPi: https://pypi.org/project/cptemplate/

View on Libraries.io: https://libraries.io/pypi/cptemplate

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/ansicolortags.svg)](https://pypi.org/project/pycrypt-cli/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

## Installation

`cptemplate` can be installed using pip, and it is an OS independent module

> Windows
```shell
pip install cptemplate
```

> Linux
```bash
pip3 install cptemplate
```

## Usage

```
Usage: cptemplate [OPTIONS] COMMAND [ARGS]...

  competitive programming template for python

Options:
  --help  Show this message and exit.

Commands:
  info  information about the module
  new   create a new template file
  test  run and test the code
```

### `cptemplate` commands

 - `cptemplate` can be used by directly typing the command `cptemplate` in CMD/Terminal

- For creating a new template file, the command `cptemplate new` is used, which by default creates a `new.py` file in the directory where `cptemplate` command is run. By using `cptemplate new -n <file_name>`, template with name `file_name` will be created.

```
Usage: cptemplate new [OPTIONS]

  create a new template file, default name new.py

Options:
  -n, --file_name TEXT  Set custom name for file
  --help                Show this message and exit.
```

> default command, creates file `new.py`
```shell
cptemplate new
```

> `-n <file_name>` command, creates file with name `file_name`
```shell
cptemplate new -n main
```

- For running/testing the file, the command `cptemplate test` is used to run `new.py` (default command). To open a file with custom name,
the command `cptemplate test -n <file_name>` is used, to run `file_name.py` file

```
Usage: cptemplate test [OPTIONS]

  run and test the code, by default runs new.py

Options:
  -n, --file_name TEXT  Open .py file with custom name
  --help                Show this message and exit.
```

> runs by default `new.py`
```shell
cptemplate test
```

> runs `file_name.py`
```shell
cptemplate test -n main
```

## Contributing

Contributions can be made to the project by making PR's :)

## License

MIT License
