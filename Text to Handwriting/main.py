import pywhatkit as convertor

user_text = """Python is a general purpose,dynamically typed high-level language. Python It's design philosophy emphasizes code readability with its use of significant indentation."""

# Format of this method (text,file_name,rgb)
convertor.text_to_handwriting(user_text,"Demo.png",[0,0,138])

# When operation is done then it will print completed.
print(" Completed ")