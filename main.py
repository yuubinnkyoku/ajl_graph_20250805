import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ticker import FuncFormatter
import numpy as np
import yaml # YAMLを扱うためのライブラリをインポート

# --- データの読み込み ---
# YAMLファイルを開き、内容を読み込む
# encoding='utf-8' を指定することで、日本語が正しく読み込まれる
with open('data.yaml', 'r', encoding='utf-8') as file:
    chart_data = yaml.safe_load(file)
# ----------------------

# 日本語フォントの設定（ご使用の環境に合わせてフォント名を変更してください）
plt.rcParams['font.sans-serif'] = ['Yu Gothic', 'Meiryo', 'TakaoGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 描画の準備
fig, ax = plt.subplots(figsize=(14, 8))

# データを抽出
labels = [f"{d['rank_info']}\n{d['school_name']}" for d in chart_data]
total_scores = [d['total_score'] for d in chart_data]
bar_indices = np.arange(len(chart_data))

# 背景の白いバーをプロット
ax.bar(bar_indices, total_scores, color='white', edgecolor='black', linewidth=1.2)

# バーの内部にテキストを配置し、区切り線を描画
for i, data in enumerate(chart_data):
    bottom = 0
    # YAMLから読み込んだ参加者リストがNoneでないことを確認
    participants = data.get('participants', [])
    if participants is None:
        participants = []
        
    num_participants = len(participants)
    bar_width = 0.8 # matplotlibのデフォルトのバーの幅
    
    # 参加者ごとに処理
    for j, participant in enumerate(participants):
        score = participant['score']
        name = participant['name']
        
        # スコアと名前の長さに応じてフォントサイズを動的に調整
        # 描画面積に比例するような計算式に変更
        name_len = len(name)
        if name_len == 0:
            name_len = 1

        # score / name_len の平方根に比例させることで、急激なサイズ変化を抑制
        font_size = 0.3 * np.sqrt(score / name_len)

        # 参加者名を表示
        ax.text(
            i,
            bottom + score / 2,
            name,
            ha='center',
            va='center',
            rotation=90,
            fontsize=font_size,
            color=participant['color'],
            fontweight='bold'
        )
        
        # 現在の参加者のスコアを加算
        bottom += score
        
        # 複数の参加者がいて、かつ最後の参加者でない場合に区切り線を描画
        if num_participants > 1 and j < num_participants - 1:
            ax.hlines(
                y=bottom, 
                xmin=i - bar_width / 2, 
                xmax=i + bar_width / 2, 
                colors='black', 
                linewidth=1.2
            )

# 各バーの上に合計スコアを表示
for i, score in enumerate(total_scores):
    ax.text(i, score + 1000, f'{score/1000:.1f}K', ha='center', va='bottom', fontsize=14, fontweight='bold')

# Y軸のフォーマットを 'K' 形式にする
def kilo_formatter(x, pos):
    return f'{int(x/1000)}K'
ax.yaxis.set_major_formatter(FuncFormatter(kilo_formatter))

# タイトルとサブタイトルの設定
fig.suptitle('AtCoder Junior League 2024 Winter - アルゴリズム部門', fontsize=18)
ax.set_title('筑波大学附属中学校 (23位)', fontsize=24, fontweight='bold', pad=20)

# X軸とY軸の各種設定
ax.set_xticks(bar_indices)
ax.set_xticklabels(labels, fontsize=12, ha='center', linespacing=1.5)
ax.tick_params(axis='x', length=0, pad=10)
ax.tick_params(axis='y', labelsize=12)

# Y軸の範囲とグリッド
ax.set_ylim(0, 58000)
ax.grid(axis='y', linestyle='-', color='gray', alpha=0.5)

# グラフの枠線を調整
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_color('black')

# レイアウトを調整して表示
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()