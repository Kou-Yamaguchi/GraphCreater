import tkinter as tk

class OptionItem(tk.Frame):
  def __init__(self, master=None, item_name=None):
    super().__init__(master)
    self.label = tk.Label(master=self, text=item_name, background="lightgray")
    self.label.pack(side=tk.LEFT)

class EntryForm(OptionItem):
  def __init__(self, master=None, item_name=None, content=None, fig_canvas=None) -> None:
    super().__init__(master, item_name)
    self.content = content
    self.fig_canvas = fig_canvas
    # validate_command = self.master.register(self.renew_text)
    self.var = tk.StringVar(value=str(content.get_text()))
    self.input = tk.Entry(self,
                          textvariable=self.var,
                          # validate='all',
                          # validatecommand=(
                          #   validate_command,
                          #   '%P'
                          #   )
                          )

    self.input.bind("<Return>", self.press_enter)

    self.input.pack(side=tk.RIGHT)
    self.pack()

  def press_enter(self, event):
    self.content.set_text(self.var.get())
    self.fig_canvas.draw()
  
  # def renew_text(self, text):
  #   # self.content.set_text(self.var.get())
  #   self.content.set_text(text)
  #   self.fig_canvas.draw()


class SpinboxForm(OptionItem):
  def __init__(self, master=None, item_name=None, content=None, fig_canvas=None, min=1, max=30) -> None:
    super().__init__(master, item_name)
    self.content = content
    self.fig_canvas = fig_canvas
    self.var = tk.DoubleVar(value=float(content.get_fontsize()))
    self.input = tk.Spinbox(
      self,
      textvariable=self.var,
      from_=min,
      to=max,
      increment=1,
    )

    self.input.bind("<Return>", self.press_enter)

    self.input.pack(side=tk.RIGHT)
    self.pack()

  def press_enter(self, event):
    self.content.set_fontsize(self.var.get())
    self.fig_canvas.draw()

class CheckbuttonFrame(tk.Frame):
  def __init__(self, master=None, name_list=None, content=None, fig_canvas=None, pack_side=tk.LEFT):
    super().__init__(master)
    self.content = content
    self.fig_canvas = fig_canvas
    self.vars = []
    for _ in name_list:
      var = tk.BooleanVar()
      self.vars.append(var)
    for _, (name, var) in enumerate(zip(name_list, self.vars)):
      self.check = tk.Checkbutton(
        master = self,
        text = name,
        variable = var,
        command=self.change_state
      )
      self.check.pack(side=pack_side)

    # self.bind("<Return>", self.change_state)

    self.pack()

  def read(self, index):
    return self.vars[index].get()
  
  def change_state(self):
    if self.vars[0].get():
      self.content.set_fontweight("heavy")
    else:
      self.content.set_fontweight("normal")
    if self.vars[1].get():
      self.content.set_fontstyle("oblique")
    else:
      self.content.set_fontstyle("normal")
    self.fig_canvas.draw()

class RadiobuttonFrame(tk.Frame):
  def __init__(self, master=None, items=None, pack_side=tk.LEFT):
    super().__init__(master)
    # self.master = master
    self.var = tk.IntVar(self)
    for item in items:
      r = tk.Radiobutton(
        master=self,
        text=item["text"],
        value=item["value"],
        var=self.var
      )
      r.pack(side=pack_side)
    self.pack()

  def read(self):
    return self.var.get()

class OptionWidget(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)

  def display(self, contents_list, fig_canvas):
    selected_list = [content for content in contents_list if content["selected"] == True]
    try:
      self.widgets_frame.destroy()
    except:
      pass
    if len(selected_list) == 1:
      self.widgets_frame = tk.Frame(self)
      selected_type = selected_list[0]["type"]
      if selected_type == "text":

        selected_content = selected_list[0]["value"]

        self.entry = EntryForm(self.widgets_frame, "text", selected_content, fig_canvas)
        self.font = SpinboxForm(self.widgets_frame, "サイズ", selected_content, fig_canvas)
        CheckbuttonFrame(self.widgets_frame, ["太字", "斜体"], selected_content, fig_canvas)
        radiobutton_items=[{"text" : "なし", "value" : 0}, {"text" : "1つ", "value" : 1}, {"text" : "2つ", "value" : 2}]
        RadiobuttonFrame(self.widgets_frame, radiobutton_items)
      self.widgets_frame.pack()
    self.pack(side=tk.RIGHT)
