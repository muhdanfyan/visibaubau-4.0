# Dokumentasi Komparasi 8 Web Scraper Tools

**Tanggal:** 27 Mei 2026
**Tujuan:** Membandingkan 8 tools scraping untuk kebutuhan smart city, data publik, dan data pemerintahan
**Fork oleh:** muhdanfyan

---

## Daftar Isi

1. [Ringkasan & Tabel Perbandingan](#ringkasan--tabel-perbandingan)
2. [1. Crawl4AI](#1-crawl4ai)
3. [2. Firecrawl](#2-firecrawl)
4. [3. Scrapy](#3-scrapy)
5. [4. Crawlee](#4-crawlee)
6. [5. Playwright](#5-playwright)
7. [6. ScrapeGraphAI](#6-scrapegraphai)
8. [7. Browser-Use](#7-browser-use)
9. [8. Katana](#8-katana)
10. [Rekomendasi untuk Smart City / Data Publik / Data Pemerintah](#rekomendasi)
11. [Saran Kombinasi Tools](#saran-kombinasi-tools)

---

## Ringkasan & Tabel Perbandingan

| No | Tool | Bahasa/Framework | Lisensi | Metode Scraping | Support JS | Anti-Block | AI-Powered |
|----|------|-----------------|---------|-----------------|-----------|------------|------------|
| 1 | **Crawl4AI** | Python | Apache 2.0 | Async browser-based | Ya (Playwright) | Ya (3-tier anti-bot) | LLM-ready output |
| 2 | **Firecrawl** | Python/Node.js/Go | AGPL-3.0 | API + browser-based | Ya | Ya (built-in proxy rotation) | LLM-ready output |
| 3 | **Scrapy** | Python | BSD-3 | HTTP request-based | Tidak native | Via middleware | Tidak |
| 4 | **Crawlee** | TypeScript/Node.js | Apache 2.0 | HTTP + Playwright/Puppeteer | Ya | Ya (proxy rotation + session mgmt) | Tidak |
| 5 | **Playwright** | Python/Node.js/Java/.NET | Apache 2.0 | Browser automation (headless) | Ya (native) | Tidak built-in | Tidak |
| 6 | **ScrapeGraphAI** | Python | MIT | LLM + graph pipeline | Ya (Playwright) | Tidak built-in | Ya (LLM-based) |
| 7 | **Browser-Use** | Python | MIT | AI agent + browser automation | Ya (native) | Via cloud version | Ya (LLM agent) |
| 8 | **Katana** | Go | MIT | HTTP + headless Chrome | Ya (opsional) | Tidak built-in | Tidak |

---

## 1. Crawl4AI

- **Repositori Fork:** [muhdanfyan/crawl4ai](https://github.com/muhdanfyan/crawl4ai)
- **Repositori Asli:** [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
- **Bahasa/Framework:** Python
- **Lisensi:** Apache 2.0
- **Stars:** 50k+

### Fungsi Utama
Web crawler dan scraper open-source yang mengubah konten web menjadi Markdown siap-LLM. Mendukung ekstraksi konten dengan browser headless (Playwright di backend), anti-bot detection 3-tier, deep crawling, dan LLM extraction.

### Kelebihan
- Output LLM-ready (Markdown bersih dengan heading, tabel, code, citation hints)
- Anti-bot detection 3-tier otomatis dengan proxy escalation
- Sangat cepat berkat async browser pool dan caching
- Kontrol penuh: session, proxy, cookies, user scripts, hooks
- Zero konfigurasi API key, bisa CLI dan Docker
- Deep crawl dengan crash recovery dan resume state
- 50k+ stars, komunitas sangat aktif

### Kekurangan
- Masih relatif baru dibanding Scrapy
- Dokumentasi masih berkembang
- Bergantung pada Playwright untuk rendering browser
- Fitur anti-block masih dalam tahap pengembangan aktif (v0.8.x)

### Use Case Terbaik
- **Scraping konten publik** untuk RAG dan LLM pipelines
- Ekstraksi data dari website pemerintah yang tidak terlalu ketat anti-scraping-nya
- Deep crawling dokumentasi publik
- Konversi website ke Markdown untuk knowledge base smart city

### Cara Kerja Singkat
Menggunakan AsyncWebCrawler dengan Playwright di backend. Pengguna bisa menentukan URL, strategy crawling, proxy, dan hooks. Hasil scraping dikembalikan dalam format Markdown, HTML, atau JSON. Bisa dijalankan via Python async, CLI (`crwl`), atau Docker.

---

## 2. Firecrawl

- **Repositori Fork:** [muhdanfyan/firecrawl](https://github.com/muhdanfyan/firecrawl)
- **Repositori Asli:** [mendableai/firecrawl](https://github.com/mendableai/firecrawl)
- **Bahasa/Framework:** Python, Node.js, Go (SDK multi-platform)
- **Lisensi:** AGPL-3.0
- **Stars:** 25k+

### Fungsi Utama
Platform scraping yang menyediakan endpoint Search, Scrape, Crawl, Map, dan Interact. Bisa di-self-host atau menggunakan cloud service. Fokus pada reliability tinggi (96% coverage) dengan proxy rotation otomatis.

### Kelebihan
- Reliability tertinggi (96% web coverage, termasuk JS-heavy pages)
- Latensi P95 3.4 detik untuk jutaan halaman
- Anti-block built-in (rotating proxies, rate limit handling, orchestration)
- Output LLM-ready: Markdown, structured JSON, screenshots
- Bisa self-host (open source)
- Media parsing: PDF, DOCX dari web
- Actions: click, scroll, write sebelum extract
- MCP-compatible untuk AI agents

### Kekurangan
- Versi cloud berbayar (self-host butuh resource)
- Lisensi AGPL-3.0 (restriktif untuk commercial closed-source)
- Setup self-host cukup kompleks
- SDK Python masih kalah mature dibanding Scrapy

### Use Case Terbaik
- **Scraping data publik skala besar** dengan kebutuhan reliability tinggi
- Anti-block untuk situs yang agresif memblokir scraper
- Ekstraksi data real-time untuk dashboard smart city
- Integrasi dengan AI agents / MCP

### Cara Kerja Singkat
Firecrawl menyediakan REST API endpoint. Pengguna mengirim URL dan mendapatkan hasil scraping dalam format yang diinginkan. Di backend, Firecrawl mengelola browser headless, proxy rotation, dan rendering JS secara otomatis. Juga ada fitur Search (search engine + scrape hasilnya) dan Map (discover semua URL di domain).

---

## 3. Scrapy

- **Repositori Fork:** [muhdanfyan/scrapy](https://github.com/muhdanfyan/scrapy)
- **Repositori Asli:** [scrapy/scrapy](https://github.com/scrapy/scrapy)
- **Bahasa/Framework:** Python
- **Lisensi:** BSD-3
- **Stars:** 53k+

### Fungsi Utama
Framework scraping Python yang mature dan komprehensif untuk mengekstrak data terstruktur dari website. Bisa handle crawling skala besar dengan pipeline, middleware, dan item processing.

### Kelebihan
- Paling mature (2008+), dokumentasi sangat lengkap
- Ekosistem middleware dan pipeline sangat kaya
- Performa HTTP request sangat tinggi
- Bisa scale horizontal dengan mudah
- Banyak tools pendukung: Splash (JS rendering), ScrapyRT, Scrapy Cloud
- Didukung Zyte (perusahaan professional scraping)
- BSD-3 license (paling permisif)

### Kekurangan
- Tidak support JavaScript out-of-the-box (butuh Splash/Selenium middleware)
- Learning curve lebih curam dibanding tools modern
- Konfigurasi lebih verbose (spiders, items, pipelines, settings)
- Tidak built-in untuk AI/LLM integration
- Async support baru ditambahkan di versi 2.6+

### Use Case Terbaik
- **Scraping data publik skala enterprise**
- Pipeline data pemerintah yang perlu transformasi kompleks
- Scraping terjadwal dan monitoring
- Proyek yang butuh stabilitas dan mature ecosystem
- Data warehouse / ETL dari web publik

### Cara Kerja Singkat
Pengguna membuat Spider class yang mendefinisikan URL awal, aturan ekstraksi (CSS/XPath selectors), dan pipeline pemrosesan. Scrapy mengelola request queue, download, parsing, item validation, dan export secara otomatis. Bisa diintegrasikan dengan middleware untuk proxy, user-agent rotation, dan JS rendering.

---

## 4. Crawlee

- **Repositori Fork:** [muhdanfyan/crawlee](https://github.com/muhdanfyan/crawlee)
- **Repositori Asli:** [apify/crawlee](https://github.com/apify/crawlee)
- **Bahasa/Framework:** TypeScript / Node.js (juga ada Python version)
- **Lisensi:** Apache 2.0
- **Stars:** 16k+

### Fungsi Utama
Library scraping dan browser automation untuk Node.js yang menyediakan antarmuka tunggal untuk HTTP crawling dan headless browser crawling. Dibangun oleh Apify, platform web scraping enterprise.

### Kelebihan
- Single interface untuk HTTP dan headless browser crawling
- Persistent URL queue (breadth & depth first)
- Pluggable storage (local dan cloud)
- Automatic scaling dengan system resources
- Integrated proxy rotation dan session management
- CLI untuk bootstrap project
- Configurable routing, error handling, retries
- TypeScript dengan generic types
- Docker-ready

### Kekurangan
- Bahasa utama TypeScript/Node.js (bukan Python)
- Lebih berat dibanding Scrapy untuk pure HTTP scraping
- Ekosistem lebih kecil dibanding Scrapy
- Python version masih lebih baru dan kurang mature
- Dependency pada Apify ecosystem

### Use Case Terbaik
- **Scraping data publik dari Node.js ecosystem**
- Proyek yang butuh JavaScript/TypeScript stack
- Aplikasi yang perlu browser automation + HTTP crawling dalam satu framework
- Integration dengan Apify platform untuk scale

### Cara Kerja Singkat
Pengguna membuat Crawler instance (BasicCrawler, CheerioCrawler, PlaywrightCrawler, atau PuppeteerCrawler), mendefinisikan request handler, dan menjalankan dengan URL awal. Crawlee mengelola request queue, session management, proxy rotation, dan penyimpanan hasil secara otomatis.

---

## 5. Playwright

- **Repositori Fork:** [muhdanfyan/playwright](https://github.com/muhdanfyan/playwright)
- **Repositori Asli:** [microsoft/playwright](https://github.com/microsoft/playwright)
- **Bahasa/Framework:** Python, Node.js, Java, .NET
- **Lisensi:** Apache 2.0
- **Stars:** 70k+

### Fungsi Utama
Framework browser automation dari Microsoft yang mendukung Chromium, Firefox, dan WebKit. Bisa digunakan untuk testing, scraping, dan AI agent automation.

### Kelebihan
- Multi-browser (Chromium, Firefox, WebKit) dengan single API
- Auto-waiting dan web-first assertions
- Network interception untuk monitoring request/response
- Screenshot, PDF, video recording
- Browser context isolation
- Sangat fast dibanding Selenium
- Microsoft-backed, komunitas besar
- Multi-language: Python, Node.js, Java, .NET
- MCP server untuk AI agents

### Kekurangan
- Bukan dedicated scraping tool (tidak ada queue management, pipeline, dll)
- Harus manage anti-block sendiri
- Resource heavy (butuh browser binary)
- Tidak ada built-in data pipeline
- Setup awal lebih kompleks

### Use Case Terbaik
- **Scraping JS-heavy websites** (SPA, React, Angular, Vue)
- **Bypass sederhana** dengan browser fingerprint management
- Testing + scraping dalam satu workflow
- Ekstraksi data dari web apps interaktif
- Sebagai engine rendering untuk tools lain (Crawl4AI, Scrapy+Splash)

### Cara Kerja Singkat
Playwright mengontrol browser sesungguhnya (Chromium/Firefox/WebKit) melalui API. Pengguna bisa navigate ke URL, klik elemen, isi form, intercept network requests, dan ekstrak konten. Mendukung headless mode dan bisa digunakan synchronously atau asynchronously.

---

## 6. ScrapeGraphAI

- **Repositori Fork:** [muhdanfyan/scrapegraph-ai](https://github.com/muhdanfyan/scrapegraph-ai)
- **Repositori Asli:** [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai)
- **Bahasa/Framework:** Python
- **Lisensi:** MIT
- **Stars:** 16k+

### Fungsi Utama
Library scraping berbasis LLM dan graph logic. Pengguna cukup menyebut informasi apa yang ingin diekstrak, dan AI akan menentukan cara mengekstraknya secara otomatis.

### Kelebihan
- **Zero-config scraping**: cukup beri prompt, AI yang kerjakan
- Output terstruktur langsung dalam format yang diminta (JSON)
- Mendukung berbagai LLM (OpenAI, Ollama, Claude, Gemini, dll)
- Bisa scraping website dan dokumen lokal (XML, HTML, JSON, Markdown)
- Integrasi dengan LangChain, LlamaIndex, CrewAI
- Licensing MIT (sangat permisif)
- MCP server support

### Kekurangan
- **Butuh LLM API key** (biaya token untuk setiap scraping)
- Lebih lambat karena harus memproses dengan LLM
- Tidak cocok untuk scraping skala besar (mahal)
- Masih bergantung pada Playwright untuk rendering
- Akurasi tergantung model LLM yang digunakan
- Tidak ada anti-block built-in

### Use Case Terbaik
- **Scraping data dari situs kompleks** dengan struktur tidak beraturan
- **Ekstraksi data spesifik** dari halaman pemerintah (misal: nama pejabat, anggaran, jadwal)
- Rapid prototyping scraping tanpa perlu selector
- Scraping untuk proyek kecil dengan budget token terjangkau

### Cara Kerja Singkat
Pengguna mendefinisikan SmartScraperGraph dengan prompt (misal: "Extract all prices and product names") dan source URL. ScrapeGraphAI menggunakan LLM untuk memahami struktur halaman, menentukan elemen yang relevan, dan mengekstrak data ke format JSON. Pipeline scraping-nya terdiri dari graph nodes yang bisa dikustomisasi.

---

## 7. Browser-Use

- **Repositori Fork:** [muhdanfyan/browser-use](https://github.com/muhdanfyan/browser-use)
- **Repositori Asli:** [browser-use/browser-use](https://github.com/browser-use/browser-use)
- **Bahasa/Framework:** Python
- **Lisensi:** MIT
- **Stars:** 55k+

### Fungsi Utama
AI agent yang bisa mengontrol browser untuk menyelesaikan tugas kompleks secara otomatis. Bisa mengisi form, navigasi multi-step, login, dan ekstraksi data dengan instruksi bahasa alami.

### Kelebihan
- **AI-native**: tugas kompleks bisa diselesaikan dengan instruksi bahasa alami
- Sangat powerful untuk task multi-step (login -> search -> extract -> download)
- Benchmark akurasi tinggi untuk task browser
- MIT license
- Integrasi dengan berbagai LLM (OpenAI, Anthropic, Google, lokal)
- Cloud version dengan stealth proxy dan captcha solving
- Komunitas sangat aktif (55k+ stars)
- Custom tools dan hooks

### Kekurangan
- **Sangat lambat** untuk scraping sederhana (butuh LLM call setiap langkah)
- Biaya token LLM tinggi untuk setiap task
- Tidak cocok untuk bulk scraping
- Overhead besar untuk task sederhana
- Butuh dependency Chromium + LLM API key
- Cloud version berbayar

### Use Case Terbaik
- **Scraping data dari portal pemerintah** yang butuh login dan navigasi multi-step
- **Form automation**: mengisi dan submit form secara otomatis
- **Ekstraksi data** dari web apps kompleks (dashboard, portal, sistem informasi)
- Task yang membutuhkan pengambilan keputusan (mana tombol yang diklik, dll)

### Cara Kerja Singkat
Pengguna membuat Agent dengan task dalam bahasa alami (misal: "Go to portal XYZ, login with credentials, find the budget report for 2025, download the PDF"). Agent menggunakan LLM untuk menentukan langkah-langkah yang harus dilakukan, mengontrol browser via Playwright, dan menyelesaikan task secara otonom. Bisa menggunakan local browser atau cloud browser untuk stealth.

---

## 8. Katana

- **Repositori Fork:** [muhdanfyan/katana](https://github.com/muhdanfyan/katana)
- **Repositori Asli:** [projectdiscovery/katana](https://github.com/projectdiscovery/katana)
- **Bahasa/Framework:** Go
- **Lisensi:** MIT
- **Stars:** 10k+

### Fungsi Utama
Next-generation crawling and spidering framework dari ProjectDiscovery. Fokus pada speed, automation pipeline, dan web security reconnaissance. Bisa digunakan untuk crawling endpoint discovery, URL extraction, dan data gathering.

### Kelebihan
- **Sangat cepat** (ditulis dalam Go, kompilasi native)
- Ringan, tidak butuh banyak dependency
- Mendukung standard mode (HTTP) dan headless mode (Chrome)
- Form filling otomatis untuk login
- Scope control dengan field/regex
- Pipeline-friendly: STDIN/STDOUT, JSON output
- Bagus untuk automation pipeline
- MIT license

### Kekurangan
- **Fokus pada URL discovery**, bukan content extraction
- Tidak ada data pipeline/transformasi
- Ekosistem lebih kecil
- Tidak cocok untuk scraping konten mendalam
- Output mentah (URL, paths, form fields) bukan data terstruktur
- Anti-block minimal

### Use Case Terbaik
- **Endpoint discovery**: menemukan semua URL di domain pemerintah
- **Web reconnaissance** untuk security assessment
- **Crawling awal** untuk mapping struktur website sebelum scraping detail
- Automation pipeline untuk bug bounty / security research
- **Finding hidden pages** dan endpoints

### Cara Kerja Singkat
Katana dijalankan sebagai CLI tool dengan target URL. Secara default menggunakan standard mode (HTTP requests) untuk crawl links. Bisa di-switch ke headless mode dengan Chrome untuk JS rendering. Hasil output berupa daftar URL yang ditemukan, bisa difilter berdasarkan scope, field, atau regex.

---

## Rekomendasi

### Untuk Scraping Data Smart City / Data Publik / Data Pemerintah (Tanpa Kena Blokir)

#### Peringkat Rekomendasi:

1. **Firecrawl** (Paling Recommended)
   - Anti-block built-in terbaik (proxy rotation, rate limit handling)
   - Reliability 96% untuk berbagai jenis website
   - Output LLM-ready, bisa untuk dashboard smart city
   - Self-host atau cloud
   - Cocok untuk: scraping data publik skala besar, data real-time

2. **Crawl4AI** (Runner Up)
   - Anti-bot 3-tier dengan proxy escalation
   - Output Markdown bersih untuk RAG/knowledge base
   - Open source, zero API key
   - Cocok untuk: knowledge base smart city, dokumentasi publik

3. **Scrapy + Playwright Middleware** (Untuk Enterprise)
   - Paling mature dan stabil
   - Pipeline komprehensif untuk data transformation
   - Bisa scale horizontal
   - Cocok untuk: scraping terjadwal skala enterprise, ETL pipeline

4. **Browser-Use** (Untuk Kasus Kompleks)
   - Bisa handle login, form, navigasi multi-step
   - Cocok untuk: portal pemerintah yang butuh autentikasi

5. **ScrapeGraphAI** (Untuk Ekstraksi Cerdas)
   - Prompt-based extraction, zero selector
   - Cocok untuk: data spesifik dari halaman kompleks

6. **Katana** (Untuk Discovery Awal)
   - Mapping struktur website sebelum scraping
   - Cocok untuk: menemukan semua endpoint publik

7. **Crawlee** (Untuk Node.js Stack)
   - Cocok jika tech stack sudah Node.js/TypeScript

8. **Playwright** (Sebagai Engine, Bukan Tool Utama)
   - Gunakan sebagai backend rendering untuk tools lain

### Tips Anti-Blokir untuk Scraping Data Pemerintah:

1. **Gunakan Proxy Rotating** - Firecrawl dan Crawl4AI sudah built-in
2. **Rate Limiting** - Jangan request terlalu cepat (delay 2-5 detik antar request)
3. **User Agent Rotation** - Gunakan user agent real browser
4. **Headless Browser** - Jangan pure HTTP request, gunakan browser engine
5. **Respect robots.txt** - Hormati aturan website
6. **Gunakan API Resmi** jika tersedia - Prioritaskan API pemerintah
7. **Schedule scraping** di jam sepi (malam hari / akhir pekan)
8. **Simpan state/kuki** - Untuk session persistence

---

## Saran Kombinasi Tools

| Kombinasi | Kegunaan | Stack |
|-----------|----------|-------|
| **Katana + Crawl4AI** | Katana untuk discover URL, Crawl4AI untuk extract konten | Go + Python |
| **Crawl4AI + Playwright** | Crawl4AI sebagai orchestrator, Playwright sebagai JS engine | Python |
| **Scrapy + Playwright (+ Splash)** | Scrapy untuk pipeline/scaling, Playwright/Splash untuk JS rendering | Python |
| **Firecrawl + Browser-Use** | Firecrawl untuk bulk scraping, Browser-Use untuk task kompleks (login) | Python |
| **Crawlee + Playwright** | Crawlee orchestrator + Playwright browser engine | Node.js |
| **ScrapeGraphAI + Crawl4AI** | ScrapeGraphAI untuk extraction cerdas, Crawl4AI untuk anti-block | Python |
| **Katana + Scrapy** | Katana untuk discovery, Scrapy untuk extract terstruktur | Go + Python |
| **Playwright + BeautifulSoup** | Playwright dapatkan HTML, BeautifulSoup/extract dengan selector | Python |

### Recommended Stack untuk Smart City / Data Publik:

**Stack Primary (Recommended):**
```
Firecrawl (bulk scraping) + Crawl4AI (anti-block + Markdown)
+ Browser-Use (login/form task) + Katana (discovery)
```

**Stack Python Murni:**
```
Crawl4AI (orchestrator + anti-block) + Playwright (engine)
+ ScrapeGraphAI (extraction cerdas untuk data spesifik)
```

**Stack Enterprise:**
```
Scrapy (pipeline + scheduling) + Playwright middleware (JS)
+ API resmi pemerintah (jika ada)
```

---

## Catatan Akhir

- Semua repo sudah di-fork ke [github.com/muhdanfyan](https://github.com/muhdanfyan)
- Dokumentasi ini bisa diupdate seiring perkembangan tools
- Untuk data sensitif, pastikan mematuhi kebijakan website dan hukum yang berlaku
- Prioritaskan penggunaan API resmi pemerintah jika tersedia

---

*Dokumen dibuat pada 27 Mei 2026 untuk keperluan proyek visibaubau-4.0*
