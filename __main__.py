import tkinter as tk
# from ipywidgets import interact
import numpy as np

from widgets import Plot_Widget, OptionWidget, Table_widget
from test_functions import add_sin

# matplotlib.use("svg")

class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.master.title('graph')
    self.config(relief="groove",bd=2)
    frame_graph = tk.Frame(self, width=640, height=480, relief=tk.RIDGE, bd=5)
    # frame_graph.propagate(False)

    self.option_widget = OptionWidget(frame_graph)
    self.graph_widget = Plot_Widget(self.option_widget, frame_graph)

    # frame_graph.pack(anchor=tk.NW)
    frame_graph.grid(row=0, column=0)
    Table_widget(self, widget_row=1)
    self.pack()

    self.master.update_idletasks()

    # button_add_sin = tk.Button(self.master, text = "Add Sin Graph", command = lambda: add_sin(self.graph_widget))
    # button_add_sin.pack(side = tk.LEFT)
    # button_check_size = tk.Button(self.master, text = "Check_size", command = self.check_size)
    # button_check_size.pack(side = tk.LEFT)
    # button_add_Dtext = tk.Button(self.master, text = "Add text", command = lambda: [self.graph_widget.graph.add_text(), self.graph_widget.fig_canvas.draw()])
    # button_add_Dtext.pack(side = tk.LEFT)
    # button_delete_content = tk.Button(self.master, text = "Remove", command = lambda: [self.graph_widget.graph.del_content(), self.graph_widget.fig_canvas.draw()])
    # button_delete_content.pack(side = tk.LEFT)

  #   button_read_option = tk.Button(self.master, text = "Read option", command = self.read_option)
  #   button_read_option.pack(side = tk.RIGHT)

  # def read_option(self):
  #   text = self.option_widget.entry.read()
  #   print(text)
  #   selected_list = [content for content in self.graph_widget.graph.contentsList if content["selected"] == True]
  #   selected_list[0]["value"].set_text(text)
  #   self.graph_widget.fig_canvas.draw()

  def check_size(self):
    print(self.master.winfo_geometry())

root = tk.Tk()
root.geometry('1200x800')
app = Application(master=root)
app.mainloop()
