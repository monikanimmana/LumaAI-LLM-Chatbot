from pypdf import PdfReader # type:ignore
from langchain_text_splitters import RecursiveCharacterTextSplitter #type:ignore

def read_pdf(file_path:str)->str:
    reader=PdfReader(file_path)

    text=""

    for page in reader.pages:
        page_text=page.extract_text()

        print(page_text)

        if page_text:
            text+=page_text + "\n"

    return text

def create_chunk(text:str):

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_text(text)

