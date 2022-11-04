def search(path):
    print("Searching...")
    sections=""
    books= "Books:\n"
    with open(path,"r") as file:
        for line in file:
            if line.startswith("Section"):
                sections+=line
            else:
                books+=line
    print("Done!")
    output=sections+"\n\n"+books
    return output

def save(path, string):
    print("Saving...")
    with open(path, "w") as file:
        file.write(string)
    print("Done!")

def run():
    data = search("books.txt")
    save("section-books.txt", data)

if __name__=="__main__":
    run()
