from __future__ import absolute_import

from operator import itemgetter

mapping = {
    'has_header': True,
    'is_split': False,
    'bank': 'Bank Name',
    'currency': 'GBP',
    'delimiter': ',',
    'account': itemgetter('Field'),
    'account_id': itemgetter('Field'),
    'date': itemgetter('Field'),
    'type': itemgetter('Field'),
    'amount': itemgetter('Field'),
    'balance': itemgetter('Field'),
    'desc': itemgetter('Field'),
    'payee': itemgetter('Field'),
    'notes': itemgetter('Field'),
    'class': itemgetter('Field'),
    'id': itemgetter('Field'),
    'check_num': itemgetter('Field'),
}
