import os
import re

# Set the directory path
dir_path = "./asd"
line_number = 0
# Set the pattern to match Amharic letters
amharic_pattern = r'[\u1200-\u137F]+'

# Create a new file to write the output to
output_file = open("output.txt", "w", encoding="utf-8")

# Iterate through all files in the directory
for file_name in os.listdir(dir_path):
    # Open the file
    with open(os.path.join(dir_path, file_name), "r", encoding="utf-8") as f:
        # Read the contents of the file
        contents = f.read()
    # Split the contents into sentences
    sentences = contents.split(".")
    # Create a new list to store the sentences that do not contain special characters
    filtered_sentences = []
    # Iterate through each sentence
    for sentence in sentences:
        # Check if the sentence contains any special characters that are not Amharic letters
        if not re.search(r'[^\w\s' + amharic_pattern + ']|\d', sentence):
            line_number += 1
            # If the sentence does not contain any special characters, add it to the list
            filtered_sentences.append(sentence)
    
    # Join the sentences in the list into a single string
    filtered_contents = ".".join(filtered_sentences)
    # Write the filtered contents to the output file
    print('Number of sentences that is written in pure amharic: ', line_number)
    output_file.write(filtered_contents)

# Close the output file
output_file.close()
