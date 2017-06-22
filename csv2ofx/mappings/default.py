from __future__ import absolute_import

from operator import itemgetter

mapping = {
    'has_header': True,
    'is_split': False,
    'bank': 'Bank',
    'currency': 'GBP',
    'delimiter': ',',
    'account': itemgetter('Account'),
    'date': itemgetter('Date'),
    'amount': itemgetter('Amount'),
    'desc': itemgetter('Reference'),
    'payee': itemgetter('Description'),
    'notes': itemgetter('Notes'),
    'check_num': itemgetter('Num'),
    'id': itemgetter('Row'),
}
