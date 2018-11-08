#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Production"

import doccron


def test_tokenizer():
    assert [['*'] * 6] == list(doccron.tokenize('* * * * *'))
    assert [['*'] * 6] == list(doccron.tokenize('* * * * * *'))
    assert [['*'] * 6] == list(doccron.tokenize('*  * * * *'))
    assert [['*'] * 6, ['*'] * 6] == list(doccron.tokenize('* * * * *%* * * * * *'))
    assert [['*'] * 6, ['*'] * 6] == list(doccron.tokenize('* * * * *\n* * * * * *'))
    assert [['*'] * 6] * 2 == list(doccron.tokenize('''* * * * *
    * * * * *'''))
    assert [['0,15,30,45', '0,6,12,18', '1,15,31', '*', '1,2,3,4,5', '*']
            ] == list(doccron.tokenize('0,15,30,45 0,6,12,18 1,15,31 * 1,2,3,4,5 *'))
    assert [['*'] * 7] == list(doccron.tokenize('*  * * * *', quartz=True))
