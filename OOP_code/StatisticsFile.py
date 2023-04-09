import pandas as pd

class Statistics:

  def __init__(self,df : pd.DataFrame):
    self.df = df

  def count_elements(self,column: str) -> dict:
    d = dict(self.df[column].value_counts())
    return d

  def calculate_percentage(self,x:int,length:int) -> float:
    return round(100*x/length,2)

  def calculate_non_null_content(self) -> None:
    len_col = self.df.shape[0]
    for col in list(self.df.keys()):
      total_nonNull=round(self.calculate_percentage(self.df[col].count(), len_col),2)
      print('Column {} has {} % of non null values'.format(col,total_nonNull))