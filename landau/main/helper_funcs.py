def save_file(f):
    with open('file.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
