from copystatic import copystatic, generate_page, generate_pages_recursive
import sys


def main():
    
    
    if len(sys.argv) > 1: 
        basepath = sys.argv[1]
    else: basepath = "/"
    print(basepath) 
    copystatic("static/","docs/")

    generate_pages_recursive("content/", "template.html", "docs/", basepath)
    
 
if __name__ == "__main__":
    main()