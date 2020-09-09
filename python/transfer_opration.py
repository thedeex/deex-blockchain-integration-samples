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

deex = DeEx(
    ["wss://node4p.deexnet.com/ws"]
)
set_shared_blockchain_instance(deex)


login_transfer_from="test"
login_transfer_to="test2"

accountFrom = Account(login_transfer_from, full=True)
accountTo = Account(login_transfer_to, full=True)



tx = TransactionBuilder(blockchain_instance=deex)

tx.appendOps(Transfer(**{
             "fee": {"amount": 0, "asset_id": "1.3.0"},  # will be filled in automatically. must be zero
             "from": accountFrom['id'], # sender ID
             "to": accountTo['id'],	# receiver ID
             "amount": {"amount": 1, "asset_id": "1.3.0"}, #Amount with decimals.  Sample: If asset has 2 decimals: 1 === 100
             "memo": "" # Encoded memo. Please read memo_encoding.py
         }))

deex.unlock();
tx.appendSigner(accountFrom['id'], "Your-Sender-Private-Key"); #Fiest parameter: ID of sender, second parameter: Private key of sender
signed = tx.sign()

print(signed)
# Print signed message (for debug)

f = tx.broadcast()
print(f)
# Print blockchain response.
