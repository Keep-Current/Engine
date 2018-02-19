Cleaner module cleans the unnecessary HTML sections and elements from the document.
It recieves from the scrapper an HTML file, and needs to determine which sections are unnecessary and irrelevant (menus, ads, maps, photos, etc)

input: HTML Document
output: parsed text document (list of tupples)

How?
1. Detect the document type (pdf, text, html)
2. break the document down to pargraphs, sentences and tokenized words.
3. Perform POS tagging
4. Perform entity detection
5. Perform relation detection
