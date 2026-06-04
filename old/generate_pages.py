import os

app_pages = [
    {"file": "e-retribusi.html", "title": "E-Retribusi", "icon": "credit-card", "desc": "Digitalisasi pembayaran retribusi untuk transparansi dan kemudahan masyarakat."},
    {"file": "surat-digital.html", "title": "Surat Digital", "icon": "file-signature", "desc": "Sistem persuratan elektronik untuk efisiensi birokrasi pemerintahan."},
    {"file": "lapor-baubau.html", "title": "Lapor Baubau", "icon": "message-square-warning", "desc": "Layanan aspirasi dan pengaduan online rakyat berbasis digital."},
    {"file": "portal-publik.html", "title": "Portal Publik", "icon": "globe", "desc": "Pintu gerbang informasi tunggal untuk seluruh layanan masyarakat Kota Baubau."}
]

dokumen_pages = [
    {"file": "blueprint-baubau-4.0.html", "title": "Blueprint Baubau 4.0", "desc": "Dokumen rancang bangun komprehensif Transformasi Digital Kota Baubau."},
    {"file": "laporan-lengkap.html", "title": "Laporan Lengkap", "desc": "Laporan eksekutif pelaksanaan kajian dan rancangan Baubau 4.0."},
    {"file": "infrastruktur.html", "title": "Laporan Infrastruktur", "desc": "Kajian teknis kondisi eksisting dan kebutuhan infrastruktur jaringan fiber optik."},
    {"file": "keamanan-jaringan.html", "title": "Keamanan Jaringan", "desc": "Master plan arsitektur dan sistem keamanan informasi (Cyber Security)."},
    {"file": "studi-kelayakan.html", "title": "Studi Kelayakan E-Retribusi", "desc": "Kajian potensi PAD dan kelayakan implementasi e-retribusi daerah."},
    {"file": "rab.html", "title": "Kumpulan RAB", "desc": "Rincian Anggaran Biaya (RAB) untuk berbagai proyek digitalisasi (SIMKES, MPAD, Blueprint, dll)."}
]

template = """<!DOCTYPE html>
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
</head>
<body class="font-sans antialiased bg-slate-50 flex flex-col min-h-screen">
  <div id="header-placeholder"></div>

  <main class="flex-grow flex items-center justify-center pt-32 pb-20 px-4">
    <div class="max-w-2xl w-full text-center" data-animate>
      <div class="w-24 h-24 mx-auto mb-8 bg-blue-100 rounded-3xl flex items-center justify-center shadow-inner">
        <i data-lucide="{icon}" class="w-12 h-12 text-blue-600"></i>
      </div>
      <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 mb-6">{title}</h1>
      <p class="text-lg text-slate-600 mb-10 leading-relaxed">{desc}</p>
      
      <div class="glass-card p-8 border border-slate-200">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-amber-100 text-amber-700 rounded-full font-semibold text-sm mb-4">
          <i data-lucide="clock" class="w-4 h-4"></i> Sedang Dalam Pengembangan
        </div>
        <p class="text-slate-500 text-sm">Halaman atau dokumen ini sedang dalam tahap finalisasi dan akan segera tersedia untuk publik.</p>
      </div>

      <div class="mt-10">
        <a href="../index.html" class="inline-flex items-center gap-2 text-blue-600 font-semibold hover:text-blue-700 transition-colors">
          <i data-lucide="arrow-left" class="w-4 h-4"></i> Kembali ke Beranda
        </a>
      </div>
    </div>
  </main>

  <div id="footer-placeholder"></div>
  <script src="../js/main.js"></script>
  <script>lucide.createIcons();</script>
</body>
</html>
"""

os.makedirs("new/app", exist_ok=True)
os.makedirs("new/dokumen", exist_ok=True)

for p in app_pages:
    with open(f"new/app/{p['file']}", "w") as f:
        f.write(template.format(title=p['title'], desc=p['desc'], icon=p.get('icon', 'smartphone')))

for p in dokumen_pages:
    with open(f"new/dokumen/{p['file']}", "w") as f:
        f.write(template.format(title=p['title'], desc=p['desc'], icon=p.get('icon', 'file-text')))

print("Generated all app and dokumen pages successfully.")
