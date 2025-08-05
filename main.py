import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ticker import FuncFormatter
import numpy as np

# 日本語フォントの設定（ご使用の環境に合わせてフォント名を変更してください）
# 使用可能なフォントは次のコードで確認できます:
# [f.name for f in fm.fontManager.ttflist if 'Gothic' in f.name]
plt.rcParams['font.sans-serif'] = ['Yu Gothic', 'Meiryo', 'TakaoGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# グラフの元になるデータ
# 注意: 複数人のスコアの内訳は画像からのおおよその推定値です。
#       正確なグラフを作成するには、ここのデータを実際の値に置き換えてください。
chart_data = [
    {
        'rank_info': '18th\n(n=5)',
        'school_name': '岡山県立倉敷\n天城中学校',
        'total_score': 52800,
        'participants': [
            {'name': 'michikusamichiya', 'score': 24000, 'color': '#8B4513'},
            {'name': 'Sunshine28aki', 'score': 7000, 'color': 'black'},
            {'name': 'yuki_mateki', 'score': 7000, 'color': 'black'},
            {'name': 'Nykci', 'score': 8000, 'color': 'black'},
            {'name': 'bigigura', 'score': 6800, 'color': 'black'},
        ],
    },
    {
        'rank_info': '19th\n(n=1)',
        'school_name': '安曇野市立穂高\n東中学校',
        'total_score': 52500,
        'participants': [
            {'name': 'hidehico', 'score': 52500, 'color': 'green'},
        ],
    },
    {
        'rank_info': '20th\n(n=1)',
        'school_name': '渋谷教育学園\n渋谷中学校',
        'total_score': 45800,
        'participants': [
            {'name': 'toxireh', 'score': 45800, 'color': '#A52A2A'},
        ],
    },
    {
        'rank_info': '21st\n(n=7)',
        'school_name': '東京都立武蔵高等学校\n附属中学校',
        'total_score': 44700,
        'participants': [
            {'name': 'Fruit_sugar', 'score': 25000, 'color': '#A52A2A'},
            {'name': '3110kounotori', 'score': 7000, 'color': 'black'},
            {'name': 'applefrisk', 'score': 6700, 'color': 'black'},
            {'name': 'spbob8y', 'score': 6000, 'color': 'black'},
            # 他の参加者はスコアが小さいため省略
        ],
    },
    {
        'rank_info': '22nd\n(n=1)',
        'school_name': '仙台市立仙台青陵\n中等教育学校',
        'total_score': 42900,
        'participants': [
            {'name': 'nowf41', 'score': 42900, 'color': '#A52A2A'},
        ],
    },
    {
        'rank_info': '23rd\n(n=4)',
        'school_name': '筑波大学附属中学校',
        'total_score': 38000,
        'participants': [
            {'name': 'yuubinnkyoku', 'score': 20000, 'color': '#A52A2A'},
            {'name': 'Meis_Meiko', 'score': 7000, 'color': 'black'},
            {'name': 'lemonydrink', 'score': 6000, 'color': 'black'},
            # 他の参加者はスコアが小さいため省略
        ],
    },
    {
        'rank_info': '24th\n(n=1)',
        'school_name': '高松市立協和中学校',
        'total_score': 30900,
        'participants': [
            {'name': 'friedrice0', 'score': 30900, 'color': '#A52A2A'},
        ],
    },
    {
        'rank_info': '25th\n(n=1)',
        'school_name': '江東区立第二\n大島中学校',
        'total_score': 30700,
        'participants': [
            {'name': 'Kosei0506', 'score': 30700, 'color': '#A52A2A'},
        ],
    },
    {
        'rank_info': '26th\n(n=1)',
        'school_name': '海城中学校',
        'total_score': 26900,
        'participants': [
            {'name': 'masa0118', 'score': 26900, 'color': '#A52A2A'},
        ],
    },
    {
        'rank_info': '27th\n(n=1)',
        'school_name': '町田市立つくし野中学校',
        'total_score': 26100,
        'participants': [
            {'name': 'jaae', 'score': 26100, 'color': '#A52A2A'},
        ],
    },
     {
        'rank_info': '28th\n(n=1)',
        'school_name': '三豊市立高瀬中学校',
        'total_score': 25200,
        'participants': [
            {'name': 'tyokousagi', 'score': 25200, 'color': '#A52A2A'},
        ],
    },
]

# 描画の準備
fig, ax = plt.subplots(figsize=(14, 8))

# データを抽出
labels = [f"{d['rank_info']}\n{d['school_name']}" for d in chart_data]
total_scores = [d['total_score'] for d in chart_data]
bar_indices = np.arange(len(chart_data))

# 背景の白いバーをプロット
ax.bar(bar_indices, total_scores, color='white', edgecolor='black', linewidth=1.2)

# バーの内部にテキストを配置
for i, data in enumerate(chart_data):
    bottom = 0
    # 参加者が1人の場合と複数人の場合でフォントサイズを調整
    num_participants = len(data['participants'])
    for participant in data['participants']:
        score = participant['score']
        name = participant['name']
        
        # フォントサイズをスコアに応じて動的に変更
        if num_participants == 1:
            font_size = 28 # 1人の場合は大きく
        else:
            font_size = 10 + score / 2000 # 複数人はスコアに応じて調整
            if font_size > 20: font_size = 20 # 上限

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
        bottom += score

# 各バーの上に合計スコアを表示
for i, score in enumerate(total_scores):
    ax.text(i, score + 500, f'{score/1000:.1f}K', ha='center', va='bottom', fontsize=14, fontweight='bold')

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
ax.tick_params(axis='x', length=0, pad=10) # X軸の目盛り線を消す
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
plt.tight_layout(rect=[0, 0, 1, 0.96]) # suptitleとの重なりを避ける
plt.show()