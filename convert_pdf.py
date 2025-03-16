import fitz  # PyMuPDF
import os

# Create output directory if it doesn't exist
os.makedirs('prob_images', exist_ok=True)

# Open the PDF
pdf = fitz.open('prob.pdf')

# Convert each page to an image
for i, page in enumerate(pdf):
    # Render page to an image with higher resolution
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))  # 3x zoom for better quality
    # Save the image
    pix.save(f"prob_images/slide{i+1:03d}.png")

pdf.close()
