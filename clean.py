import fitz  # PyMuPDF

def create_text_only_pdf(input_pdf, output_pdf, initial_font_size=10, line_spacing=1.2, min_font_size=5, footer_height=50):
    doc = fitz.open(input_pdf)
    new_doc = fitz.open()  # Create a new PDF to hold the text
    
    def add_text_block(new_page, text, rect, placed_blocks, font_size, line_spacing, footer_height):
        """Adds a text block to the page while avoiding vertical overlaps and preserving footer space."""
        current_font_size = font_size
        page_height = new_page.rect.height - footer_height  # Reserve space for the footer
        
        while current_font_size >= min_font_size:
            block_height = (len(text.split('\n')) + 1) * current_font_size * line_spacing
            rect.y1 = rect.y0 + block_height

            while any(rect.intersects(pb) for pb in placed_blocks) and rect.y1 <= page_height:
                rect.y0 += current_font_size * line_spacing
                rect.y1 += current_font_size * line_spacing

            if rect.y1 <= page_height:
                new_page.insert_text(rect.tl, text, fontsize=current_font_size)
                placed_blocks.append(fitz.Rect(rect))
                return True  # Block placed successfully
            
            current_font_size -= 1  # Reduce font size and try again

        return False  # Could not place block

    for page_number, page in enumerate(doc):
        new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
        text_blocks = page.get_text("blocks")
        text_blocks.sort(key=lambda block: (block[1], block[0]))
        
        placed_blocks = []  # Track placed text blocks
        font_size = initial_font_size  # Start with the initial font size

        for block in text_blocks:
            rect = fitz.Rect(block[:4])
            text = block[4].strip()
            
            if rect.y0 >= new_page.rect.height - footer_height:
                # This block is in the footer region, copy it as is
                new_page.insert_text(rect.bl, block[4], fontsize=font_size)
            elif text:  # If there's text to process and it's not in the footer
                success = add_text_block(new_page, text, rect, placed_blocks, font_size, line_spacing, footer_height)
                if not success:
                    print(f"Text block overflow on page {page_number + 1}. Content may be truncated.")

    new_doc.save(output_pdf)
    new_doc.close()
    doc.close()

# Usage example
create_text_only_pdf("test7.pdf", "output.pdf")
