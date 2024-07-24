from sys import argv
from collections import Counter

def main():

    # check the received arguments 
    command = False
    if len(argv) == 3:
        command = argv[2]
        path_string = argv[1]
    elif len(argv) == 2:
        path_string = argv[1]
    else:
        print('Need at least 1 argument, example: [directory path] [command]')
        return

    # check the file and create list with file row
    try:
        rows = load_logs(path_string)
    except FileNotFoundError:
        print('No such file')
        return

    # parse every line
    parsed_data = []
    for line in rows:
        item = parse_log_line(line)
        parsed_data.append(item)

    # grouped by type and print results
    type_counts = count_logs_by_level(parsed_data)
    display_log_counts(type_counts)

    # look filtered command
    if type(command) != bool and command != False:
        command = command.upper()
        result = filter_logs_by_level(parsed_data, command)
        display_filtered_type(result, command)

def parse_log_line(line: str) -> dict:
    splited_row = line.split()
    return {
        "data": splited_row.pop(0),
        "time": splited_row.pop(0),
        "type": splited_row.pop(0),
        "message": " ".join(splited_row),
    }

def load_logs(file_path: str) -> list:
    file_rows = []
    with open(file=file_path, mode='r', encoding='utf-8') as fh:    
        while True:
            line = fh.readline().strip()
            if not line:
                break
            file_rows.append(line)
    return file_rows

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['type'] == level]

def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log['type'] for log in logs))

def display_log_counts(counts: dict):
    headers = ('Рівень логування ', ' Кількість')
    headers_row = '|'.join(headers)
    delimeter = tuple(len(header) for header in headers)
    delimeter_row = '|'.join('-' * length for length in delimeter)

    print(headers_row)
    print(delimeter_row)

    for type, count in counts.items():
        added_type_len = len(headers[0]) - len(type)
        print(type + ' ' * added_type_len + '| ' + str(count))
    
def display_filtered_type(data: dict, type: str):
    print()
    if data:
        print(f"Деталі логів для рівня '{type}'")
    else:
        print("Немає рядків для цього рівня логів")
    for line in data:
        print(line["data"], line["time"], "-", line["message"])
    pass

if __name__ == '__main__':
    main()
