from pypdf import PdfReader, PdfWriter

def split_pdf(input_path):
    reader = PdfReader(input_path)
    
    # Loop through all pages and save them individually
    for index, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        
        output_filename = f"page_{index + 1}.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)
        print(f"Created: {output_filename}")

split_pdf("exemplo.pdf")