filetype=input("Enter the type of the file:").strip()
if filetype.endswith("jpg"):
     print("image/jpg")
elif filetype.endswith("gif"):
     print("image/gif")
elif filetype.endswith("jpeg"):
     print("image/jpeg")
elif filetype.endswith("png"):
     print("image/png")
elif filetype.endswith("pdf"):
     print("application/pdf")
elif filetype.endswith("txt"):
     print("text",filetype)
elif filetype.endswith("zip"):
     print("application/zip")
else :
     print("application/octet-stream")



