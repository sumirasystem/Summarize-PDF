import re
from PyPDF2 import PdfReader
from langchain.chains import AnalyzeDocumentChain
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI

# This function is reading PDF from the start page to final page
def get_pdf_text(document_path, start_page=1, final_page=999):
    reader = PdfReader(document_path)
    number_of_pages = len(reader.pages)
    print(f'numer of pages: {number_of_pages}')
    pages = ''
    for page_num in range(start_page - 1, min(number_of_pages, final_page)):
        page = reader.pages[page_num].extract_text()
        pages += page
    return pages

if __name__ == '__main__':
    doc_path_name = 'documents/MuonKiepNhanSinh-PDF.pdf'
    pages = get_pdf_text(doc_path_name)
    pages = pages.replace('\n', ' ')
    
    model = OpenAI(temperature=0)
    summary_chain = load_summarize_chain(llm=model, chain_type='map_reduce')
    summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=summary_chain)
    try:
        print('output(AnalyzeDocumentChain):', summarize_document_chain.run(pages))
    except Exception as e:
        print('Exception:', e)