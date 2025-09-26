import re
import os

def extract_data_from_report(file_content, file_path):
    extracted_records = []
    keywords = [
        "Internet",
        "Pengadaan Aplikasi",
        "Infrastruktur IT",
        "Belanja Perangkat Lunak"
    ]

    # Extract year and month from file path
    path_parts = file_path.split(os.sep)
    year = "Tahun Tidak Diketahui"
    month = "Bulan Tidak Diketahui"
    for part in path_parts:
        if re.match(r"^\d{4}$", part):
            year = part
        if "laporan-bulan-" in part:
            month_num_match = re.search(r"laporan-bulan-(\d+)", part)
            if month_num_match:
                month_map = {
                    "1": "Januari", "2": "Februari", "3": "Maret", "4": "April",
                    "5": "Mei", "6": "Juni", "7": "Juli", "8": "Agustus",
                    "9": "September", "10": "Oktober", "11": "November", "12": "Desember"
                }
                month = month_map.get(month_num_match.group(1), f"Bulan {month_num_match.group(1)}")
            break

    # Extract institution from the header (first few lines)
    institution = "Institusi Tidak Diketahui"
    lines = file_content.split('\n')
    for i, line in enumerate(lines[:10]): # Check first 10 lines for institution
        if "DEWAN PERWAKILAN RAKYAT DAERAH KOTA BAUBAU" in line.upper():
            institution = "SEKRETARIAT DEWAN PERWAKILAN RAKYAT DAERAH KOTA BAUBAU"
            break
        elif "DINAS" in line.upper() or "BADAN" in line.upper() or "KANTOR" in line.upper() or "SEKRETARIAT" in line.upper():
            if len(line.strip()) > 5 and not re.search(r'\d', line.strip()):
                institution = line.strip()
                break
    
    # Regex for monetary values (e.g., 1.234.567 or 123.456,00)
    money_pattern = r'\d{1,3}(?:\.\d{3})*(?:,\d{2})?'
    
    # Iterate through lines to find keywords and extract data
    for line_num, line in enumerate(lines):
        for keyword in keywords:
            if keyword.lower() in line.lower():
                nama_pengerjaan = line.strip()
                bidang = "IT/Digital" # Inferred
                nama_kegiatan = nama_pengerjaan
                
                total_anggaran = "Tidak Diketahui"
                penanggung_jawab = "Tidak Diketahui"

                # Attempt to extract Realisasi (Rp.)
                all_money_values_in_line = re.findall(money_pattern, line)
                if len(all_money_values_in_line) >= 3:
                    total_anggaran = all_money_values_in_line[2]

                # Attempt to extract Penanggung Jawab
                parts = [p.strip() for p in re.split(r'\s{2,}', line) if p.strip()]
                
                if parts:
                    last_part = parts[-1]
                    if not re.match(r'^\d+(?:\,\d+)?$', last_part) and \
                       not re.match(money_pattern, last_part) and \
                       len(last_part.split()) <= 5 and \
                       not re.search(r'\d', last_part):
                        penanggung_jawab = last_part
                    else:
                        if len(parts) >= 2:
                            second_last_part = parts[-2]
                            if not re.match(r'^\d+(?:\,\d+)?$', second_last_part) and \
                               not re.match(money_pattern, second_last_part) and \
                               len(second_last_part.split()) <= 5 and \
                               not re.search(r'\d', second_last_part):
                                penanggung_jawab = second_last_part

                extracted_records.append({
                    "nama_pengerjaan": nama_pengerjaan,
                    "bidang": bidang,
                    "institusi": institution,
                    "file_mana": file_path,
                    "nama_kegiatan": nama_kegiatan,
                    "waktu_pengerjaan": f"{month} {year}",
                    "total_anggaran": total_anggaran,
                    "penanggung_jawab": penanggung_jawab
                })
    return extracted_records

if __name__ == "__main__":
    # Read file paths from the temporary file
    file_paths_file = "file_paths.txt"
    full_file_paths = []
    try:
        with open(file_paths_file, 'r', encoding='utf-8') as f:
            for line in f:
                full_file_paths.append(line.strip())
    except FileNotFoundError:
        print(f"Error: {file_paths_file} not found. Please ensure it exists and contains file paths.")
        exit(1)

    all_extracted_data = []

    for f_path in full_file_paths:
        try:
            with open(f_path, 'r', encoding='utf-8') as f:
                content = f.read()
            all_extracted_data.extend(extract_data_from_report(content, f_path))
        except Exception as e:
            # print(f"Error reading or processing file {f_path}: {e}") # Suppress for cleaner output
            pass # Continue processing other files even if one fails

    output_content = "Rekapitulasi Pengeluaran Terkait IT/Digital\n\n"
    output_content += "Catatan: Ekstraksi data dari file teks tidak terstruktur mungkin tidak 100% akurat.\n\n"
    output_content += "{:<50} {:<20} {:<60} {:<80} {:<30} {:<20} {:<20}\n".format(
        "Nama Pengerjaan", "Bidang", "Institusi/Dinas", "File Sumber", "Waktu Pengerjaan", "Anggaran (Rp.)", "Penanggung Jawab"
    )
    output_content += "="*280 + "\n"

    for record in all_extracted_data:
        output_content += "{:<50} {:<20} {:<60} {:<80} {:<30} {:<20} {:<20}\n".format(
            record.get("nama_pengerjaan", "N/A")[:48], # Truncate for display
            record.get("bidang", "N/A"),
            record.get("institusi", "N/A")[:58], # Truncate for display
            os.path.basename(record.get("file_mana", "N/A"))[:78], # Just filename, truncated
            record.get("waktu_pengerjaan", "N/A"),
            record.get("total_anggaran", "N/A"),
            record.get("penanggung_jawab", "N/A")
        )

    with open("rekap_pengeluaran_it.txt", "w", encoding="utf-8") as outfile:
        outfile.write(output_content)

    print("Data pengeluaran terkait IT/Digital telah berhasil diekstrak dan disimpan ke rekap_pengeluaran_it.txt")