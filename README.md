# pdf-to-text-only-pdf
This converts most PDF files into a text only PDF file. This script strips a PDF document of all images, designs, etc and only keeps the text

## Description 
This script takes a PDF input file and strips it clean of all objects, formatting, etc and only keeps a text-only version of the PDF. The text formatting and positions will remain almost the same as your input PDF with just a few artifacts here and there depending on your input PDF's formatting. The output PDF will keep all the pages the same so you wont have text from page 3 overlapping into page 4 nor would you have page 3 taking up two pages causing a complete break in the total number of PDF pages. This is very useful for people who would like to keep a text only version of their PDF documents to use with AI or some other script.

## Usage
This was a script I made for my specific use scenerio so if you use it yourself, be sure to modify a few variables and sections of this script to better match the layout and formatting of your input PDF file.
There are a few things to note regarding this script:
1. This script is designed to take in page numbers that are in the footer section of the PDF file and output it in the footer of your output PDF document. If your PDF has no page numbers, I suggest making sure your output file is free from artifacts as I have not tried this script on a PDF with no page numbers.
2. This script has a mechanism that reduces each page's output font size if the page's content begins to overflow in either direction. You can modify these values by following the "What to change' instructions below.

## What to change

Required:
You must change your input PDF and output.pdf variables at the bottom of the script.
```
create_text_only_pdf("test7.pdf", "output.pdf")
```
"test7.pdf" will need to be changed to your input pdf file and "output.pdf" should be changed to your output file name


Optional:
You can also modify these variables to ensure that your output PDF file is free from any visual defects or artifacts. 
```
def create_text_only_pdf(input_pdf, output_pdf, initial_font_size=10, line_spacing=1.2, min_font_size=5, footer_height=50):
```

1. initial_font_size=10  -- This can be changed into your output document's default font size
2. line_spacing=1.2 -- You can mofify your line spacing here
3. min_font_size=5 -- This will be the absolute lowest a page's font size can go. From the script there is a check in place that watches out for text overflow, if overflow is detected, the script will reduce the font size down to this minimum variable until all text fits or the minimum is reached.
4. footer_height=50 -- This is the reserved space for page numbers at the bottom of each page
