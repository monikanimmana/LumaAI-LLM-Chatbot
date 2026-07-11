from app.rag import read_pdf

text = read_pdf("documents/python.pdf")

print(len(text))