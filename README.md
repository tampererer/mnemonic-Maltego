# [mnemonic] Maltego Local Transforms
Maltego Local Transforms to use mnemonic Passive DNS - https://passivedns.mnemonic.no/

# Prerequisites
- Python 2.7.x + requests, re module
- Python 3.6.x will probably work.

# 必要なもの
- Python 2.7.x + requests, re モジュール
- Python 3.6.x でもたぶん動作します。

# Setup
- Put all python files into your working directory. (e.g. C:\Maltego\Transforms\mnemonic)
- Open mnemonic.mtz to import Maltego configuration.
- The current configuration uses the following directories, so you may have to change them according to your environment. (Maltego -> Transforms -> Transform Manager)  
  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\mnemonic

# セットアップ
- 全てのPythonファイルを、このTransform用に作ったディレクトリに置いてください。（例： C:\Maltego\Transforms\mnemonic）
- mnemonic.mtz を開いて、Maltegoの設定をインポートしてください。
- mtzファイルに含まれる設定では、下記のディレクトリが指定されていますが、自分の環境に合わせて変更してください。（Maltego -> Transforms -> Transform Manager）

  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\mnemonic

# Transforms
- [mnemonic] domain_to_ip  
Input: Domain  
Output: IP address 
<img src="https://user-images.githubusercontent.com/16297449/42553671-b78fc616-851c-11e8-8a0c-02424785a71e.png" width="600">

- [mnemonic] ip_to_domain  
Input: IP address  
Output: Domain  
<img src="https://user-images.githubusercontent.com/16297449/42553756-15e86d30-851d-11e8-9993-14c9bfa8cd13.png" width="600">
