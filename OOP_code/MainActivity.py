
path = 'C:/Users/sofia/OneDrive/Área de Trabalho/Tecnicas_OOP_Project/code/files/PE_2010_2019.csv'
""" Define the path to your interest file."""

import ExtractorFile as ef
""" Import ExtractorFile class and create object."""
extract = ef.Extractor(path)
df = extract.extract_df_from_csv()
# print(df)
df = extract.verify_data("PE",2010,2019)
df = extract.select_columns_of_interest(['LINHAA', 'LINHAB', 'LINHAC', 'LINHAD', 'LINHAII', 'CAUSABAS', 'CAUSABAS_O', 'ANO_O', 'ESTADO', 'CODMUNRES','CODMUNOCOR'])

import StatisticsFile as sf
""" Import StatisticsFile class and create object."""
stats = sf.Statistics(df)
stats.calculate_non_null_content()
dict_cause_of_death = stats.count_elements("CAUSABAS")
dict_10_causes = {}
for x,y in zip(list(dict_cause_of_death.keys())[:10],list(dict_cause_of_death.values())[:10]):
    dict_10_causes[x]=y

import VisualElementsFile as vef
""" Import VisualElementsFile class and create object."""
ve = vef.Visual_Elements(dict_10_causes)
ve.plot_bar_graph()
ve.plot_pie_graph()
ve.display_top10_dataframe()



