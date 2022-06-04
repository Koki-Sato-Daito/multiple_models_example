## 複数モデルをシリアライズするView
- https://qiita.com/s17161278/items/c6c7c5f57cb99a5ccd68

## インストール
```
# クローン
$ git clone https://github.com/Koki-Sato-Daito/multiple_models_example.git
$ cd multiple_models_example/

# 仮想環境作成と依存パッケージインストール
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# 環境変数のセット
# https://miniwebtool.com/ja/django-secret-key-generator/
$ echo SECRET_KEY='seacret_key' > .env

# マイグレーションとfixtureの準備
$ python manage.py migrate
$ python manage.py loaddata items.json
$ python manage.py loaddata coupons.json

# サーバ起動
$ python manage.py runserver
```
- http://localhost:8000/api/items/ にアクセスするとレスポンスを確認できます。
