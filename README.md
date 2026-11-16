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
