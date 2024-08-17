import os 

folder_path='NewEnvironment/Files'

files=[
    'kjh.jpg',
    'klh.jpg',
    'lha.jpg',
    'kjg.jpg',
    'kgj.png',
    'kjg.png',
    'jkg.jpeg'
]

for files_name in files:
    file_path=os.path.join(folder_path, files_name)
    if os.path.exists(files_name):
        print(f'{files_name} exists')
        continue
    with open(files_name, 'w') as f:
        f.write('')

png_count=1
jpg_count=1
jpeg_count=1

for file_name in files:
    current_file_path=os.path.join(folder_path , file_name)#this tells us the path of folder and file are joined like NewEnvironment/File/kjh.png
    if file_name.endswith('.png'):
        new_name= f'{png_count}(png).png'
        png_count += 1
    elif file_name.endswith('.jpg'):
        new_name= f'{jpg_count}(jpg).jpg'
        jpg_count += 1
    elif file_name.endswith('.jpeg'):
        new_name= f'{jpeg_count}(jpeg).jpeg'
        jpeg_count += 1
    else:
        continue
    if os.path.exists(new_file_path):
        print(f'Skipped Renaming {file_name} cause it exists.')
        continue
    new_file_path=os.path.join(folder_path , file_name)#this tells us the path of folder and file are joined like NewEnvironment/File/1(png).png
    os.rename(current_file_path, new_file_path)
    print(f'Renamed {file_name} to {new_name}')
print(f"Name Changed.")
