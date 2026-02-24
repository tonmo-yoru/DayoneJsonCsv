import json
import csv

# JSONファイルを読み込む
with open('Journal.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 変換後のデータを保存するリスト
output_data = []

for entry in data['entries']:
    # 日付の取得
    date = entry.get('creationDate', '')
    
    # 本文を取得し、タイトルと内容に分割
    full_text = entry.get('text', '')
    lines = full_text.split('\n', 1) # 最初の一行目で分割
    
    title = lines[0] if len(lines) > 0 else "無題"
    content = lines[1] if len(lines) > 1 else ""

    output_data.append([date, title, content])

# CSVとして保存
with open('notion_import.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Title', 'Content']) # ヘッダー
    writer.writerows(output_data)

print("変換が完了しました！ notion_import.csv をNotionへインポートしてください。")