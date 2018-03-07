## The Cleaner Package
The Cleaner is actually also a Parser.

Its role is to clean the unnecessary HTML sections and elements from the document.
It recieves from the scrapper an HTML file, and needs to determine which sections are unnecessary and irrelevant (menus, ads, maps, photos, etc)

input: HTML Document
output: Clean text document

### How?
 Detect the document type (pdf, text, html). 
 if it is HTML - consider using readability https://github.com/mozilla/readability to simplify it.
 if it's PDF - extract he content into text.