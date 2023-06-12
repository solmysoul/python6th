import  os
import time

current_directory = os.getcwd() # 절대경로를 알려줌
print(current_directory)

# os.mkdir('new_directory') # 파일추가

# os.makedirs('parent_directory/child_directory/grandchild_directory') # /를 통한 중첩 디렉토리

# os.chdir('new_directory')
# current_directory2 = os.getcwd()
# print(current_directory2)

# with open('example.txt','w') as file_object:
#     file_object.write('Hello, World!')

# os.rename('new_directory', 'new_directory2') # 이름 변경
#
# os.rmdir('new_directory2') # 폴더 한개 삭제
#
# os.removedirs('parent_directory/child_directory/grandchild_directory') # 폴더 여러개 삭제

# os.makedirs('parent_directory/child_directory/grandchild_directory')

# for dirpath, dirnames, filenames in os.walk('.'):
#     print(f"디렉터리 경로: {dirpath}")
#     print(f"디렉터리 이름: {dirnames}")
#     print(f"파일이름 : {filenames}")

for dirpath, dirnames, filenames in os.walk('parent_directory'):
    print(f"디렉터리 경로: {dirpath}")
    print(f"디렉터리 이름: {dirnames}")
    print(f"파일이름 : {filenames}")

