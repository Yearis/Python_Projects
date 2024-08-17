import os

def check_file_name(file_name):
    try:
        if not file_name.lower().endswith('.pdf'):
            raise ValueError(f'{file_name} is invalid.')
    except ValueError as e:
        print(e)
        return False
    return True

pdf_lists = []
j = int(input("Enter the number of files you want to merge:\n"))

for i in range(j):
    name = input("Enter the file name: ")
    if os.path.exists(name):
        if check_file_name(name):
            pdf_lists.append(name)
        else:
            print(f'{name} is invalid. It should end with ".pdf".')
    else:
        print(f'{name} doesn\'t exist.')
        yn = input("Do you want to create it? Yes or No: ").lower()
        if yn == "yes" or yn == "y":
            with open(name, 'w') as f:
                write = input("Write something: ")
                f.write(write)
            if os.path.getsize(name) == 0:
                print(f"The file {name} was skipped as it was empty.")
            else:
                if check_file_name(name):
                    pdf_lists.append(name)
                else:
                    print(f'The file {name} is invalid. It should end with ".pdf".')
        elif yn == "no" or yn == "n":
            print("Okay")
        else:
            print("Invalid input.")

import PyPDF2
merger = PyPDF2.PdfMerger()

for pdf in pdf_lists:
    merger.append(pdf)

name_merged_file = input("Enter the name of your file: ")
if check_file_name(name_merged_file):
    merger.write(name_merged_file)
    merger.close()
    print(f"PDFs have been merged as {name_merged_file}")
else:
    print(f"{name_merged_file} is invalid. It should end with '.pdf'.")





