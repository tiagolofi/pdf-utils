from pypdf import PdfReader, PdfWriter
from typing import List
from os import makedirs, path

class PDF():
    def __init__(self, path: str) -> None:
        self.path = path
        self.reader = PdfReader(self.path)
        self.writers = {}
        self.writer = None

    def split(self, writer_name: str, start: int = 0, end: int = None) -> None:
        if end is None:
            end = len(self.reader.pages)

        for _, page in enumerate(self.reader.pages[start:end]):
            self.writers[writer_name] = PdfWriter()
            self.writers[writer_name].add_page(page)

    def join(self, writers: List[str]) -> None:
        if self.writer is None:
            self.writer = PdfWriter()

        for writer_name in writers:
            for page in self.writers[writer_name].pages:
                self.writer.add_page(page)

    def save(self, filename: str, output_folder: str = ".")  -> None:
        if self.writer is None:
            self.writer = PdfWriter()
            for writer in self.writers.values():
                for page in writer.pages:
                    self.writer.add_page(page)

        if not path.exists(output_folder):
            makedirs(output_folder)

        output_filename = f"{output_folder}/{filename}.pdf"
        with open(output_filename, "wb") as out:
            self.writer.write(out)
        print(f"Created: {output_filename}")
