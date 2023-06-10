# はじめに

python でargparse で引数の定義を行い、コマンドラインから引数の値を入力するのに使っていました。
同じものをプログラム内部でパラメータで渡したいと思ってて方法を調べました。

# 方法

### (A) parse_args() に引数を直接入れる

これが正解だと思います。

以下のようなParser が作られていて、shellから引数を指定します。

```python:test01.py
import argparse
parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('filename')
parser.add_argument('-c', '--count', type=int)
parser.add_argument('-v', '--verbose', action='store_true')

args1 = parser.parse_args()
print('args1=', args1)
```

実行すると下記のようになります。

```
$ python3 test01.py -c 100 -v aaa
args1= Namespace(count=100, filename='aaa', verbose=True)
```

これを以下のようにしても同じです。

```python:test02.py
from test01 import parser

args2 = parser.parse_args("-c 100 -v aaa".split())
print('args2=', args2)
```

```
$ python3 test02.py
args2= Namespace(count=100, filename='aaa', verbose=True)
```

### (B) 直接namespace やclass instance を作る

最初、こちらで行っていました。ご苦労なことですが、同じものを作ろうという作戦です。

```
from types import SimpleNamespace
args3 = SimpleNamespace(count=100, filename="aaa", verbose=True)

print('args3=', args3)
```

実行すると以下のように。namespace の n　が小文字になっていました。

```
$ python3 test03.py
args3= namespace(count=100, filename='aaa', verbose=True)
```

これでも args3.filename のように参照できるので、args を渡した関数でプログラムは正常に動作します。

そもそも直接参照できるようにだけすなら、クラスを使ってもできます。

```python:test04.py
class Cls():
    pass

args = Cls()
args.count=100
args.filename="aaa"
args.verbose=True
print('args.count=',args.count)
print('args.filename=',args.filename)
print('args.verbose=',args.verbose)
```

この場合namespace ではないですが、同じように参照できます。

```

```

https://stackoverflow.com/questions/37161275/what-is-the-difference-between-simplenamespace-and-empty-class-definition



実際には、引数の設定はたくさんあり、default 値を設定している場合もあります。それを呼び出す側で全て書くのはバグの元なので(B)はよろしくないなと後で思いました。


# まとめ

普段はシェルから引数で渡しているものをプログラム内で指定する方法として、arg_parse()するときに引数の文字列をそのまま入れればよいということで解決できました。おまけとして、parse_args で作られるnamespace なるものと似たものをtypes.SimpleNamespace で作る方法も確認できました。

来週も生き延びることができるかな。。。

(2023/06/10)


