def get_category(file):
    ext = file.lower().split('.')[-1]

    if ext in ['jpg','jpeg','png','gif']:
        return 'Images'
    elif ext in ['pdf','doc','docx','txt','ppt','pptx']:
        return 'Documents'
    elif ext in ['py','js','java','cpp','c','html','css']:
        return 'Code'
    elif ext in ['zip','rar','7z','tar']:
        return 'Archives'
    else:
        return 'Others'
