FILENAME = "subject_data.txt"

def main():
    data = get_data()
    display_subject_details(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []

    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        data_list.append(parts)
    input_file.close()
    return data_list

def display_subject_details(data):
    for subject_data in data:
        subject_code, lecturer, num_students = subject_data
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")

main()