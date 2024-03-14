

import sys, os, struct, shutil, filecmp, crc32c, pandas
from PIL import Image
from openpyxl import Workbook

class Repair:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def repair_image(self, input_file, output_file):
        try:
            img = Image.open(input_file)
            img.save(output_file)
            print(f"Repaired image: {input_file} -> {output_file}")
            return True
        except Exception as e:
            print(f"Error repairing image: {e}")
            return False

    def repair_excel(self, input_file, output_file):
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

    def calculate_crc32(self, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
            crc = crc32c.crc32c(data)
        return crc

    def repair_files(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for filename in os.listdir(self.input_dir):
            input_file = os.path.join(self.input_dir, filename)
            output_file = os.path.join(self.output_dir, filename)
            file_ext = os.path.splitext(filename)[1]

            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                self.repair_image(input_file, output_file)
                self.calculate_crc32(output_file)

            elif filename.endswith(".xlsx"):
                self.repair_excel(input_file, output_file)
                self.calculate_crc32(output_file)

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    repair_tool = Repair(input_dir, output_dir)
    repair_tool.repair_files()
