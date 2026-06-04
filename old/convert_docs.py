import os
import re

doc_mapping = [
    ("blueprint-baubau-4.0.html", "dokumen/visi-roadmap-baubau-4.0.html", "Blueprint Baubau 4.0"),
    ("laporan-lengkap.html", "dokumen/laporan-lengkap.html", "Laporan Lengkap"),
    ("infrastruktur.html", "dokumen/laporan-teknis-infrastruktur-digital.html", "Laporan Infrastruktur"),
    ("keamanan-jaringan.html", "dokumen/master-plan-keamanan-jaringan.html", "Keamanan Jaringan"),
    ("studi-kelayakan.html", "dokumen/studi-kelayakan-e-retribusi.html", "Studi Kelayakan E-Retribusi"),
    ("rab.html", "dokumen/rab-blueprint-baubau-4.0.html", "RAB Blueprint")
]

template_top = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} - Transformasi Digital Kota Baubau 4.0</title>
  <link rel="icon" href="../../assets/img/logo/logobaubau4.0.png" type="image/png">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>tailwind.config={{theme:{{extend:{{colors:{{primary:{{DEFAULT:'#2F80ED',dark:'#1e3a5f',light:'#4A9AF5'}},accent:{{DEFAULT:'#F59E0B',light:'#FCD34D'}}}},fontFamily:{{sans:['Plus Jakarta Sans','system-ui','sans-serif']}}}}}}}}</script>
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <link rel="stylesheet" href="../css/style.css">
  <style>
    /* Legacy Document Styles */
    .document-container {{ background: #e0e0e0; font-family: 'Times New Roman', serif; padding: 20px 0; color: #333; }}
    .document-container .page {{
        width: 21cm;
        min-height: 29.7cm;
        padding: 1.5cm;
        margin: 0 auto 1.5cm;
        background: white;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        position: relative;
        box-sizing: border-box;
    }}
    .document-container .page-cover {{ display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }}
    .document-container .page-cover .logo {{ width: 120px; margin-bottom: 30px; }}
    .document-container .page-cover h1 {{ font-family: 'Georgia', serif; font-size: 2.5rem; color: #1a237e; margin-bottom: 15px; font-weight:bold; border:none; }}
    .document-container .page-cover h2 {{ font-size: 1.4rem; color: #555; font-weight: 400; border:none; }}
    .document-container .page-footer {{ position: absolute; bottom: 1cm; left: 1.5cm; right: 1.5cm; text-align: center; font-size: 9pt; color: #999; }}
    .document-container h1, .document-container h2, .document-container h3, .document-container h4 {{ font-weight: 700; color: #1a237e; margin-top: 15px; margin-bottom: 10px; border-bottom: 2px solid #dfe3ee; padding-bottom: 6px; }}
    .document-container h1 {{ font-size: 18pt; }}
    .document-container h2 {{ font-size: 15pt; }}
    .document-container h3 {{ font-size: 13pt; }}
    .document-container p, .document-container li {{ font-size: 11pt; line-height: 1.6; text-align: justify; }}
    .document-container ul, .document-container ol {{ padding-left: 20px; margin-bottom: 10px; }}
    .document-container .content-img {{ max-width: 75%; margin: 15px auto; display: block; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
    .document-container .full-width-img {{ max-width: 100%; }}
    .document-container table {{ width: 100%; border-collapse: collapse; margin-bottom: 15px; font-size: 10pt; }}
    .document-container th, .document-container td {{ border: 1px solid #ddd; padding: 8px; }}
    .document-container th {{ background-color: #f2f2f2; font-weight: bold; text-align: left; }}
    .document-container .info-card {{ background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #3B5998; margin-bottom:15px; }}
    .document-container .info-card h5 {{ font-weight: 700; color: #3B5998; margin-bottom: 5px; font-size: 11pt; border:none; }}
    @media (max-width: 768px) {{
        .document-container .page {{ width: 100%; padding: 20px; margin-bottom: 20px; min-height:auto; }}
    }}
  </style>
</head>
<body class="font-sans antialiased bg-slate-50">
  <div id="header-placeholder"></div>

  <main class="pt-24 pb-20">
    <div class="max-w-7xl mx-auto px-4 mb-8 flex justify-between items-end">
      <div>
        <h1 class="text-3xl font-bold text-slate-900 mb-2">{title}</h1>
        <p class="text-slate-500">Pratinjau Dokumen Resmi Baubau 4.0</p>
      </div>
      <button onclick="window.print()" class="hidden md:flex px-4 py-2 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition-colors items-center gap-2">
        <i data-lucide="printer" class="w-4 h-4"></i> Cetak Dokumen
      </button>
    </div>

    <div class="document-container w-full overflow-x-auto">
"""

template_bottom = """
    </div>
  </main>

  <div id="footer-placeholder"></div>
  <script src="../js/main.js"></script>
  <script>lucide.createIcons();</script>
</body>
</html>
"""

for dest_file, src_file, title in doc_mapping:
    if not os.path.exists(src_file):
        print(f"Skipping {src_file}, not found.")
        continue
        
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract everything inside body, but ignore scripts and print-fab
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
    if body_match:
        body_content = body_match.group(1)
        
        # Remove old print fab
        body_content = re.sub(r'<div class="print-fab"[^>]*>.*?</div>', '', body_content, flags=re.DOTALL)
        
        # Fix image paths. Old paths are `../assets/img/...` and the new file is in `new/dokumen/`
        # They will still need `../../assets/` because we are at `new/dokumen/` and assets are at the root `assets/`
        # The old files were in `dokumen/` so `../assets/` goes to root `assets/`.
        # In new structure, `new/dokumen/` -> `../../assets/`.
        body_content = body_content.replace('../assets/', '../../assets/')
        
        # Write to new file
        full_html = template_top.format(title=title) + body_content + template_bottom
        with open(f"new/dokumen/{dest_file}", "w", encoding='utf-8') as out_f:
            out_f.write(full_html)
        print(f"Successfully converted {dest_file}")
    else:
        print(f"Could not find body in {src_file}")

