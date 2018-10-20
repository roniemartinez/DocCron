# DocCron

Schedule with Docstring

## Description

Cron scheduler inspired by [doctest](https://en.wikipedia.org/wiki/Doctest)

## Example

Run `hello()` at every 2nd minute.

```python
import time

import doccron


def hello():
    """
    */2 * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S'), "hello world")


if __name__ == '__main__':
    doccron.run_jobs()

```

## TODO

- [ ] Support [Non-standard characters](https://en.wikipedia.org/wiki/Cron#Non-standard_characters)
- [ ] Support [Nonstandard predefined scheduling definitions](https://en.wikipedia.org/wiki/Cron#Nonstandard_predefined_scheduling_definitions)
- [ ] Support [Quartz format](http://www.quartz-scheduler.org/documentation/quartz-2.x/tutorials/crontrigger.html)

## References

- [Cron Format](http://www.nncron.ru/help/EN/working/cron-format.htm)
- [Wikipedia - Cron](https://en.wikipedia.org/wiki/Cron)

## Author

- [Ronie Martinez](mailto:ronmarti18@gmail.com)