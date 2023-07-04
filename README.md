# Summarize PDF - README

This repository contains source code for summarizing PDF documents using the AI Summarize technology. It utilizes the PyPDF2 library for extracting text from PDFs and the LangChain library for performing the summarization.

## Installation

To run the code, you need to install the required libraries. Use the following command to install the dependencies:

```shell
pip install PyPDF2 langchain
```

## Usage

1. Import the necessary modules:

```python
import re
from PyPDF2 import PdfReader
from langchain.chains import AnalyzeDocumentChain
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
```

2. Define a function to extract text from the PDF:

```python
def get_pdf_text(document_path, start_page=1, final_page=999):
    reader = PdfReader(document_path)
    number_of_pages = len(reader.pages)
    print(f'number of pages: {number_of_pages}')
    pages = ''
    for page_num in range(start_page - 1, min(number_of_pages, final_page)):
        page = reader.pages[page_num].extract_text()
        pages += page
    return pages
```

3. Specify the path to the PDF document and extract the text:

```python
if __name__ == '__main__':
    doc_path_name = 'documents/MuonKiepNhanSinh-PDF.pdf'
    pages = get_pdf_text(doc_path_name)
    pages = pages.replace('\n', ' ')
```

4. Initialize the OpenAI language model and the summarization chain:

```python
    model = OpenAI(temperature=0)
    summary_chain = load_summarize_chain(llm=model, chain_type='map_reduce')
    summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=summary_chain)
```

5. Run the summarization process:

```python
    try:
        print('output(AnalyzeDocumentChain):', summarize_document_chain.run(pages))
    except Exception as e:
        print('Exception:', e)
```

## Explanation

The code starts by importing the necessary modules. It then defines a function `get_pdf_text()` to extract the text from the PDF document using the PyPDF2 library. The function reads the PDF pages from the start page to the final page specified and removes any unwanted patterns.

In the main part of the code, the path to the PDF document is specified, and the text is extracted using the `get_pdf_text()` function. The extracted text is cleaned up by replacing newline characters.

Next, the OpenAI language model is initialized with a temperature value of 0, which controls the level of creativity in the generated summaries. The summarization chain is loaded using the language model and the 'map_reduce' chain type.

Finally, the extracted text is passed through the summarization chain using the `run()` function of `AnalyzeDocumentChain`. The generated summary is printed as the output.

Please make sure to replace the `doc_path_name` variable with the actual path to your PDF document before running the code.

That's it! You can now use this code to summarize PDF documents and extract key information efficiently.

**Note:** If you encounter any exceptions during the summarization process, please ensure that you have the required dependencies installed and that the PDF document is accessible at the specified path.

Happy summarizing!