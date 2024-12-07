# MP3 Processor

A Python script for batch processing MP3 files that:
- Changes playback speed of audio files
- Splits long files into smaller segments
- Processes files recursively across folders
- Preserves folder structure in output

## Requirements

- Python 3.6 or higher
- pydub library
- ffmpeg (required by pydub for MP3 processing)

## Installation

1. Install Python dependencies:
```bash
pip install pydub
```

2. Install ffmpeg:
- **Windows**: 
  - Download from [ffmpeg website](https://ffmpeg.org/download.html)
  - Add to system PATH
- **macOS**:
  ```bash
  brew install ffmpeg
  ```
- **Linux**:
  ```bash
  sudo apt-get install ffmpeg
  ```

## Usage

1. Save the script as `mp3_processor.py`

2. Run the script:
```bash
python mp3_processor.py
```

3. When prompted, enter:
   - Full path to the folder containing MP3 files
   - Speed factor (e.g., 1.5 for 50% faster, 0.5 for 50% slower)
   - Maximum segment length in minutes (default: 15)

## Features

### Speed Adjustment
- Modify playback speed while preserving pitch
- Supports any speed factor (e.g., 0.5x, 1.5x, 2x)

### File Splitting
- Automatically splits files longer than specified duration
- Default maximum segment length: 15 minutes
- Customizable segment length
- Part numbers added to split files (e.g., "part001_", "part002_")

### Folder Processing
- Recursively processes all subfolders
- Maintains original folder structure in output
- Creates "processed_audio" folder for output
- Skips output folder to prevent reprocessing

### Error Handling
- Continues processing if individual files fail
- Displays error messages for problematic files
- Creates output folders as needed

## Output Structure

```
input_folder/
├── song1.mp3
├── subfolder/
│   └── song2.mp3
└── processed_audio/
    ├── speed_1.5x_song1.mp3
    └── subfolder/
        └── speed_1.5x_part001_song2.mp3
        └── speed_1.5x_part002_song2.mp3
```

## File Naming Convention

- Regular files: `speed_[factor]x_filename.mp3`
- Split files: `speed_[factor]x_part[number]_filename.mp3`

## Limitations

- Only processes MP3 files
- Requires sufficient disk space for output files
- Processing time depends on file size and CPU speed

## Troubleshooting

1. **"ffmpeg not found" error**:
   - Ensure ffmpeg is installed and in system PATH
   - Restart terminal/command prompt after installation

2. **"Permission denied" error**:
   - Check folder permissions
   - Run with appropriate privileges

3. **Memory issues with large files**:
   - Reduce segment length
   - Process fewer files at once

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - Feel free to use and modify for your needs.


# MP3プロセッサー

MP3ファイルを一括処理するPythonスクリプトです：
- 音声ファイルの再生速度を変更
- 長いファイルを小さなセグメントに分割
- フォルダを再帰的に処理
- 出力時にフォルダ構造を保持

## 必要条件

- Python 3.6以上
- pydubライブラリ
- ffmpeg（MP3処理用にpydubが必要とします）

## インストール

1. Python依存ライブラリのインストール：
```bash
pip install pydub
```

2. ffmpegのインストール：
- **Windows**：
  - [ffmpegウェブサイト](https://ffmpeg.org/download.html)からダウンロード
  - システムPATHに追加
- **macOS**：
  ```bash
  brew install ffmpeg
  ```
- **Linux**：
  ```bash
  sudo apt-get install ffmpeg
  ```

## 使用方法

1. スクリプトを`mp3_processor.py`として保存

2. スクリプトを実行：
```bash
python mp3_processor.py
```

3. プロンプトが表示されたら、以下を入力：
   - MP3ファイルが含まれるフォルダのフルパス
   - 速度係数（例：1.5で50%速く、0.5で50%遅く）
   - 最大セグメント長（分）（デフォルト：15分）

## 機能

### 速度調整
- ピッチを保持したまま再生速度を変更
- あらゆる速度係数に対応（例：0.5倍、1.5倍、2倍）

### ファイル分割
- 指定された長さを超えるファイルを自動分割
- デフォルトの最大セグメント長：15分
- セグメント長のカスタマイズ可能
- 分割ファイルにパート番号を追加（例："part001_"、"part002_"）

### フォルダ処理
- すべてのサブフォルダを再帰的に処理
- 出力時に元のフォルダ構造を維持
- 出力用に"processed_audio"フォルダを作成
- 再処理を防ぐため出力フォルダをスキップ

### エラー処理
- 個別のファイルが失敗しても処理を継続
- 問題のあるファイルのエラーメッセージを表示
- 必要に応じて出力フォルダを作成

## 出力構造

```
input_folder/
├── song1.mp3
├── subfolder/
│   └── song2.mp3
└── processed_audio/
    ├── speed_1.5x_song1.mp3
    └── subfolder/
        └── speed_1.5x_part001_song2.mp3
        └── speed_1.5x_part002_song2.mp3
```

## ファイル命名規則

- 通常のファイル：`speed_[係数]x_ファイル名.mp3`
- 分割ファイル：`speed_[係数]x_part[番号]_ファイル名.mp3`

## 制限事項

- MP3ファイルのみ処理可能
- 出力ファイル用の十分なディスク容量が必要
- 処理時間はファイルサイズとCPU速度に依存

## トラブルシューティング

1. **"ffmpeg not found"エラー**：
   - ffmpegがインストールされ、システムPATHに含まれていることを確認
   - インストール後、ターミナル/コマンドプロンプトを再起動

2. **"Permission denied"エラー**：
   - フォルダのアクセス権限を確認
   - 適切な権限で実行

3. **大きなファイルでのメモリ問題**：
   - セグメント長を短くする
   - 一度に処理するファイル数を減らす

## 貢献

問題点や機能改善のリクエストはお気軽にお寄せください！

## ライセンス

MITライセンス - 自由に使用・改変いただけます。