# plantbot(更新中)
Raspberry Piを使用した自動水やりシステムです。  
土壌湿度や温湿度、水位を監視し、必要に応じてポンプを制御して自動で散水を行います。

# 概要図
<img width="947" height="633" alt="image" src="https://github.com/user-attachments/assets/67a2ebca-8839-4620-86cc-9b2da009e1b2" />

# 動作環境
- Raspberry Pi 4 Model B 4GB
- Raspberry Pi OS
  - Debian GNU/Linux 13 (trixie)
 
# 使用部品

### 温湿度センサー
- DHT11
- 抵抗：3.3KΩ

### 土壌湿度センサー
- YL-69
- YL-38

### 水位センサー
- 無印

### ポンプ制御回路
- 給水ポンプ
- リレー：SRD-05VDC-SL-C
- トランジスタ：2SC1815Y
- ダイオード：1N4148
- 抵抗：1KΩ

### その他
- ピンヘッダ(2×20 40pin)
- JST XH × 3
- JST VH × 1

# システム構成
- 土壌湿度を監視
- 閾値以下でポンプをON
- 一定時間散水
- 水位低下時はポンプ停止

# ディレクトリ構成
```txt
plantbot/
├── src/        # 制御プログラム
├── service/    # systemdサービス設定
├── 3D_models/  # 3Dモデル(stl)
├── pcb_data/   # 回路基板データ
└── README.md
```
