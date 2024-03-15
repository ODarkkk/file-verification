import os
import crc32c
import pandas
from PIL import Image
from openpyxl import Workbook

class Repair:
    def __init__(self, input_dir, output_dir):
        """Initialize Repair class with input and output directories."""
        self.input_dir = input_dir
        self.output_dir = output_dir

    def repair_image(self, input_file, output_file):
        """Attempt to repair image file."""
        try:
            img = Image.open(input_file)
            img.save(output_file)
            print(f"Repaired image: {input_file} -> {output_file}")
            return True
        except Exception as e:
            print(f"Error repairing image: {e}")
            return False

    def repair_excel(self, input_file, output_file):
        """Attempt to repair Excel file."""
        try:
            wb = Workbook()
            df = pandas.read_excel(input_file, engine='openpyxl')
            wb.active = df.to_worksheet()
            wb.save(output_file)
            print(f"Repaired Excel: {input_file} -> {output_file}")
            return True
        except Exception as e:
            print(f"Error repairing Excel: {e}")
            return False

    def repair_file(self, input_file, output_file):
        """Attempt to repair file based on file extension."""
        file_ext = os.path.splitext(input_file)[1]
        if file_ext.lower() in ['.jpg', '.jpeg']:
            return self.repair_image(input_file, output_file)
        elif file_ext.lower() == '.xlsx':
            return self.repair_excel(input_file, output_file)
        else:
            print(f"Unsupported file format: {file_ext}")
            return False

    def calculate_crc32(self, file_path):
        """Calculate CRC32 checksum of a file."""
        with open(file_path, 'rb') as f:
            data = f.read()
            crc = crc32c.crc32c(data)
        return crc

    def repair_files(self):
        """Repair files in the input directory."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for filename in os.listdir(self.input_dir):
            input_file = os.path.join(self.input_dir, filename)
            output_file = os.path.join(self.output_dir, filename)
            self.repair_file(input_file, output_file)
            self.calculate_crc32(output_file)
