import csv
import re

#Method to parse the input file
def parse_text_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

#Method to extract network element name
def extract_ne_name(input_text):
    pattern = r'([a-zA-Z0-9_]+)_network_element'
    match = re.search(pattern, input_text)
    if match:
        return match.group()
    else:
        return None

#Method to extract execution status
def extract_ret_code(input_text):
    pattern = r'RETCODE\s*=\s*(.*?)(?=\.)'
    match = re.search(pattern, input_text)
    if match:
        return match.group(1)
    else:
        return None

#Method to convert table data to csvfile
def write_table_to_csv(table_data, csv_file_path):
    try:
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(table_data)
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

#Method to convert text input data into tabke values
def extract_table_from_text_file(file_path, start_marker, end_marker):
    table_data = []
    is_extracting = False
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() == start_marker:
                    is_extracting = True
                    continue
                elif line.strip() == end_marker:
                    is_extracting = False
                    break
                if is_extracting:
                    table_data.append(line.strip().split('\t'))

    except Exception as e:
        print(f"Error occurred: {e}")

    return table_data

#Method to remove last line in table data
def delete_last_row(table_data):
    if table_data:
        del table_data[-1]
    return table_data

#Method to remove empty lines in table data
def delete_empty_rows(table_data):
    updated_table = [row for row in table_data if any(row)]
    return updated_table

#Method to extract column data from table by column names
def fetch_column_data(csv_file, column_name):
            column_data = []
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if column_name in row:
                        column_data.append(row[column_name])
            return column_data

file_path = "C:\\Users\\swbp\\Downloads\\network_element_data.txt"
start_marker = "----------------------------------"
end_marker = "---    END"
result_lines = parse_text_file(file_path)
result =''.join(result_lines)
network_element_name = extract_ne_name(result)
print("Network element name:", network_element_name)
retcode = extract_ret_code(result).split(" ", 1)
print("Command execution status is:", retcode[1].strip())
column_name = "Csg indicator"
csv_file_path = "table_data.csv"
table = extract_table_from_text_file(file_path, start_marker, end_marker)
updated_table = delete_last_row(table)
updated_table_02 = delete_last_row(updated_table)
updated_table_03 = delete_empty_rows(updated_table_02)
success = write_table_to_csv(updated_table_03, csv_file_path)
if success:
    print("Table data written to CSV file successfully.")
else:
    print("Failed to write table data to CSV file.")
column_data = fetch_column_data(csv_file_path, column_name)
print(f"Column Data for column name {column_name} are as follows:\n",column_data)
