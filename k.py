import chardet

# Replace 'your_file.json' with the path to your JSON file
file_path = "your_file.json"

# Detect the encoding of the file
with open(file_path, "rb") as file:
    detector = chardet.universaldetector.UniversalDetector()
    for line in file.readlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    encoding = detector.result["encoding"]

print(f"The encoding of {file_path} is: {encoding}")
