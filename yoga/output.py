import csv
import numpy as np

def write_to_csv(file_name_csv, data_points, header=False):
  row = []
  row.append(data_points)
  myFile = open(file_name_csv, 'a')
  with myFile:
        writer = csv.writer(myFile)
        if header:
            writer.writerows(header)
        writer.writerows(row)
  return

