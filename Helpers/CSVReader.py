from Models.CSVmodel import CSV_model
import csv

class CSVReader:
    def ReadFromFile(self, filePath: str, model: CSV_model) -> CSV_model:
        with open(filePath) as f:
            rows = csv.reader(f)
            if csv.Sniffer().has_header:
                header = next(rows)
                model.header = header[0].split(';')
            for i in rows:
                model.data.append(i[0].split(';'))
        return model