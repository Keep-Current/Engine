# -*- coding: utf-8 -*-
import textract


class Convert:

    def file2text(filename):
        """
        This method recieves a filename and extracts the text
        out of it into a string

        Arguments:
            filename {[string]} -- a path string to the file to extract
        """

        text = textract.process('path/to/a.pdf', method='pdfminer')
        return text
