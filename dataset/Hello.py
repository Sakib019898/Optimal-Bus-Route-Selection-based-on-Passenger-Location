import pandas as pd

excel_file = 'EXTENDED_1.xlsx'
dataFrame = pd.read_excel(excel_file)

dataFrame.head()
dataFrame.loc[:,['ID','Pickup location of yours for bus','Pickup time of yours for bus']]
