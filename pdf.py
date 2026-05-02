from pypdf import PdfReader, PdfWriter
from os import makedirs, path

class PDF():
    def __init__(self, path: str) -> None:
        self.path = path
        self.reader = PdfReader(self.path)

    def split(self, output_folder: str = ".", start: int = 0, end: int = None) -> None:
        if end is None:
            end = len(self.reader.pages)

        if not path.exists(output_folder):
            makedirs(output_folder)

        for index, page in enumerate(self.reader.pages[start:end]):
            writer = PdfWriter()
            writer.add_page(page)
            
            output_filename = f"{output_folder}/page_{index + 1}.pdf"
            with open(output_filename, "wb") as out:
                writer.write(out)
            print(f"Created: {output_filename}")

# Criando uma instância da classe PDF com o arquivo "gato-xadrez.pdf"
pdf = PDF("gato-xadrez.pdf")

# Separando apenas a primeira página do PDF
pdf.split(output_folder="gato-xadrez-pages", start=0, end=1)