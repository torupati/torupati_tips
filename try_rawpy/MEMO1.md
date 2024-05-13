# はじめに

色のスペクトルを扱うためのライブライでcolour というのがあります。

スペクトル情報を扱う SpectralDistribution というクラスがの使い方をメモっておきます。


# 内容

## 数値データから作成する

下記の内容をフォローしています。

https://colour.readthedocs.io/en/latest/basics.html

### 反射スペクトルの値

波長と反射係数のペアから作れます。
numpy に似た構造をしていますが、引数の波長にはもとのデータにない波長を指定することもできます。


```
import colour

data = {
    500: 0.0651,
    520: 0.0705,
    540: 0.0772,
    560: 0.0870,
    580: 0.1128,
    600: 0.1360,
}
sd = colour.SpectralDistribution(data)

print(f"spectral density at wave length 550.5nm is {sd[550.5]}")
print(f"first 3 elements of the data is {sd[0:2]}")
print(f"shape of this is {sd.shape} {repr(sd.shape)}")
```

### カラーパッチ

Color Checker に含まれている Spectral Disbribution もあります。


### 証明

```
illuminant = colour.SDS_ILLUMINANTS["D65"]
print(type(illuminant))
```

### 描画する

```plot_signal_sd(sd)``` や ```plot_multi_sds([sd1, sd2])``` を使えます。

# まとめ

とりあえずこれでだましだまし使っていこうと思います。



