import numpy as np

def add_sin(graph_widget):
  x = np.arange(-np.pi+50, np.pi+50, 0.1)
  y = np.sin(x)
  graph_widget.graph.ax.plot(x,y)
  graph_widget.fig_canvas.draw()