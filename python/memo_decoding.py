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
	'from': 'DX82y5ZQiKeWG8HLxukKAQtDywARAjQjPGLC9b6DYtL5LTj4fZ1o',	# Sender public address (public key)
     'message': '3c4c9b610201f5b17b6f858d19899a02a12fce274aedbb49ad866d79b75e3967', (Encoded message)
     'nonce': '8555724032490455626', 
     'plain': 'abcdefghijÛ', # padding limit and last character is unicode
     'to': 'DX82y5ZQiKeWG8HLxukKAQtDywARAjQjPGLC9b6DYtL5LTj4fZ1o',	# public key receiver
     'wif': '5KR8jzysz2kbYy3TkL3x6NRxfNXwQUWyeVAF5ZagxdqKMawGgXG'} # Private key of receiver





dec = decode_memo(PrivateKey(test_case["wif"]),
                  PublicKey(test_case["to"],prefix="DX"),
                  test_case["nonce"],
                  test_case["message"])

print(dec)
# Decoded memo message