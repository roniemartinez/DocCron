# List of changes to DocCron

## Unreleased

## 1.5.0 - 2020-03-22
### Added
- Support @every interval (#14)

### Changed
- Drop pytz and tzlocal for python-dateutil

## 1.4.1 - 2020-03-15
### Added
- Include isort, black, flake8, mypy, safety, bandit 

### Changed
- Use poetry

## 1.4.0 - 2019-11-24
### Added
- OSX tests
- Python linter

### Changed
- Move metadata to setup.cfg

### Removed
- Drop Python 2 support

## 1.3.1 - 2019-04-03
### Added
- Include examples (#28)
- Include doccron/timezone.py to MANIFEST (#28)

## 1.3.0 - 2019-04-03
### Added
- Timezone-awareness (#24)

### Removed
- Drop Python 3.4 support

## 1.2.1 - 2019-01-12
### Changed
- Updated copyright

### Fixed
- Refactor tests

## 1.2.0 - 2018-11-13
### Added
- Embed into `/etc/crontab::` literal blocks (#20)

## 1.1.2 - 2018-11-13
### Fixed
- Remove DeprecationWarning for collections module (#21)

## 1.1.1 - 2018-11-09
### Changed
- Add downloads shield

## 1.1.0 - 2018-11-08
### Added
- Fast skipping in datetime odometer (#17)

## 1.0.0 - 2018-10-23
### Added
- Support for Quartz format by adding seconds column (#4)

## 0.4.1 - 2018-10-23
### Fixed
- Bump version to fix failed builds on Travis CI and AppVeyor due to October 21 Github issue

## 0.4.0 - 2018-10-22
### Added
- Support @midnight predefined schedule (#9)

### Removed
- Drop unused/untested code for 100% code coverage

## 0.3.0 - 2018-10-21
### Added
- Support for comments (#) and percent separator (%)
- 100% code coverage
- Support non-standard characters (#3)

## 0.2.0 - 2018-10-20
### Added
- Support nonstandard predefined scheduling definitions (#2)

## 0.1.0 - 2018-10-20
### Added
- README, LICENSE, CHANGELOG
- Support Standard (5) and Extended (6) Formats
- Support abbreviated names, lists, ranges and steps
- Show example application
- Add setup.py and deploy to PyPI