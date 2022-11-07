# `solus`

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]
[![Test][Test Badge]][Actions]
[![Coverage][Coverage Badge]][Coverage]

> *Singleton types.*

In python, an *entry point* can be thought of as an explicit function
that gets called when the script is run directly from the console.

Defining an entry point requires some boilerplate code, which is
abstracted away by this library.

## Installing

**Python 3.7 or above is required.**

### pip

Installing the library with `pip` is quite simple:

```console
$ pip install solus
```

Alternatively, the library can be installed from source:

```console
$ git clone https://github.com/nekitdev/solus.git
$ cd solus
$ python -m pip install .
```

### poetry

You can add `solus` as a dependency with the following command:

```console
$ poetry add solus
```

Or by directly specifying it in the configuration like so:

```toml
[tool.poetry.dependencies]
solus = "^1.0.1"
```

Alternatively, you can add it directly from the source:

```toml
[tool.poetry.dependencies.solus]
git = "https://github.com/nekitdev/solus.git"
```

## Examples

### Default

[`Singleton`][solus.core.Singleton] type is used to create *thread-safe* singletons.

```python
from solus import Singleton


class Null(Singleton):
    ...
```

Somewhere else in the code:

```python
null = Null()  # instantiate
```

### Unsafe

[`UnsafeSingleton`][solus.core.UnsafeSingleton] type is used to create *thread-unsafe* singletons.

```python
from solus import UnsafeSingleton


class Null(UnsafeSingleton):
    ...


null = Null()  # instantiate right away
```

### Warning

!!! warning

    It is highly recommended to instantiate unsafe singleton types right after their creation!

## Documentation

You can find the documentation [here][Documentation].

## Support

If you need support with the library, you can send an [email][Email]
or refer to the official [Discord server][Discord].

## Changelog

You can find the changelog [here][Changelog].

## Security Policy

You can find the Security Policy of `solus` [here][Security].

## Contributing

If you are interested in contributing to `solus`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`solus` is licensed under the MIT License terms. See [License][License] for details.

[Email]: mailto:support@nekit.dev

[Discord]: https://nekit.dev/discord

[Actions]: https://github.com/nekitdev/solus/actions

[Changelog]: https://github.com/nekitdev/solus/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/solus/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/solus/blob/main/CONTRIBUTING.md
[Security]: https://github.com/nekitdev/solus/blob/main/SECURITY.md

[License]: https://github.com/nekitdev/solus/blob/main/LICENSE

[Package]: https://pypi.org/project/solus
[Coverage]: https://codecov.io/gh/nekitdev/solus
[Documentation]: https://nekitdev.github.io/solus

[Discord Badge]: https://img.shields.io/badge/chat-discord-5865f2
[License Badge]: https://img.shields.io/pypi/l/solus
[Version Badge]: https://img.shields.io/pypi/v/solus
[Downloads Badge]: https://img.shields.io/pypi/dm/solus

[Documentation Badge]: https://github.com/nekitdev/solus/workflows/docs/badge.svg
[Check Badge]: https://github.com/nekitdev/solus/workflows/check/badge.svg
[Test Badge]: https://github.com/nekitdev/solus/workflows/test/badge.svg
[Coverage Badge]: https://codecov.io/gh/nekitdev/solus/branch/main/graph/badge.svg

[solus.core.Singleton]: https://nekitdev.github.io/solus/reference#solus.Singleton
[solus.core.UnsafeSingleton]: https://nekitdev.github.io/solus/reference#solus.UnsafeSingleton
