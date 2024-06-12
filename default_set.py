import matplotlib.pyplot as plt

def set():
  plt.rcParams["figure.figsize"] = [4,2.8]  # 図の縦横のサイズ([横(inch),縦(inch)])
  # plt.rcParams["figure.dpi"] = 100            # dpi(dots per inch)解像度
  plt.rcParams["figure.autolayout"] = False   # レイアウトの自動調整を利用するかどうか
  plt.rcParams["figure.subplot.left"] = 0.15  # 余白
  plt.rcParams["figure.subplot.bottom"] = 0.20# 余白
  plt.rcParams["figure.subplot.right"] =0.90  # 余白
  plt.rcParams["figure.subplot.top"] = 0.95   # 余白
  plt.rcParams["figure.subplot.wspace"] = 0.20# 図が複数枚ある時の左右との余白
  plt.rcParams["figure.subplot.hspace"] = 0.20# 図が複数枚ある時の上下との余白

  plt.rcParams["font.family"] = "serif"
  plt.rcParams["font.serif"] = ["Times New Roman"]
  plt.rcParams["font.size"] = 14
  plt.rcParams["mathtext.cal"] = "serif"      # TeX表記に関するフォント設定
  plt.rcParams["mathtext.rm"] = "serif"       # TeX表記に関するフォント設定
  plt.rcParams["mathtext.it"] = "serif:italic"# TeX表記に関するフォント設定
  plt.rcParams["mathtext.bf"] = "serif:bold"  # TeX表記に関するフォント設定
  plt.rcParams["mathtext.fontset"] = "cm"     # TeX表記に関するフォント設定

  plt.rcParams['xtick.direction'] = "in"
  plt.rcParams['ytick.direction'] = "in"

  plt.rcParams["axes.labelsize"] = 18
  plt.rcParams["axes.linewidth"] = 2.0
  plt.rcParams["axes.grid"] = False