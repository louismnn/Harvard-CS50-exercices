import sys

inpt = input("File name : ")

if "." in inpt:
    document = (inpt.lower().strip()).rsplit(".", 1)
else:
    sys.exit("application/octet-stream")

if document[1] == "gif" :
    sys.exit("image/gif")
elif document[1] == "jpg" or document[1] == "jpeg":
    sys.exit("image/jpeg")
elif document[1] == "png" :
    sys.exit("image/png")
elif document[1] == "pdf" :
    sys.exit("application/pdf")
elif document[1] == "txt" :
    sys.exit("text/plain")
elif document[1] == "zip" :
    sys.exit("application/zip")
else :
    sys.exit("application/octet-stream")

