import re

#Parse input file
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

#Method to fetch column data by column name
def get_column_by_name(file_path, column_name, delimiter="\t"):
        column_data = []
        with open(file_path, 'r') as file:
            for line in file:
                Found = False
                headerstr="----------------------------------"
                if headerstr in line:
                    Found = True
                    header = file.readline().strip().split(delimiter)
                    column_index = header.index(column_name)
                if Found:
                    for linenew in file:
                        lines = file.readlines()
                        print(lines)
                        for newline in lines:
                            print(newline.split())
                            values = newline.strip().split(delimiter)

                            print(values[column_index])
                            column_data.append(values[column_index])
                        return column_data

file_path = "C:\\Users\\swbp\\Downloads\\network_element_data.txt"
result_lines = parse_text_file(file_path)
result =''.join(result_lines)
network_element_name = extract_ne_name(result)
print("Network element name:", network_element_name)
retcode = extract_ret_code(result).split(" ", 1)
print("Command execution status is:", retcode[1].strip())
column_name = "Csg indicator"
data = get_column_by_name(file_path, column_name)
