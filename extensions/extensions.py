filetype=input("Enter the type of the file:").strip()
match filetype:
    case filetype.endswith("jpg"):
          print("application/jpg")
    case filetype.enswith("gif"):
          print("application/gif")

