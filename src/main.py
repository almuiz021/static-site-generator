from copystatic import copystatic, generate_page



def main():
    print("main")
    copystatic("static/","public/")
    generate_page("content/index.md", "template.html", "public/index.html")
 
if __name__ == "__main__":
    main()