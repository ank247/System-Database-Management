
class handle_uploaded_file(f):
    with open('/','wb+') as destination:
       for chunks in f.chunks():
         destination.write(chunk)

