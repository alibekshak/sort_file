def sort():
    import os 
    os.system('clear')

    list_file = []
    folders = [
        '/Users/apple/Movies', 
        '/Users/apple/Documents', 
        '/Users/apple/Downloads', 
        '/Users/apple/Pictures', 
        '/Users/apple/Music', 
        '/Users/apple/Desktop',  
        '/Users/apple'
        ]


    photo_expansion = [
        "png", "jpg", "jpeg",
        "gif", "HEIC", "(1).png",
        "(2).png", "(1).jpg", "(2).jpg",
        "(1).gif", "(2).gif", "(1).jpeg", 
        "(2).jpeg", "(1).HEIC", "(2).HEIC",
        " (2).HEIC", " (3).HEIC", " (4).HEIC"
    ]


    video_expansion = [
        'mp4', '(1).mp4', '(2).mp4', ' .mp4',
        ' mp4', ' (1).mp4', ' (2).mp4',
        'MP4', '(1).MP4', '(2).MP4', ' .MP4',
        ' MP4', ' (1).MP4', ' (2).MP4',
    ]

    document_expansion = [
        'pdf', 'deb', 'tgz', 'tar.xz', 'xz', 'exe', 'zip', 
        ' .pdf', ' .deb', ' .tgz', ' .tar.xz', ' .xz', ' .exe', 
        ' .zip', '(1).pdf', '(1).deb', '(1).tgz', '(1).tar.xz', 
        '(1).xz','(1).exe', '(1).zip', '(2).pdf', '(2).deb', 
        '(2).tgz', '(2).tar.xz', '(2).xz', '(2).exe', '(2).zip', "dmg", ".dmg" 
        ]

    music_expansion = [
        'mp3', ' .mp3', '(1).mp3', '(2).mp3', '(3).mp3', '(4).mp3',
        'MP3', ' .MP3', '(1).MP3', '(2).MP3', '(3).MP3', '(4).MP3'
        ]



    agreement = input("""
_________________________________________________________________________________
|                                                                                |
|     Я пройдусь по всем перечисленным папкам (y/n)                              |
|                                                                                |
|        [ Видео     Документы    Загрузки    Изображения ]                      |
|        [ Музыка    Рабочий стол                         ]                      |
|                                                                                |
|_____________________[Введите номер папки: """)

    os .system("claer")

    if agreement in ["y", "yes", "Yes", "Y"]:
        try:
            search_file = int(input(
"""_________________________________________________________________________________
|                                                                                |
| Что мне проверить:                                                             |
|                                                                                |
|   1       Видео                                                                |
|   2       Документы                                                            |
|   3       Изображения                                                          |
|   4       Музыка                                                               |
|                                                                                |
|_____________[Введите что нужно отсортировать: """))
        except ValueError:
            os.system("clear")
            return f"Прошу прошения выберите что-то из меню от (от 1 до 4)"

        if search_file == 1:
            os.system("clear")
            os.system("mkdir core")

            with open("core/s_Documents.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[1]} > /Users/apple/Desktop/main/part_2/core/s_Documents.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Documents.bash")

            with open("core/s_Downloads.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[2]} > /Users/apple/Desktop/main/part_2/core/s_Downloads.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Downloads.bash")

            with open("core/s_Pictures.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[3]} > /Users/apple/Desktop/main/part_2/core/s_Pictures.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Pictures.bash")

            with open("core/s_Music.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[4]} > /Users/apple/Desktop/main/part_2/core/s_Music.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Music.bash")

            with open("core/s_Desktop.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[5]} > /Users/apple/Desktop/main/part_2/core/s_Desktop.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Desktop.bash")


            with open("core/s_Documents.txt", "r") as read_file:
                name_items1 = read_file.read().split("\n")
            
            for item in name_items1:
                if item.split(".")[-1] in video_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[1]}/{name_file} {folders[0]}")
                else:
                    continue


            with open("core/s_Downloads.txt", "r") as read_file:
                name_items2 = read_file.read().split("\n")
            
            for item in name_items2:
                if item.split(".")[-1] in video_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[2]}/{name_file} {folders[0]}")
                else:
                    continue


            with open("core/s_Pictures.txt", "r") as read_file:
                name_items3 = read_file.read().split("\n")
            
            for item in name_items3:
                if item.split(".")[-1] in video_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[3]}/{name_file} {folders[0]}")
                else:
                    continue


            with open("core/s_Music.txt", "r") as read_file:
                name_items4 = read_file.read().split("\n")
            
            for item in name_items4:
                if item.split(".")[-1] in video_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[4]}/{name_file} {folders[0]}")
                else:
                    continue


            with open("core/s_Desktop.txt", "r") as read_file:
                name_items5 = read_file.read().split("\n")
            
            for item in name_items5:
                if item.split(".")[-1] in video_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[5]}/{name_file} {folders[0]}")
                else:
                    continue
            
            
            with open("core/s_delete_file.bash", "w") as create_file:
                create_file.write(f'''#!/bin/zsh
                rm -rf /Users/apple/Desktop/main/part_2/core''')
    
            os.system(f'bash /Users/apple/Desktop/main/part_2/core/s_delete_file.bash')
            return 'Программа завершила работу'





        elif search_file == 2:
            os.system("clear")
            os.system("mkdir core")

            with open("core/s_Movies.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[0]} > /Users/apple/Desktop/main/part_2/core/s_Movies.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Movies.bash")

            with open("core/s_Downloads.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[2]} > /Users/apple/Desktop/main/part_2/core/s_Downloads.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Downloads.bash")

            with open("core/s_Pictures.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[3]} > /Users/apple/Desktop/main/part_2/core/s_Pictures.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Pictures.bash")

            with open("core/s_Music.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[4]} > /Users/apple/Desktop/main/part_2/core/s_Music.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Music.bash")

            with open("core/s_Desktop.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[5]} > /Users/apple/Desktop/main/part_2/core/s_Desktop.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Desktop.bash")


            with open("core/s_Movies.txt", "r") as read_file:
                name_items1 = read_file.read().split("\n")
            
            for item in name_items1:
                if item.split(".")[-1] in document_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[0]}/{name_file} {folders[1]}")
                else:
                    continue


            with open("core/s_Downloads.txt", "r") as read_file:
                name_items2 = read_file.read().split("\n")
            
            for item in name_items2:
                if item.split(".")[-1] in document_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[2]}/{name_file} {folders[1]}")
                else:
                    continue


            with open("core/s_Pictures.txt", "r") as read_file:
                name_items3 = read_file.read().split("\n")
            
            for item in name_items3:
                if item.split(".")[-1] in document_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[3]}/{name_file} {folders[1]}")
                else:
                    continue


            with open("core/s_Music.txt", "r") as read_file:
                name_items4 = read_file.read().split("\n")
            
            for item in name_items4:
                if item.split(".")[-1] in document_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[4]}/{name_file} {folders[1]}")
                else:
                    continue


            with open("core/s_Desktop.txt", "r") as read_file:
                name_items5 = read_file.read().split("\n")
            
            for item in name_items5:
                if item.split(".")[-1] in document_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[5]}/{name_file} {folders[1]}")
                else:
                    continue
            
            
            with open("core/s_delete_file.bash", "w") as create_file:
                create_file.write(f'''#!/bin/zsh
                rm -rf /Users/apple/Desktop/main/part_2/core''')
    
            os.system(f'bash /Users/apple/Desktop/main/part_2/core/s_delete_file.bash')
            return 'Программа завершила работу'

        

        elif search_file == 3:
            os.system("clear")
            os.system("mkdir core")

            with open("core/s_Movies.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[0]} > /Users/apple/Desktop/main/part_2/core/s_Movies.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Movies.bash")

            with open("core/s_Downloads.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[2]} > /Users/apple/Desktop/main/part_2/core/s_Downloads.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Downloads.bash")

            with open("core/s_Documents.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[1]} > /Users/apple/Desktop/main/part_2/core/s_Documents.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Documents.bash")

            with open("core/s_Music.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[4]} > /Users/apple/Desktop/main/part_2/core/s_Music.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Music.bash")

            with open("core/s_Desktop.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[5]} > /Users/apple/Desktop/main/part_2/core/s_Desktop.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Desktop.bash")


            with open("core/s_Movies.txt", "r") as read_file:
                name_items1 = read_file.read().split("\n")
            
            for item in name_items1:
                if item.split(".")[-1] in photo_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[0]}/{name_file} {folders[3]}")
                else:
                    continue


            with open("core/s_Downloads.txt", "r") as read_file:
                name_items2 = read_file.read().split("\n")
            
            for item in name_items2:
                if item.split(".")[-1] in photo_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[2]}/{name_file} {folders[3]}")
                else:
                    continue


            with open("core/s_Documents.txt", "r") as read_file:
                name_items3 = read_file.read().split("\n")
            
            for item in name_items3:
                if item.split(".")[-1] in photo_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[1]}/{name_file} {folders[3]}")
                else:
                    continue


            with open("core/s_Music.txt", "r") as read_file:
                name_items4 = read_file.read().split("\n")
            
            for item in name_items4:
                if item.split(".")[-1] in photo_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[4]}/{name_file} {folders[3]}")
                else:
                    continue


            with open("core/s_Desktop.txt", "r") as read_file:
                name_items5 = read_file.read().split("\n")
            
            for item in name_items5:
                if item.split(".")[-1] in photo_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[5]}/{name_file} {folders[3]}")
                else:
                    continue
            
            
            with open("core/s_delete_file.bash", "w") as create_file:
                create_file.write(f'''#!/bin/zsh
                rm -rf /Users/apple/Desktop/main/part_2/core''')
    
            os.system(f'bash /Users/apple/Desktop/main/part_2/core/s_delete_file.bash')
            return 'Программа завершила работу'


        elif search_file == 4:
            os.system("clear")
            os.system("mkdir core")

            with open("core/s_Movies.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[0]} > /Users/apple/Desktop/main/part_2/core/s_Movies.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Movies.bash")

            with open("core/s_Downloads.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[2]} > /Users/apple/Desktop/main/part_2/core/s_Downloads.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Downloads.bash")

            with open("core/s_Pictures.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[3]} > /Users/apple/Desktop/main/part_2/core/s_Pictures.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Pictures.bash")

            with open("core/s_Documents.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[4]} > /Users/apple/Desktop/main/part_2/core/s_Documents.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Documents.bash")

            with open("core/s_Desktop.bash", "w") as create_file:
                create_file.write(f"""#!/bin/zsh
ls {folders[5]} > /Users/apple/Desktop/main/part_2/core/s_Desktop.txt""")
            os.system("bash /Users/apple/Desktop/main/part_2/core/s_Desktop.bash")


            with open("core/s_Movies.txt", "r") as read_file:
                name_items1 = read_file.read().split("\n")
            
            for item in name_items1:
                if item.split(".")[-1] in music_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[0]}/{name_file} {folders[4]}")
                else:
                    continue


            with open("core/s_Downloads.txt", "r") as read_file:
                name_items2 = read_file.read().split("\n")
            
            for item in name_items2:
                if item.split(".")[-1] in music_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[2]}/{name_file} {folders[4]}")
                else:
                    continue


            with open("core/s_Pictures.txt", "r") as read_file:
                name_items3 = read_file.read().split("\n")
            
            for item in name_items3:
                if item.split(".")[-1] in music_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[3]}/{name_file} {folders[4]}")
                else:
                    continue


            with open("core/s_Documents.txt", "r") as read_file:
                name_items4 = read_file.read().split("\n")
            
            for item in name_items4:
                if item.split(".")[-1] in music_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[1]}/{name_file} {folders[4]}")
                else:
                    continue


            with open("core/s_Desktop.txt", "r") as read_file:
                name_items5 = read_file.read().split("\n")
            
            for item in name_items5:
                if item.split(".")[-1] in music_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f"mv {folders[5]}/{name_file} {folders[4]}")
                else:
                    continue
            
            
            with open("core/s_delete_file.bash", "w") as create_file:
                create_file.write(f'''#!/bin/zsh
                rm -rf /Users/apple/Desktop/main/part_2/core''')
    
            os.system(f'bash /Users/apple/Desktop/main/part_2/core/s_delete_file.bash')
            return 'Программа завершила работу'

print(sort())