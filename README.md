# yolo-quickstart1

[Install Ultralytics](https://docs.ultralytics.com/quickstart) を参考にして
YOLO26(YOLO26n)を使ってみる。

テストは
NVIDIA GeForce RTX 3070 Ti Laptop GPU, 8192MiB
の載っているホストで行ったけど、
GPU メモリはほとんど使わない。

## 実行

```sh
uv sync
uv run poe first_predict
# ↑ `yolo predict model=yolo26n.pt` を実行する。
# - yolo26n.pt をプロジェクトルートにダウンロードする
# - ultralytics パッケージに同梱されている bus.jpg と zidane.jpg に対して
#   predict (inference) を行って、結果を runs/detect/predict/ に出力

uv run poe ex0
#  同じようなことをPythonスクリプトで実行する
# プロジェクトルートにbus.jpgをダウンロードし、runs/detect/predict-n/ に結果を出力する
```

### アレンジ

(以下、venv 環境を activate してるものとする)

```sh
# すでにある画像ファイルに対して predict を行って、
# 結果を指定された場所に出力する
poe download_examples
poe ex1
```

## CPUの仕様を強制する

GPU のあるホストでも環境変数で制御できる。

例:

```sh
CUDA_VISIBLE_DEVICES=-1 uv run poe first_predict
```

## 注意: yolo cli の出力先

`yolo setting` はグローバル設定なので注意。

設定一覧:
[Ultralytics Settings and Configuration](https://docs.ultralytics.com/usage/settings)

## 注意: yolo cli の引数

サブコマンド式じゃないので注意

「`yolo TASK MODE ARGS` で TASK と ARGS は省略可能」という「第一引数が省略可能」なのが落とし穴で、
オプション式でないのも変。

[Command Line Interface | Ultralytics](https://docs.ultralytics.com/usage/cli)

## おまけ: セグメンテーションを yolo cli で実行してみる

物体検出(Bounding Box)以外にも

- インスタンスセグメンテーション(-seg) - 画像内の物体を一つずつ識別し、それぞれの輪郭を切り出す
- セマンティックセグメンテーション(-sem) - 画像のすべてのピクセルに対して、何のクラスに属するかを判定する

というモデルがあるのでテスト

```sh
poe bounding_box
poe segment
poe semantic
```

出力は `runs/` の下に出る。
