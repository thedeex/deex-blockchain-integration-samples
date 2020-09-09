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

from deexbase.memo import (
    get_shared_secret,
    _pad,
    _unpad,
    encode_memo,
    decode_memo
)


test_case={
     'nonce': '8555724032490455626',	# Nonce use random string + microtime. Every request must have uniq nonce
     'plain': 'abcdefghijÛ', # padding limit and last character is unicode
     'to': 'DX82y5ZQiKeWG8HLxukKAQtDywARAjQjPGLC9b6DYtL5LTj4fZ1o',	# Receiver public key (public address)
     'wif': '5KR8jzysz2kbYy3TkL3x6NRxfNXwQUWyeVAF5ZagxdqKMawGgXG'}	# Sender PRIVATE key. (active)




enc = encode_memo(PrivateKey(test_case["wif"]),
                  PublicKey(test_case["to"],prefix="DX"),
                  test_case["nonce"],
                  test_case["plain"])

print(enc)

//Result encoded message.