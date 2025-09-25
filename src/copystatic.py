import os, shutil
from markdown_blocks import markdown_to_html_node, extract_title

def copystatic(source, destination):
    # print(source, destination)
    source_exists = os.path.exists(source)
    if not source_exists:
        raise Exception("No Source to Copy From")
    des_exists = os.path.exists(destination)
    if des_exists:
        shutil.rmtree(destination)
    os.makedirs(destination, exist_ok=True)

    list_dir = os.listdir(source)
    if list_dir:
        for each in list_dir:
            new_source = os.path.join(source,each)
            new_dest = os.path.join(destination,each)
            is_file = os.path.isfile(new_source)
            if is_file:
                shutil.copy(new_source,new_dest)
            else:
                copystatic(new_source,new_dest)



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as content_file:
        content = content_file.read()

    with open(template_path) as template_file:
        template = template_file.read()


    html = markdown_to_html_node(content)
    title = extract_title(content)

    replaced_title = template.replace("{{ Title }}", title)

    replaced_content = replaced_title.replace("{{ Content }}", html.to_html())

    with open(dest_path, "w") as to_write:
        all_content = to_write.write(replaced_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_exists = os.path.exists(dir_path_content)
    template_exists = os.path.exists(template_path)
    if not dir_exists:
        raise Exception("Content Directory Not Available")
    
    if not template_exists:
        raise Exception("Template Not Available")
     
    os.makedirs(dest_dir_path, exist_ok=True)
    
    list_content = os.listdir(dir_path_content)
    print(list_content)

    if list_content:
        for each in list_content:
            print("thisis",)
            content_inside = os.path.join(dir_path_content,each)
            public_inside = os.path.join(dest_dir_path,each)

            if os.path.isfile(content_inside):
                html_ext = each.replace(".md",".html")
                print(html_ext)
                html_file = os.path.join(dest_dir_path,html_ext)
                generate_page(content_inside, template_path, html_file)
            else:
                generate_pages_recursive(content_inside,template_path,public_inside)

    