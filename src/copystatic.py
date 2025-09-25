import os, shutil

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



    