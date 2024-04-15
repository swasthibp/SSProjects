import re
import csv
def write_table_to_csv(table_data, csv_file_path):
    try:
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(table_data)
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def parse_text_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

def extract_ne_name(input_text):
    pattern = r'([a-zA-Z0-9_]+)_network_element'
    match = re.search(pattern, input_text)
    if match:
        return match.group()
    else:
        return None

def extract_ret_code(input_text):
    pattern = r'RETCODE\s*=\s*(.*?)(?=\.)'
    match = re.search(pattern, input_text)
    if match:
        return match.group(1)
    else:
        return None

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
                    table_data.append(line.strip().split('\n'))

    except Exception as e:
        print(f"Error occurred: {e}")

    return table_data

def delete_empty_rows(table_data):
    updated_table = [row for row in table_data if any(row)]
    return updated_table

def delete_last_row(table_data):
    if table_data:
        del table_data[-1]
    return table_data

def fetch_column_values(csv_file, column_name):
    column_values = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        if column_name not in reader.fieldnames:
            print(f"Column '{column_name}' not found in the CSV file.")
            return []
        for row in reader:
            column_values.append(row[column_name])

    return column_values


file_path = "C:\\Users\\swbp\\Downloads\\network_element_data.txt"
result_lines = parse_text_file(file_path)
result =''.join(result_lines)
network_element_name = extract_ne_name(result)
print("Network element name:", network_element_name)
retcode = extract_ret_code(result).split(" ", 1)
print("Operation status is:", retcode[1].strip())
start_marker = "----------------------------------"
end_marker = "(Number of results"


#column_name = "Local Cell ID"
#data = grab_column_data(table, column_name)
#print(data)

#table_data=get_column_by_name(file_path,column_name,"  ")
table = extract_table_from_text_file(file_path, start_marker, end_marker)
'''if table:
    print("Extracted table:")
    for row in table:
        print(row)'''
updated_table = delete_last_row(table)
updated_table_02 = delete_last_row(updated_table)

'''if updated_table_02:
    print("Extracted table:")
    for row in updated_table_02:
        print(row)'''

updated_table_03 = delete_empty_rows(updated_table_02)
if updated_table_03:
    print("Table with empty rows deleted:")
    for row in updated_table_03:
        print(row)

csv_file_path = "table_data.csv"
success = write_table_to_csv(updated_table_03, csv_file_path)
if success:
    print("Table data written to CSV file successfully.")
else:
    print("Failed to write table data to CSV file.")

csv_file = 'table_data.csv'
column_name = 'NB-IoT'
column_values = fetch_column_values(csv_file, column_name)
print(column_values)



