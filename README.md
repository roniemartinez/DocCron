# DocCron

Schedule with Docstrings

<table>
    <tr>
        <td>License</td>
        <td><img src='https://img.shields.io/pypi/l/DocCron.svg'></td>
        <td>Version</td>
        <td><img src='https://img.shields.io/pypi/v/DocCron.svg'></td>
    </tr>
    <tr>
        <td>Travis CI</td>
        <td><img src='https://travis-ci.org/roniemartinez/DocCron.svg?branch=master'></td>
        <td>Coverage</td>
        <td><img src='https://codecov.io/gh/roniemartinez/DocCron/branch/master/graph/badge.svg'></td>
    </tr>
    <tr>
        <td>AppVeyor</td>
        <td><img src='https://ci.appveyor.com/api/projects/status/ceqj4tmh13r8hc79/branch/master?svg=true'></td>
        <td>Supported versions</td>
        <td><img src='https://img.shields.io/pypi/pyversions/DocCron.svg'></td>
    </tr>
    <tr>
        <td>Wheel</td>
        <td><img src='https://img.shields.io/pypi/wheel/DocCron.svg'></td>
        <td>Implementation</td>
        <td><img src='https://img.shields.io/pypi/implementation/DocCron.svg'></td>
    </tr>
    <tr>
        <td>Status</td>
        <td><img src='https://img.shields.io/pypi/status/DocCron.svg'></td>
        <td>Downloads</td>
        <td><img src='https://img.shields.io/pypi/dm/DocCron.svg'></td>
    </tr>
    <tr>
        <td>Show your support</td>
        <td><a href='https://saythanks.io/to/roniemartinez'><img src='https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg'></a></td>
    </tr>
</table>

## Installation

```bash
pip install DocCron
```

## Description

Cron-based scheduler inspired by [doctest](https://en.wikipedia.org/wiki/Doctest)

## Example

Cron jobs can be embedded into docstrings by using a [literal block](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#literal-blocks) (`::`). Literal blocks should start with `/etc/crontab`.

### Standard/Extended Format

Run `hello()` at every 2nd minute and 3rd minute:

```python
import time


def hello():
    """
    Print "hello world" at every 2nd minute and 3rd minute:

    /etc/crontab::

        */2 * * * *
        */3 * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S'), "hello world")


if __name__ == '__main__':
    import doccron
    doccron.run_jobs()

```

### Quartz Format

Run `hello()` at every 2nd second and 3rd second:

```python
import time


def hello():
    """
    Print "hello world" every 2nd second and 3rd second:

    /etc/crontab::

        */2 * * * * *
        */3 * * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S'), "hello world")


if __name__ == '__main__':
    import doccron
    doccron.run_jobs(quartz=True)

```

## Features

- Standard and extended cron formats (see [CRON Expression](https://en.wikipedia.org/wiki/Cron#CRON_expression))
- [Nonstandard predefined scheduling definitions](https://en.wikipedia.org/wiki/Cron#Nonstandard_predefined_scheduling_definitions)
- [Non-standard characters](https://en.wikipedia.org/wiki/Cron#Non-standard_characters)
- [Quartz format](http://www.quartz-scheduler.org/documentation/quartz-2.x/tutorials/crontrigger.html)
- Works with documentation tools like [Sphinx](https://github.com/sphinx-doc/sphinx)

## TODO

- Human readable date/time strings 
- Timezone-awareness

## References

- [Cron Format](http://www.nncron.ru/help/EN/working/cron-format.htm)
- [Wikipedia - Cron](https://en.wikipedia.org/wiki/Cron)

## Author

- [Ronie Martinez](mailto:ronmarti18@gmail.com)