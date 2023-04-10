while True:
    try:
        pass
        file_path = input()
        if file_path.find('.mp4') != -1:
            print(file_path)
    except EOFError:
        break
