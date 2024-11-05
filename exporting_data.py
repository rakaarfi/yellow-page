import pandas as pd

class DataExporter:
    """Handles exporting collected data to various formats."""
    
    def __init__(self, data):
        self.data = data

    def to_excel(self, file_name='dentists_data.xlsx'):
        """Exports the collected data to an Excel file."""
        df = pd.DataFrame(self.data)
        df.to_excel(file_name, index=False)