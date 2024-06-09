from typing import List, Dict
import matplotlib.pyplot as plt

def remove_content(contentsList):
  removeList = [content for content in contentsList if content["selected"] == True]
  for content in removeList:
    # print(content["value"])
    content["value"].remove()
  return [content for content in contentsList if content["selected"] == False], [content for content in contentsList if content["selected"] == True]

def select_content(data, contentsList):
  for content in contentsList:
    content["selected"] = False
    if content["value"] == data["value"]:
      content["rank"] = len(contentsList) - 1
      content["selected"] = True
    # ※要確認
    elif content["rank"] >= data["rank"]:
      content["rank"] = int(content["rank"]) - 1

def release_select(contentsList):
  for content in contentsList:
    content["selected"] = False

def convert_position_widget_to_graph(position, widget_size):
  left_blank = plt.rcParams.get("figure.subplot.left")
  right_blank = plt.rcParams.get("figure.subplot.right")
  bottom_blank = plt.rcParams.get("figure.subplot.bottom")
  top_blank = plt.rcParams.get("figure.subplot.top")

  graph_range_left = widget_size[0] * left_blank
  graph_range_right = widget_size[0] * right_blank
  graph_range_bottom = widget_size[1] * (1 - bottom_blank)
  graph_range_top = widget_size[1] * (1 - top_blank)

  #グラフ内相対座標
  relative_x = (position[0] - graph_range_left) / (graph_range_right - graph_range_left)
  relative_y = (graph_range_bottom - position[1]) / (graph_range_bottom - graph_range_top)

  return (relative_x, relative_y)
  #グラフ内絶対座標

def convert_abs_to_rel(ax, position):
  range_x = ax.get_xlim()
  range_y = ax.get_ylim()
  rel_x = position[0] - float(range_x[0]) / (range_x[1] - range_x[0])
  rel_y = position[1] - float(range_y[0]) / (range_y[1] - range_y[0])
  return (rel_x, rel_y)

def convert_rel_to_abs(ax, position):
  range_x = ax.get_xlim()
  range_y = ax.get_ylim()
  absolute_x = (range_x[1] - range_x[0]) * position[0] + float(range_x[0])
  absolute_y = (range_y[1] - range_y[0]) * position[1] + float(range_y[0])
  return (absolute_x, absolute_y)
