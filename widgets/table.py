import tkinter as tk

#セルのフレーム(雛形)を作成
class Cell_frame(tk.Frame):
  instances = []

  def __init__(self, row=0, column=0, bgcolor="white", master=None, text=None):
    super().__init__(master, cnf={
      "relief" : tk.GROOVE,
      "bd" : 1,
      "bg" : bgcolor,
    })
    self.text = text
    self.bg = bgcolor
    self.str = tk.StringVar(value=self.text)
    self.selected = False
    self.grid(row=row, column=column)

    self.label = tk.Label(master=self, bg=self.bg, bd=1, textvariable=self.str, width=8, height=1)
    self.label.pack(padx=2, pady=2, expand=True, fill=tk.BOTH)
    Cell_frame.instances.append(self)

  @classmethod
  def reset_select(cls, self):
    for instance in cls.instances:
      instance.selected = False
      instance.config(bg=instance.bg)
      try:
        instance.entry.destroy()
        instance.label.pack(padx=2, pady=2)
      except:
        pass

#列のラベル(一番左のやつ)
class Row(Cell_frame):
  def __init__(self, row, bgcolor, master, text):
    super().__init__(row, bgcolor=bgcolor, master=master, text=text)
    self.config(bg=self.bg)
    self.label.config(bg=self.bg, width=2)

#カラム(一番上のやつ)
class Column(Cell_frame):
  def __init__(self, column, bgcolor, master, text):
    super().__init__(column=column, bgcolor=bgcolor, master=master, text=text)
    self.config(bg=self.bg)
    self.label.config(bg=self.bg)

#セル
class Cell(Cell_frame):
  def __init__(self, row, column, master, text):
    super().__init__(row=row, column=column, master=master, text=text)
    self.label.bind("<ButtonPress-1>", self.select_cell)
    self.label.bind("<Double-1>", self.edit_cell)
    self.label.bind("<Enter>", self.enter_cell)
    self.label.bind("<Leave>", self.leave_cell)

  def enter_cell(self, event):
    if not self.selected:
      self.config(bg="lightblue")

  def leave_cell(self, event):
    if not self.selected:
      self.config(bg="white")

  def select_cell(self, event):
    Cell_frame.reset_select(self)
    self.selected = True
    self.config(bg="blue")

  def edit_cell(self, event):
    self.label.pack_forget()
    self.entry = tk.Entry(self, textvariable=self.str, width=8)
    self.entry.bind("<Return>", self.complete_edit)
    self.entry.focus_set()
    self.entry.place(x=-2,y=-2)

  def complete_edit(self, event):
    self.entry.destroy()
    self.label.pack(padx=2, pady=2)
    self.selected = False
    self.config(bg="white")

class Table_widget(tk.Frame):
  def __init__(self, master=None, row=0, column=0):
    super().__init__(master)
    self.cell_canvas_frame = tk.Frame(self)
    self.cell_canvas = tk.Canvas(self.cell_canvas_frame, width=600, height=260)
    self.scroll_frame = tk.Frame(self.cell_canvas)
    self.scroll_canvas_v = tk.Canvas(self, width=10, height=260)
    self.scroll_canvas_h = tk.Canvas(self, width=600)
    self.scroll_canvas_v_frame = tk.Frame(self.scroll_canvas_v)
    self.scroll_canvas_h_frame = tk.Frame(self.scroll_canvas_h)

    for column in range(10):
      Column(column=column, bgcolor="lightgray", master=self.scroll_canvas_h_frame, text=None)
    self.scroll_canvas_h_frame.pack(padx=0, pady=0)
    for row in range(50):
      Row(row=row, bgcolor="lightgray", master=self.scroll_canvas_v_frame, text=row+1)
    self.scroll_canvas_v_frame.pack(padx=0, pady=0)
    for row in range(50):
      for column in range(10):
        Cell(row=row, column=column, master=self.scroll_frame, text=None)
    self.scroll_frame.pack(padx=0, pady=0)

    self.cell_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw", width=840, height=1325)
    self.scroll_canvas_h.create_window((0, 0), window=self.scroll_canvas_h_frame, anchor="nw", width=840)
    self.scroll_canvas_v.create_window((0, 0), window=self.scroll_canvas_v_frame, anchor="nw", height=1325)

    self.scrollbar_y = tk.Scrollbar(self.cell_canvas_frame, orient="vertical", command=self.sync_scroll_y)
    # self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y, expand=True)
    self.scrollbar_y.place(relx=0.975, rely=0, relheight=1, relwidth=0.025)
    self.scrollbar_x = tk.Scrollbar(self.cell_canvas_frame, orient="horizontal", command=self.sync_scroll_x)
    self.scrollbar_x.place(relx=0, rely=0.95, relheight=0.05, relwidth=1)
    # self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X, expand=True)

    self.cell_canvas.configure(scrollregion=self.cell_canvas.bbox("all"))
    self.cell_canvas.configure(yscrollcommand=self.scrollbar_y.set)
    self.cell_canvas.configure(xscrollcommand=self.scrollbar_x.set)
    self.scroll_canvas_v.configure(scrollregion=self.scroll_canvas_v.bbox("all"))
    self.scroll_canvas_v.configure(yscrollcommand=self.scrollbar_y.set)
    self.scroll_canvas_h.configure(scrollregion=self.scroll_canvas_h.bbox("all"))
    self.scroll_canvas_h.configure(xscrollcommand=self.scrollbar_x.set)

    self.scroll_canvas_v.grid(column=0, row=1)
    self.scroll_canvas_h.grid(column=1, row=0)
    self.cell_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    self.cell_canvas_frame.grid(column=1, columnspan=2, row=1, rowspan=2, padx=0, pady=0)
    # self.pack()
    self.grid(row=row, column=column)
    self.update_idletasks()
    self.scroll_canvas_h.config(height=self.scroll_canvas_h_frame.winfo_reqheight())
    self.scroll_canvas_v.config(width=self.scroll_canvas_v_frame.winfo_reqwidth())
    self.update_idletasks()

  def sync_scroll_y(self, *arg):
    self.cell_canvas.yview(*arg)
    self.scroll_canvas_v.yview(*arg)

  def sync_scroll_x(self, *arg):
    self.cell_canvas.xview(*arg)
    self.scroll_canvas_h.xview(*arg)


if __name__ == "__main__":
  root = tk.Tk()
  root.geometry('990x500')
  app = Table_widget(master=root)
  app.mainloop()