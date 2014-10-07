Python Chatwork-API client library
==================================

Chatwork株式会社が提供しているサービス、Chatworkにてプレビュー版として公開されているAPIの
Python版クライアントライブラリです。


Installation
--------------

次のコマンドで、インストールできます。（virtualenvを使用して下さい）

.. code:: bash

   git clone https://github.com/attakei/python-chatwork.git
   cd python-chatwork
   python setup.py install


Usage
-----


.. code:: python

   >>> import chatwork

   >>> # 1. 初期化
   >>> user = chatwork.ChatworkUser('user_api_token')

   >>> # 2. ユーザ情報取得
   >>> data = user.me()
   >>> data['account_id']
   123


Official Links
--------------

* Chatwork : http://www.chatwork.com/
* Chatwork API : http://developer.chatwork.com/ja/index.html
