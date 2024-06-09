def XRD_graph(self):
  self.ax.set_xlabel(r"$ 2\theta $ [deg]")
  self.ax.set_ylabel("Intensity [arb.units]")
  self.ax.set_xlim(30,90)
  self.ax.set_ylim(0,1)
  self.fig.canvas.draw()
  self.ax.minorticks_on() # 補助目盛有効
  self.ax.tick_params(axis="y", which="minor", left=False, right=False)
  self.ax.tick_params(axis="x", which="minor", top=True, bottom=True)
  self.ax.tick_params(labelbottom=True, labelleft=False, labelright=False, labeltop=False) # 軸ラベルの表示非表示の設定
  self.ax.tick_params(bottom=True, left=False, right=False, top=True) #目盛の表示非表示の設定
  self.ax.tick_params(which = "major", width = 1.5, length = 8) #主目盛の太さ長さの設定
  self.ax.tick_params(which = "minor", width = 1.5, length = 4)
  # boxdic = {
  #   "boxstyle" : "square",
  #   "linestyle" : "-",
  #   "facecolor" : "white",
  #   "linewidth" : 1.0
  # }
  # text_XRD = ax.text(0.9, 0.9, "XRD", ha="center", va="top", transform=ax.transAxes, bbox=boxdic)
  # try:
  #   bbox_XRD = text_XRD.get_window_extent().transformed(ax.transData.inverted())
  #   print(bbox_XRD)
  # except:
  #   print("error")
  # self.add_text(self.ax, "XRD", 0.9, 0.9, self.contentsList)
  self.add_text(0.9, 0.9, "XRD")
