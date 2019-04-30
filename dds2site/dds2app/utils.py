def handle_uploaded_file(f):
    with open('uploads/uploaded.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
