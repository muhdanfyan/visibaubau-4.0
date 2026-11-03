import os

md_file = '/Users/pondokit/Herd/retribusi-api/docs/Dokumen_Perencanaan_Sistem_Pendapatan_Baubau.md'
html_file = '/Users/pondokit/Herd/visibaubau-4.0/old/dokumen/Dokumen_Perencanaan_Sistem_Pendapatan_Baubau.html'

for file_path in [md_file, html_file]:
    with open(file_path, 'r') as f:
        content = f.read()

    # Remove invalid rx:5px,ry:5px
    content = content.replace(',rx:5px,ry:5px', '')
    
    # Restrict size
    content = content.replace('<div class="mermaid">', '<div class="mermaid" style="max-width: 800px; margin: 20px auto;">')

    with open(file_path, 'w') as f:
        f.write(content)

