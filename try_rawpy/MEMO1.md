# はじめに

色のスペクトルを扱うためのライブライでcolour というのがあります。

スペクトル情報を扱う SpectralDistribution というクラスがの使い方をメモっておきます。


# 内容

## 数値データから作成する

下記の内容をフォローしています。

https://colour.readthedocs.io/en/latest/basics.html

### 黒体輻射のスペクトルをプロットしてみる

放射スペクトルの情報を```colour.colorimetry.spectrum.SpectralDistribution```に保持するようにしてみます。
ある色温度のスペクトル情報のインスタンスは、波長と値のペアを持つ辞書から作成できます。
また、黒体輻射のプランクの公式は関数が用意された関数で計算できるのでそのまま利用させていただきました。

numpy に似た構造をしていますが、引数の波長にはもとのデータにない波長を指定することもできます。
波長について値を補間して計算してくれます。

```
import colour
import scipy
import matplotlib.pyplot as plt

C1 =  2 * math.pi * h * c ** 2 # 2 * math.pi * PLANCK_CONSTANT * LIGHT_SPEED ** 2 = 3.741771e-16 
C2 =  h * c / k # PLANCK_CONSTANT * LIGHT_SPEED / BOLTZMANN_CONSTANT = 1.4388e-2

temperature = 5000
wavelengths = colour.colorimetry.spectrum.SpectralShape(350, 850, 5).range()
sd5000k = colour.colorimetry.spectrum.SpectralDistribution(
    name='{0}K Blackbody'.format(temperature),
    data=dict(zip(wavelengths,
                  colour.colorimetry.planck_law(wavelengths * 1e-9, temperature, C1, C2, 1))))

print("wavelength: ", sd5000k.wavelengths)
print("values: ", sd5000k.values)

print(f"Radiation of {temperature} K bloack body at 503[K] is {sd5000k[503]:12.4e}")

fig, ax = colour.plotting.plot_single_sd(sd5000k, cmfs = 'CIE 1931 2 Degree Standard Observer',)
fig.savefig("ct5000k_sd.png")
```


波長とスペクトルのペアから作れます。スペクトルは放射、証明、反射係数など全ての場合に共通して使えるようです。
例えば照明情報として下記は ```colour.colorimetry.spectrum.SpectralDistribution```が出力されます。

```
illuminant = colour.SDS_ILLUMINANTS["D65"]
print(type(illuminant))
```

また、波長分解能など内部のデータがことなるときに、align とすると、そのSpectralShape に保管して割り当てなおしてくれるようです。
そして、スペクトル同士の加減乗除の計算ができるらしいです。

描画には単一のスペクトルと、複数のプロットを比較する場合で```plot_signal_sd(sd)``` や ```plot_multi_sds([sd1, sd2])``` がそれぞれ使えます。


### カラーパッチ

Color Checker に含まれている Spectral Disbribution もライブラリに含まれていました。
まず、下記でカラーチェッカーを保存できます。

```
fig, ax = colour.plotting.plot_single_colour_checker()
fig.savefig('color_checker.png')
```

```
checker = colour.characterisation.SDS_COLOURCHECKERS.get('BabelColor Average')
sd_red = checker.get('Dark Skin') 
```

# まとめ

とりあえずこれでだましだまし使っていこうと思います。

- Find color temperature from spectral response
  https://stackoverflow.com/questions/62776729/find-color-temperature-from-spectral-response

- Converting a Spectrum to a Colour
  https://scipython.com/blog/converting-a-spectrum-to-a-colour/

- 日本語でカラーチェッカーの分光反射率の取得方法を記述
 https://yamagishi-2bit.blogspot.com/2022/01/colour-science-spectraldistribution.html

- HDRの計算
https://www.colour-science.org/colour-hdri/

- Colour Tutorial
  https://colab.research.google.com/drive/1Im9J7or9qyClQCv5sPHmKdyiQbG4898K

- Colour 
  https://readthedocs.org/projects/colour/downloads/pdf/latest/