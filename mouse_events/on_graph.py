import graph_contents

def mark_content(x, y, ax, contentsList):
  selected_contents = []
  for content in contentsList:
    bbox = content["value"].get_window_extent().transformed(ax.transData.inverted())
    if (bbox.x0 <= x) and (bbox.y0 <= y) and (bbox.x1 >= x) and (bbox.y1 >= y):
      selected_contents.append(content)
  
  if len(selected_contents) == 0:
    print("None is selected")
    graph_contents.release_select(contentsList)
  elif len(selected_contents) == 1:
    print(f"Selected item is {selected_contents[0]}")
    graph_contents.select_content(selected_contents[0], contentsList)
  else:
    print(f"Selected items are {selected_contents}")
    max_rank = max([i["rank"] for i in selected_contents])
    selected_content = [i for i in selected_contents if i["rank"] == max_rank]
    print(f"Finally selected {selected_content}")
    graph_contents.select_content(selected_content[0], contentsList)

  return contentsList

def getlocation(event, ax, widget_width, widget_height):
  x = event.x
  y = event.y
  # fig_size = plt.rcParams.get("figure.figsize")
  rel = graph_contents.convert_position_widget_to_graph((x, y), (widget_width, widget_height))
  abs = graph_contents.convert_rel_to_abs(ax, rel)
  return abs, rel

def dragg_event(ax, abs, start_abs, rel, start_rel, contentsList):
  moveList = [content for content in contentsList if content["selected"] == True]
  if len(moveList) == 0:
    ax.set_xlim(ax.get_xlim()[0] - abs[0] + start_abs[0], ax.get_xlim()[1] - abs[0] + start_abs[0])
    ax.set_ylim(ax.get_ylim()[0] - abs[1] + start_abs[1], ax.get_ylim()[1] - abs[1] + start_abs[1])
  else:
    for content in moveList:
      content["value"].set_position((content["value"].get_position()[0] + rel[0] - start_rel[0], content["value"].get_position()[1] + rel[1] - start_rel[1]))

