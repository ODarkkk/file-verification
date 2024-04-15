import os
import shutil
import crc32c
import pandas as pd
import pyzipper
import PyPDF2
from PIL import Image
from openpyxl import Workbook
import zipfile
from docx import Document
from docx.shared import Inches
from moviepy.editor import VideoFileClip


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

    def repair_zip(input_file, output_file):
        """Repair a ZIP file using pyzipper."""
        try:
            with pyzipper.AESZipFile(input_file, mode='r') as zin:
                with pyzipper.AESZipFile(output_file, mode='w') as zout:
                    zout.comment = zin.comment
                    for item in zin.infolist():
                        if not item.is_dir():
                            zout.writestr(item, zin.read(item))
            print(f"Repaired ZIP file: {input_file} -> {output_file}")
            return True
        except Exception as e:
            print(f"Error repairing ZIP file: {e}")
            return False
    def repair_pdf(self, input_file, output_file):
        """Attempt to repair a PDF file."""
        try:
            with open(input_file, "rb") as f:
                pdf = PyPDF2.PdfFileReader(f)
                if pdf.isEncrypted:
                    print("Error: PDF is encrypted.")
                    return False
                if pdf.getNumPages() == 0:
                    print("Error: PDF has no pages.")
                    return False
                with open(output_file, "wb") as f:
                    pdf.write(f)
                return True
        except Exception as e:
            print(f"Error repairing PDF: {e}")
            return False

    def repair_excel(self, input_file, output_file):
        """Attempt to repair Excel file."""
        try:
            wb = Workbook()
            df = pd.read_excel(input_file, engine='openpyxl')
            wb.active = df.to_worksheet()
            wb.save(output_file)
            print(f"Repaired Excel: {input_file} -> {output_file}")
            return True
        except Exception as e:
            print(f"Error repairing Excel: {e}")
            return False

    def repair_word(self, input_file, output_file):
        """Attempt to repair Word file."""
        try:
            shutil.copyfile(input_file, output_file)
            print(f"Repaired Word: {input_file} -> {output_file}")
            return True
        except Exception as e:
            print(f"Error repairing Word: {e}")
            return False

    def repair_video(self, input_file, output_file):
        """Attempt to repair Video file."""
        try:
            clip = VideoFileClip(input_file)
            clip.write_videofile(output_file)
            print(f"Repaired Video: {input_file} -> {output_file}")
            return True
        except Exception as e:
            print(f"Error repairing Video: {e}")
            return False

    def repair_file(self, input_file, output_file):
        """Repair all supported files in the input directory."""
        if not os.path.exists(output_file):
            os.makedirs(output_file)
        file_ext = os.path.splitext(input_file)[1].lower()
        if file_ext in ['.jpg', '.jpeg', '.png', '.gif']:
            return self.repair_image(input_file, output_file)
        elif file_ext == '.pdf':
            return self.repair_pdf(input_file, output_file)
        elif file_ext == '.xlsx':
            return self.repair_excel(input_file, output_file)
        elif file_ext == '.docx':
            return self.repair_word(input_file, output_file)
        elif file_ext == '.zip':
            return self.repair_zip(input_file, output_file)
        elif file_ext in ['.mp4', '.avi', '.mov']:
            return self.repair_video(input_file, output_file)
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