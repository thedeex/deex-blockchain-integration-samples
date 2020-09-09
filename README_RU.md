## **Интеграция DEEX Blockchain в вашу биржу**

Адрес DEEX биржи: [https://deex.exchange/](https://deex.exchangу)




### Интеграция между блокчейн платформами на текущее время существует в двух вариантах:

- Вариант первый, система без поддержки дополнительных полей\примечаний. Например Bitcoin, ETH. В данном случае, для интеграции, система вынуждена предоставлять для каждого депозита новый адрес для каждого пользователя.

- Вариант второй, блокчейн поддерживает возможность передачи дополнительного поля. комментария. Общепринятое обозначение "Memo".

**DEEX инфраструктура разработана по конструкии "второго варианта". Таким образом, Шлюз имеет единый кошелек, и все входящие операции будут приходить с разным коментарием. В комментарие допустимо указывать любые языки.  Комментарий шифруется и передается получателю, где получатель его расшифровывает. **

**Комментарии полностью конфиденциальны.**

**Внимание: Все комиссии сети, должны быть оплачены токеном DEEX**

Комиссии сети расположены по адресу [https://blockchain.deex.exchange/networkfees](https://blockchain.deex.exchange/networkfees)

## Установка библиотеки и зависимостей.

### Официальная библиотека расположена по адресу. [https://github.com/thedeex/python-deex](https://github.com/thedeex/python-deex)

## Python

### Установка: 

- $ sudo apt-get install libffi-dev libssl-dev python-dev python3-dev python3-pip
- $ git clone https://github.com/thedeex/python-deex/
- $ cd python-deex
- $ python3 setup.py install --user

##  Nodejs

``Soon``

## Проверка и считывание новых операций с последнего запроса и расшифровка значений.

### Python

**Пример:  [https://github.com/thedeex/deex-blockchain-integration-samples/tree/master/python/operations_history.py](https://github.com/thedeex/deex-blockchain-integration-samples/tree/master/python/operations_history.py)**

Передаваемые параметры:

- from: имеет формат 1.11.*. (Где номер - ID с последнего обработанного запроса)
- limit Количество результатов за один запрос. Не более 100.

**На данный запрос приходит ответ.**

``[
{'id': '1.11.1', 'op': [0, {'fee': {'amount': 1013, 'asset_id': '1.3.0'}, 'from': '1.2.1', 'to': '1.2.2', 'amount': {'amount': 1, 'asset_id': '1.3.1'}, 'memo': {'from': 'DX000000000000000000000', 'to': 'DX111111111111111111111', 'nonce': '408937899221506', 'message': 'ENCODED_MEMO_MESSAGE'}, 'extensions': []}], 'result': [0, {}], 'block_num': 4708554, 'trx_in_block': 0, 'op_in_trx': 0, 'virtual_op': 490},
......
]``


- Ключ ID: идентификатор операции (используется для фильтрации запроса)
- Сумма предоставлена с учетом символов после запятой. таким образом, если Ассет имеет 2 символа, наша сумма равна "0.01".

**- Memo расшифровывается согласно примеру: [https://github.com/thedeex/deex-blockchain-integration-samples/tree/master/python/memo_decoding.py](https://github.com/thedeex/deex-blockchain-integration-samples/tree/master/python/memo_decoding.py)**

В данный скрипт требуется передать параметры с ключа memo:


``{'from': 'DX000000000000000000000', 'to': 'DX111111111111111111111', 'nonce': '408937899221506', 'message': 'ENCODED_MEMO_MESSAGE'}``

Для расшифровки значений, требуется предоставить приватный ключ получателя.

### Nodejs
``soon``

## Отправка операций

### Python


**Запрос на отправку средств происходит согласно примеру: [https://github.com/thedeex/deex-blockchain-integration-samples/tree/master/python/transfer_opration.py](https://github.com/thedeex/deex-blockchain-integration-samples/tree/master/python/transfer_opration.py)**

Требуемые параметры для отправки:

 - Логин получателя
 - Логин отправителя
 - Приватный ключ отправителя
 - Сумма перевода
 - ID монеты для перевода.
 
### Nodejs
``soon``


## Получение данных о пользователе (идентификатор,балансы )

### Python

**Пример: [https://github.com/thedeex/deex-blockchain-integration-samples/tree/master/python/read_account_data.py](https://github.com/thedeex/deex-blockchain-integration-samples/tree/master/python/read_account_data.py)**

### Nodejs
``soon``


## Получение данных о монете (Идентификатор, количество значений в дробной части)

### Python

**Пример: [https://github.com/thedeex/deex-blockchain-integration-samples/tree/master/python/read_asset_data.py](https://github.com/thedeex/deex-blockchain-integration-samples/tree/master/python/read_asset_data.py)**

### Nodejs
``soon``
