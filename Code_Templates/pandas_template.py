import pandas as pd
import numpy as np


output_columns = ["name","information","reference"]
outdata = np.array([names,information,reference]).T

dfout = pd.DataFrame(outdata, columns = output_columns)
dfout.to_excel("wikipedia_resume.xlsx", index=False) 