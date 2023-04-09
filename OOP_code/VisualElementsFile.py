import tkinter as tk  
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd

class Visual_Elements:

  def __init__(self,data: dict):
    self.data = data

  def plot_bar_graph(self,title = "", y = "", x = "", len = 16, h = 8) -> None:
    plt.figure(figsize=(16,8))
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.bar(self.data.keys(), self.data.values())
    plt.show()

  def plot_pie_graph(self,title = "") -> None:
    plt.title(title)
    plt.pie(self.data.values(), labels = self.data.keys())
    plt.show() 

  def display_top10_dataframe(self,column1="Ranking",column2="") -> None:
    position = ['1º','2º','3º','4º','5º','6º','7º','8º','9º','10º']
    df_top10 = pd.DataFrame(zip(position,list(self.data.keys())), columns = [column1,column2])
    print(df_top10)