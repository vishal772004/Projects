filetype=input("Enter the type of the file:").strip().lower()
if filetype.endswith("jpg"):
     print("image/jpeg")
elif filetype.endswith("gif"):
     print("image/gif")
elif filetype.endswith("jpeg"):
     print("image/jpeg")
elif filetype.endswith("png"):
     print("image/png")
elif filetype.endswith("pdf"):
     print("application/pdf")
elif filetype.endswith("txt"):
     print("text/"+filetype.rstrip(".txt"))
elif filetype.endswith("zip"):
     print("application/zip")
else :
     print("application/octet-stream")



