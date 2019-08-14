in_file = open("name.txt","r")
file_content_list= in_file.readline(0)
for line_list in in_file:
    print("Your name is",line_list)