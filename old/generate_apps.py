import os

apps = [
    {
        "file": "surat-digital.html",
        "title": "Surat Digital (Srikandi)",
        "icon": "file-signature",
        "desc": "Aplikasi Sistem Informasi Kearsipan Dinamis Terintegrasi (SRIKANDI) untuk mewujudkan tata kelola persuratan pemerintahan yang efisien, transparan, dan paperless.",
        "bg_color": "from-indigo-900 to-blue-700",
        "features": [
            {"title": "Disposisi Online", "desc": "Lakukan disposisi surat kapan saja dan di mana saja tanpa menunggu dokumen fisik.", "icon": "send"},
            {"title": "Tanda Tangan Elektronik", "desc": "Integrasi TTE tersertifikasi BSrE untuk menjamin keabsahan dan keamanan dokumen.", "icon": "pen-tool"},
            {"title": "Pelacakan Surat", "desc": "Lacak status dan posisi surat secara real-time dengan barcode khusus.", "icon": "search"},
            {"title": "Arsip Digital Aman", "desc": "Penyimpanan arsip terpusat di Data Center yang aman dari risiko kehilangan.", "icon": "database"},
            {"title": "Akses Mobile", "desc": "Akses dokumen dan lakukan persetujuan langsung dari smartphone Anda.", "icon": "smartphone"}
        ]
    },
    {
        "file": "lapor-baubau.html",
        "title": "Lapor Baubau",
        "icon": "message-square-warning",
        "desc": "Layanan aspirasi dan pengaduan online rakyat. Wadah interaktif bagi warga untuk melaporkan infrastruktur rusak, masalah layanan publik, dan aspirasi lainnya.",
        "bg_color": "from-orange-600 to-red-700",
        "features": [
            {"title": "Laporan Anonim", "desc": "Opsi pelaporan anonim untuk melindungi identitas pelapor dan menjamin keamanan.", "icon": "shield"},
            {"title": "Geo-Tagging", "desc": "Titik lokasi otomatis terekam beserta foto kejadian untuk memudahkan petugas.", "icon": "map-pin"},
            {"title": "Tindak Lanjut Cepat", "desc": "Laporan langsung diteruskan ke OPD terkait dengan SLA respons maksimal 2x24 jam.", "icon": "zap"},
            {"title": "Tracking Laporan", "desc": "Pantau progres penyelesaian laporan Anda mulai dari masuk, diverifikasi, hingga selesai.", "icon": "activity"},
            {"title": "Statistik Publik", "desc": "Transparansi data jumlah laporan dan tingkat penyelesaian oleh tiap OPD.", "icon": "bar-chart-2"}
        ]
    },
    {
        "file": "portal-publik.html",
        "title": "Portal Publik Baubau",
        "icon": "globe",
        "desc": "Pintu gerbang informasi tunggal (Single Window) untuk seluruh layanan masyarakat Kota Baubau, mengintegrasikan berbagai aplikasi OPD dalam satu akses.",
        "bg_color": "from-teal-800 to-emerald-600",
        "features": [
            {"title": "Single Sign-On (SSO)", "desc": "Satu akun terintegrasi NIK untuk mengakses seluruh layanan publik digital Kota Baubau.", "icon": "key"},
            {"title": "Katalog Layanan", "desc": "Direktori lengkap ratusan perizinan dan layanan publik beserta syaratnya.", "icon": "book-open"},
            {"title": "Berita & Pengumuman", "desc": "Informasi resmi, agenda kota, dan pengumuman pemerintah terbaru dan terpercaya.", "icon": "bell"},
            {"title": "Chatbot Cerdas", "desc": "Asisten virtual 24/7 yang siap menjawab pertanyaan dasar mengenai layanan publik.", "icon": "bot"},
            {"title": "Akses Inklusif", "desc": "Antarmuka yang ramah pengguna, mendukung aksesibilitas bagi penyandang disabilitas.", "icon": "accessibility"}
        ]
    }
]

template = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} - Transformasi Digital Kota Baubau 4.0</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="../../assets/img/logo/logobaubau4.0.png" type="image/png">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>tailwind.config={{theme:{{extend:{{colors:{{primary:{{DEFAULT:'#2F80ED',dark:'#1e3a5f',light:'#4A9AF5'}},accent:{{DEFAULT:'#F59E0B',light:'#FCD34D'}}}},fontFamily:{{sans:['Plus Jakarta Sans','system-ui','sans-serif']}}}}}}}}</script>
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body class="font-sans antialiased bg-slate-50">
  <div id="header-placeholder"></div>

  <!-- Hero -->
  <section class="hero-overlay relative pt-32 pb-20 lg:pt-40 lg:pb-28 overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-br {bg_color} z-[1]"></div>
    <div class="absolute inset-0 opacity-20 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] z-[1]"></div>
    <div class="relative z-[2] max-w-4xl mx-auto px-4 sm:px-6 text-center">
      <div class="w-20 h-20 mx-auto mb-8 bg-white/20 backdrop-blur-md rounded-2xl flex items-center justify-center shadow-2xl border border-white/30" data-animate>
        <i data-lucide="{icon}" class="w-10 h-10 text-white"></i>
      </div>
      <h1 class="text-4xl sm:text-5xl font-extrabold text-white tracking-tight mb-6" data-animate data-animate-delay="100">{title}</h1>
      <p class="text-lg text-white/90 leading-relaxed max-w-2xl mx-auto mb-10" data-animate data-animate-delay="200">{desc}</p>
      
      <div class="flex flex-wrap justify-center gap-4" data-animate data-animate-delay="300">
        <button class="px-8 py-3.5 bg-white text-slate-900 font-bold rounded-xl shadow-xl hover:shadow-2xl hover:-translate-y-1 transition-all flex items-center gap-2">
          Buka Aplikasi <i data-lucide="external-link" class="w-4 h-4"></i>
        </button>
      </div>
    </div>
  </section>

  <!-- Fitur Utama -->
  <section class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h2 class="text-3xl font-extrabold text-slate-900 mb-4" data-animate>Fitur & Keunggulan Utama</h2>
        <p class="text-slate-500" data-animate data-animate-delay="100">Solusi digital modern yang dirancang khusus untuk mempermudah layanan dan meningkatkan efisiensi.</p>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {features_html}
      </div>
    </div>
  </section>
  
  <!-- CTA -->
  <section class="py-20 bg-slate-50 border-t border-slate-200">
    <div class="max-w-4xl mx-auto text-center px-4" data-animate>
      <h2 class="text-2xl font-bold text-slate-900 mb-4">Mulai Gunakan {title} Sekarang</h2>
      <p class="text-slate-500 mb-8">Tingkatkan efisiensi kerja dan dapatkan kemudahan layanan publik melalui platform digital terintegrasi Kota Baubau.</p>
      <a href="../index.html" class="inline-flex items-center gap-2 text-blue-600 font-semibold hover:text-blue-800 transition-colors">
        <i data-lucide="arrow-left" class="w-4 h-4"></i> Kembali ke Beranda
      </a>
    </div>
  </section>

  <div id="footer-placeholder"></div>
  <script src="../js/main.js"></script>
  <script>lucide.createIcons();</script>
</body>
</html>
"""

for app in apps:
    features_html = ""
    for idx, f in enumerate(app['features']):
        delay = (idx % 3) * 100
        features_html += f"""
        <div class="p-8 border border-slate-100 rounded-2xl bg-white shadow-sm hover:shadow-xl transition-all duration-300 group" data-animate data-animate-delay="{delay}">
          <div class="w-14 h-14 bg-blue-50 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <i data-lucide="{f['icon']}" class="w-7 h-7 text-blue-600"></i>
          </div>
          <h4 class="text-xl font-bold text-slate-900 mb-3">{f['title']}</h4>
          <p class="text-slate-500 leading-relaxed">{f['desc']}</p>
        </div>
        """
        
    html = template.format(
        title=app['title'],
        desc=app['desc'],
        icon=app['icon'],
        bg_color=app['bg_color'],
        features_html=features_html
    )
    
    with open(f"new/app/{app['file']}", "w") as f_out:
        f_out.write(html)

print("Generated full app landing pages.")
