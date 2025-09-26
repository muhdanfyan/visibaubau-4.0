import os
import re

def combine_txt_files_in_subfolders():
    combined_files_info = []
    
    all_txt_files_list = []
    try:
        with open("all_txt_files.txt", 'r', encoding='utf-8') as f:
            for line in f:
                # Clean the file path: remove leading/trailing quotes and commas
                cleaned_path = line.strip().strip('",').strip('"')
                if cleaned_path: # Ensure it's not an empty string after cleaning
                    all_txt_files_list.append(cleaned_path)
    except FileNotFoundError:
        print("Error: all_txt_files.txt not found. Please ensure it exists and contains file paths.")
        return []

    unique_txt_dirs = set()
    for file_path in all_txt_files_list:
        dir_path = os.path.dirname(file_path)
        if re.search(r'laporan-bulan-\d+-txt$', dir_path):
            unique_txt_dirs.add(dir_path)

    for current_dir in unique_txt_dirs:
        path_parts = current_dir.split(os.sep)
        year = "Tahun Tidak Diketahui"
        month_num = None

        for part in path_parts:
            if re.match(r"^\d{4}$", part):
                year = part
            month_match = re.search(r"laporan-bulan-(\d+)-txt", part)
            if month_match:
                month_num = month_match.group(1)
                break
        
        if month_num:
            parent_dir = os.path.dirname(current_dir)
            output_filename = os.path.join(parent_dir, f"laporan-bulan-{month_num}-gabungan.txt")

            # --- Debugging line ---
            # print(f"Attempting to write to: {output_filename}")
            # --- End Debugging line ---

            # Ensure the parent directory exists
            try:
                os.makedirs(parent_dir, exist_ok=True)
            except Exception as e:
                print(f"Error creating directory {parent_dir}: {e}")
                continue

            files_to_combine = [f for f in all_txt_files_list if f.startswith(current_dir)]
            
            if not files_to_combine:
                continue

            combined_content = ""
            for file_path in files_to_combine:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        combined_content += f.read() + "\n\n--- End of " + os.path.basename(file_path) + " ---\n\n"
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
            
            try:
                with open(output_filename, 'w', encoding='utf-8') as outfile:
                    outfile.write(combined_content)
                combined_files_info.append(f"Combined files from {current_dir} into {output_filename}")
            except Exception as e:
                print(f"Error writing to {output_filename}: {e}")
    
    return combined_files_info

if __name__ == "__main__":
    results = combine_txt_files_in_subfolders()
    for result in results:
        print(result)
    print("Proses penggabungan file selesai.")
