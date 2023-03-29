# Clean-amharic-sentenses
This Python code reads the contents of all files in a specified directory, filters out sentences that contain special characters other than Amharic letters and digits, and writes the filtered contents to a new file called "output.txt". It also prints the total number of sentences that are written in pure Amharic.

The code uses the os module to get the list of files in the directory, and the re module to match Amharic letters and special characters. It sets a regular expression pattern to match Amharic letters and checks each sentence in the contents of the file against this pattern using re.search(). If a sentence contains any special characters that are not Amharic letters or digits, it is not added to the filtered list of sentences.

The filtered sentences are then joined into a single string and written to a new file called "output.txt" using the open() function with write mode ("w") and UTF-8 encoding. The code also prints the total number of sentences that are written in pure Amharic, which is incremented each time a sentence is added to the filtered list.

Overall, this code can be used to extract pure Amharic text from a set of files and write it to a new file. However, it assumes that the files are encoded in UTF-8 and that sentences are separated by periods. Additionally, it does not perform any linguistic analysis to ensure that the filtered sentences are grammatically correct or meaningful.
