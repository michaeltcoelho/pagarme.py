pagarme.py
========================================
[![Build Status](https://travis-ci.org/michaeltcoelho/pagarme.py.svg)](https://travis-ci.org/michaeltcoelho/pagarme.py)
[![Coverage Status](https://coveralls.io/repos/michaeltcoelho/pagarme.py/badge.svg)](https://coveralls.io/r/michaeltcoelho/pagarme.py)

O pagarme.py oferece integração com a API REST de pagamentos do Pagar.me utilizando Python.

> Durante a integração de sua aplicacão com o Pagar.me, consulte a referência da API,
> para estar ciente das informações necessárias para realizar a integracão.
> Referência da API [https://pagar.me/docs/api/](https://pagar.me/docs/api/)


Instalação
=========================================

Você pode instalar via pip:

```
pip install pagarmepy
```

ou clonando o repositório e instalando localmente:

```
git clone https://github.com/michaeltcoelho/pagarme.py
cd pagarme
pip install -r requirements.txt
python setup.py install
```

Testes
==========================================

Rodando os testes:

```bash
make test
```

Como usar
===========================================

Registre-se no Pagar.me e pegue sua `Chave da API` e `Chave de criptografia` do ambiente de testes.
[https://pagar.me/](https://pagar.me/).

Configurar o pagarme.py utilizando as próximas duas maneiras, ficará uma objeto global disponível da classe `PagarmeApi:class:` 
que é responsável por manipular as requisições e respostas do Pagar.me:
```python
from pagarme import api

api.configure({
    'api_key': 'Sua chave da API',
    'encryption_key': 'Sua chave de criptografia'})
```
Configure através de variáveis de ambiente:
```bash
export PAGARME_API_KEY='Sua chave da API'
export PAGARME_ENCRYPTION_KEY='Sua chave de criptografia'
```
Para não trabalhar com um objeto global:
```python
from pagarme import api, resources

my_api = api.PagarmeApi({
    'api_key': 'Sua chave da API',
    'encryption_key': 'Sua chave de criptografia'})

plan = resources.Plan({...}, api=my_api)
```

Criar um Plano
===========================================

## License

Written by Michael Coelho

Released under the MIT License: http://www.opensource.org/licenses/mit-license.php
