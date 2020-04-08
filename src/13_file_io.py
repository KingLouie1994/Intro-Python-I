"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
def print_text(txt):
    file = open(txt, "r")
    content = file.read()
    file.close()
    print(content)

print_text("foo.txt")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
def write_text(txt):
    file2 = open(txt, "w")
    file2.write("Contrary to popular belief,\nLorem Ipsum is not\nsimply random text.")
    file2.close()

write_text("bar.txt")
