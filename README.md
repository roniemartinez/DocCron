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
        <td><img src='https://travis-ci.org/Code-ReaQtor/DocCron.svg?branch=develop'></td>
        <td>Coverage</td>
        <td><img src='https://codecov.io/gh/Code-ReaQtor/DocCron/branch/develop/graph/badge.svg'></td>
    </tr>
    <tr>
        <td>AppVeyor</td>
        <td><img src='https://ci.appveyor.com/api/projects/status/ceqj4tmh13r8hc79/branch/develop?svg=true'></td>
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
        <td>Show your support</td>
        <td><a href='https://saythanks.io/to/Code-ReaQtor'><img src='https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg'></a></td>
    </tr>
</table>

## Installation

```bash
pip install DocCron
```

## Description

Cron scheduler inspired by [doctest](https://en.wikipedia.org/wiki/Doctest)

## Example

Run `hello()` at every 2nd minute and 3rd minute:

```python
import time


def hello():
    """
    */2 * * * *
    */3 * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S'), "hello world")


if __name__ == '__main__':
    import doccron
    doccron.run_jobs()

```

## Todo

- [x] Support [Nonstandard predefined scheduling definitions](https://en.wikipedia.org/wiki/Cron#Nonstandard_predefined_scheduling_definitions)
- [x] Support [Non-standard characters](https://en.wikipedia.org/wiki/Cron#Non-standard_characters)
- [ ] Support [Quartz format](http://www.quartz-scheduler.org/documentation/quartz-2.x/tutorials/crontrigger.html)

## References

- [Cron Format](http://www.nncron.ru/help/EN/working/cron-format.htm)
- [Wikipedia - Cron](https://en.wikipedia.org/wiki/Cron)

## Author

- [Ronie Martinez](mailto:ronmarti18@gmail.com)