from copystatic import copystatic, generate_page, generate_pages_recursive



def main():
    print("main")
    copystatic("static/","public/")
    # generate_page("content/index.md", "template.html", "public/index.html")

    generate_pages_recursive("content/", "template.html", "public/")
    
 
if __name__ == "__main__":
    main()