from app.rag import read_pdf , create_chunk

text = read_pdf("documents/python.pdf")

print(len(text))

chunks=create_chunk("documents/python.pdf")

print("Number of chunks:",len(chunks))

print("------------------------------")

print(chunks[0])

if len(chunks)>1:
    print(chunks[1])