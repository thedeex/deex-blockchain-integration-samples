import unittest
import os
from pprint import pprint
from itertools import cycle
from deexbase.account import BrainKey, Address, PublicKey, PrivateKey
from deexbase import transactions, memo, account, operations, objects
from deexbase.objects import Operation
from deexbase.signedtransactions import Signed_Transaction

from deex.transactionbuilder import TransactionBuilder
from deexbase.operations import Transfer

from deex import DeEx, storage
from deex.instance import set_shared_blockchain_instance
from deex.account import Account

from deexbase.memo import (
    get_shared_secret,
    _pad,
    _unpad,
    encode_memo,
    decode_memo
)

deex = DeEx(
    ["wss://node4p.deexnet.com/ws"]
)
set_shared_blockchain_instance(deex)



account = Account("--your-account-login--", full=True)
print(account['id'])
print(account.balance("1.3.0"))

