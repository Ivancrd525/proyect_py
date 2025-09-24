try:
  from tkinter import Tk
except ImportError as e:
  print('Error al importar el modulo: ', e)

class Root:
  def __init__(self) -> None:
    self.root =Tk()

  def run(self):
    self.root.mainloop()

if __name__ == '__main__':
  root = Root()
  root.run()