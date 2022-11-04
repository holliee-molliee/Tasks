def display_chars(path,char_num):
    with open(path,"r") as file:
        partial_data=file.read(char_num)
        print("The first 5 characters are:\n{}\n".format(partial_data))
def display_name(path):
    with open(path,"r") as file:
        line= file.readline().strip()
        print("The first line is:\n{}\n".format(line))
def display_text(path):
    with open(path,"r") as file:
        data= file.read()
        lines=data.split("\n")
        print("The full text is:")
        for line in lines:
            print(line)
def run():
    display_chars("library.txt",5)
    display_name("library.txt")
    display_text('library.txt')

if __name__ == "__main__":
    run()