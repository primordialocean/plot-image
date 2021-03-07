# plot-image
分析位置をSEMで撮影した画像にプロットすることができます．

## 実行環境
- Python 3.8.5
以下のライブラリが必要です
- matplotlib
- matplotlib-scalebar
- numpy
- pandas
- openpyxl
- adjustText

## 使い方
`input.xlsx`に値を入力する．
- Sample: 元画像の入っているフォルダの`img_`より先の名前．
- Crystal: 分析点の名前．
- Point: 分析点の番号（必ずしも必要ではありません）．
- Filename: プロットする画像ファイルのファイル名．
- Magnification: 画像ファイルの倍率．電子顕微鏡像では倍率を12 cmx10 cmの画面に表示した場合で計算しているので，光学顕微鏡など他の画像ファイルで使用する場合は計算式を書き換える必要があります．
- X, Y: 分析点の画像上の座標．IrfanviewやImageJなどで読み取ってください．
- Mg#: 例としてorthopyroxeneを使用しているのでMg#となっていますが，分析対象に応じて自由に変えて頂いて構いません．変更する場合は`make_points.py`のpointsの所を書き換えてください．

`img_input`と`img_output`というフォルダを同じディレクトリに作成し，`img_input`中にプロットする画像を配置します．この際の画像は`tif`形式が標準となっています（jpg等他の形式を扱いたい場合は`make_points.py`を書き換えてください．）

ターミナルで`make_points.py`を実行すると，`img_output`に加工済みの画像がjpg形式で保存されます．
