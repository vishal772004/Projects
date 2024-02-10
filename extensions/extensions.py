filetype=input("Enter the type of the file:").strip()
if filetype.endswith("jpg"):
     print("application/jpg")
elif filetype.endswith("gif"):
     print("application/gif")
elif filetype.endswith("jpeg"):
     print("application/jpeg")
elif filetype.endswith("png"):
     print("application/png")
elif filetype.endswith("pdf"):
     print("application/pdf")
elif filetype.endswith("txt"):
     print("application/txt")
elif filetype.endswith("zip"):
     print("application/zip")
else :
     pritnf("application/octet-stream")



