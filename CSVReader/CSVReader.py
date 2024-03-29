import csv
from Fileutilities.absolutepath import absolute_path


class CsvReader:

    def __len__(self):
        return len(self.data)

    def __init__(self, filepath):
        self.data = []
        with open(absolute_path(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)

        pass
