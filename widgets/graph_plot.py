import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib import patches

import mouse_events
import default_set
import templates
import graph_contents

class MatplotlibFigure():
  def __init__(self):
    default_set.set()
    self.fig = plt.figure(facecolor='lightgray')
    self.ax = self.fig.add_subplot(1,1,1)
    self.contentsList = []

  def read_template(self):
    templates.XRD_graph(self)

  def add_text(self, loc_x=0.5, loc_y=0.5, text="text"):
    new_text = self.ax.text(loc_x, loc_y, text, ha="center", va="center", transform=self.ax.transAxes)
    self.contentsList.append({"rank" : int(len(self.contentsList)), "value" : new_text, "selected" : False, "type" : "text"})
    # self.add_first_frame()
    # self.add_text_frame(0.15)

  def edit_text(self, text):
    edit_list = [content for content in self.contentsList if content["selected"] == True]
    edit_list[0]["value"].set_text(text)

  def add_first_frame(self):
    add_list = [content for content in self.contentsList if content["selected"] == False]
    box_dic = {
    "boxstyle" : "square",
    "linestyle" : "-",
    "facecolor" : "white",
    "linewidth" : 1,
    "pad" : 0,
    "padtop" : 0.5
    }
    add_list[0]["value"].set_bbox(box_dic)

  def add_text_frame(self, gap):
    add_list = [content for content in self.contentsList if content["selected"] == False]
    bbox = add_list[0]["value"].get_window_extent().transformed(self.ax.transData.inverted())
    print(bbox)
    range_x = self.ax.get_xlim()[1]-self.ax.get_xlim()[0]
    range_y = self.ax.get_ylim()[1]-self.ax.get_ylim()[0]
    width = bbox.width
    height = bbox.height

    print(f"{width}, {height}")
    figsize = self.fig.get_size_inches()
    l_x = gap * (range_x) / figsize[0]
    l_y = gap * (range_y) / figsize[1]
    # fr = patches.Rectangle(xy=(bbox.x0 - l_x, bbox.y0 - l_y),
    #                        width = bbox.x1 - bbox.x0 + (2 * l_x),
    #                        height = bbox.y1 - bbox.y0 + (2 * l_y),
    #                        edgecolor="black",
    #                        facecolor=None,
    #                        fill=None,
    #                        linestyle="-",
    #                        )
    position = add_list[0]["value"].get_position()
    print(f"{position[0]-width/2}, {position[1]-height/2}")
    fr_2 = patches.Rectangle((position[0]-width/2, position[1]-height/2),
                             width=width,
                             height=height,
                             transform=self.ax.transAxes,
                             edgecolor="Black",
                             facecolor=None,
                             fill=None,
                             linestyle="-"
                             )
    self.ax.add_patch(fr_2)

  def add_plot(self, x, y):
    new_plot = self.ax.plot(x, y)
    self.contentsList.append({"rank" : int(len(self.contentsList)), "value" : new_plot, "selected" : False, "type" : "plot"})

  def add_vline(self, x):
    new_vline = self.ax.vlines(x)
    self.contentsList.append({"rank" : int(len(self.contentsList)), "value" : new_vline, "selected" : False, "type" : "line"})

  def add_hline(self, y):
    new_hline = self.ax.hlines(y)
    self.contentsList.append({"rank" : int(len(self.contentsList)), "value" : new_hline, "selected" : False, "type" : "line"})

  def select_content(self, abs_x, abs_y):
    self.contentsList = mouse_events.mark_content(abs_x, abs_y, self.ax, self.contentsList)
    # select_list = [content for content in self.contentsList if content["selected"] == True]
    # return select_list[0]["value"]
    # option_widget.display(self.contentsList)

  def move_content(self, abs, start_abs, rel, start_rel):
    mouse_events.dragg_event(self.ax, abs, start_abs, rel, start_rel, self.contentsList)

  def del_content(self):
    self.contentsList, _ = graph_contents.remove_content(self.contentsList)

class Plot_Widget(tk.Frame):
  def __init__(self, option_widget, master=None) -> None:
    super().__init__(master, relief=tk.SOLID, pady=5, bd=5)
    self.option_widget = option_widget
    self.graph = MatplotlibFigure()
    self.graph.read_template()
    self.fig_canvas = FigureCanvasTkAgg(self.graph.fig, self)
    self.graph_widget = self.fig_canvas.get_tk_widget()
    self.toolbar = NavigationToolbar2Tk(self.fig_canvas, self)

    # self.graph_widget
    self.graph_widget.bind("<ButtonPress-1>", self.left_click)
    self.graph_widget.bind("<Double-1>", self.double_click)
    self.graph_widget.bind("<B1-Motion>", self.left_dragg)
    # self.graph_widget.bind("<Return>", self.read_option)
    self.graph_widget.pack(side=tk.BOTTOM, fill=None, expand=False)

    #widget:quick optionを作成#########################

    self.pack(side=tk.LEFT)
    # self.place(x=0, y=0, width=640, height=480)

  def get_size(self):
    width = self.graph_widget.winfo_width()
    height = self.graph_widget.winfo_height()
    return width, height

  def left_click(self, event):
    # global start_rel_x, start_rel_y
    width, height = self.get_size()
    # self.start_abs_x, self.start_abs_y, self.start_rel_x, self.start_rel_y = mouse_events.getlocation(event, self.graph.ax, width, height)
    self.start_abs, self.start_rel = mouse_events.getlocation(event, self.graph.ax, width, height)
    self.graph.select_content(self.start_abs[0], self.start_abs[1])

    # self.option_widget

    print(self.graph.contentsList)

  def left_dragg(self, event):
    # global start_rel_x, start_rel_y
    width, height = self.get_size()
    # self.abs_x, self.abs_y, self.rel_x, self.rel_y = mouse_events.getlocation(event, self.graph.ax, width, height)
    self.abs, self.rel = mouse_events.getlocation(event, self.graph.ax, width, height)
    self.graph.move_content(self.abs, self.start_abs, self.rel, self.start_rel)
    self.start_abs, self.start_rel = mouse_events.getlocation(event, self.graph.ax, width, height)
    self.fig_canvas.draw()

  # def double_click(self, event):
  #   self.left_click(event)
  #   self.option_widget.display(self.graph.contentsList)

  def double_click(self, event):
    self.left_click(event)
    self.option_widget.display(self.graph.contentsList, self.fig_canvas)


  # def read_option(self, event):
  #   text = self.option_widget.entry.read()
  #   print(text)
  #   selected_list = [content for content in self.graph.contentsList if content["selected"] == True]
  #   selected_list[0]["value"].set_text(text)
  #   self.fig_canvas.draw()

if __name__ == "__main__":
  root = tk.Tk()
  root.geometry('990x500')
  app = Plot_Widget(master=root)
  app.mainloop()