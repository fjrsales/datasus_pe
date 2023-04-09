import os.path
import pandas as pd

class Extractor:
  """ A class to extract data from .csv, .json and excel format files."""

  def __init__(self, path: str) -> None:
    self.path = path
    #self.columns_of_interest = columns_of_interest

  def __get_extension(self) -> str:
    """ Get the file's extension and assure it is in the lowercase format."""

    self.__extension = os.path.splitext(self.path)[1].lower() 
    return self.__extension
  
  def extract_df_from_csv(self):
    """ Extract the data from a .csv file. Returns a DataFrame."""
    
    self.__extension = self.__get_extension()
    if self.__extension == ".csv":
      try:
        self.df = pd.read_csv(self.path, low_memory=False)
      except:
        print("Error extracting DataFrame.")
        self.df = pd.DataFrame(data={})
    else:
      print("This function only takes .csv extension files.")
    return self.df

  def extract_df_from_excel(self):
    """ Extract the data from a excel extension file. Returns a DataFrame."""
    
    self.__extension = self.__get_extension()
    if self.__extension == ".xls" or ".xlsx" or ".xlsm" or ".xlsb" or ".odf" or ".ods" or ".odt":
      try:
        self.df = pd.read_excel(self.path)
      except:
        print("Error extracting DataFrame.")
    else:
        print("This function only takes excel extensions files.")
    return self.df

  def verify_data(self, state: str, year_min: int, year_max: int): 
    """ Check if the data is from a specific state of Brazil and if it corresponds to a range of years."""

    for i in self.df["ESTADO"]:
      if i != state.upper():
        j = self.df["ESTADO"].index(i)
        self.df.drop(j)
        print("Line ",j," was erased because the state was inaccurate (",i,")")

    for i in self.df["ANO_O"]:
      if i < year_min or i > year_max :
        j = self.df["ANO_O"].index(i)
        self.df.drop(j)
        print("Line ",j," was erased because the year was inaccurate (",i,")")
        
    print("Verification done.")
    return self.df
  
  def select_columns_of_interest(self, columns: list):
    """ Return the DataFrame containing only the columns of interest."""
    return self.df[columns]