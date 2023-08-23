import os


def add_images_to_md(md_file, image_paths, vault_directory):
    # Read the existing content of the MD file
    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # Append the Markdown image syntax for each image in the list
    for image_path in image_paths:
        relative_path = os.path.relpath(image_path, vault_directory)
        md_content += f'\n![[{relative_path}]]\n'

    # Write the updated content back to the MD file
    with open(md_file, 'w', encoding='utf-8') as file:
        file.write(md_content)

def add_images_from_folder(vault_directory):
    # Iterate through the directories within the vault directory
    for root, _, _ in os.walk(vault_directory):
        for file in os.listdir(root):
            if file.endswith('.md'):
                md_file_path = os.path.join(root, file)
                image_files = [os.path.join(root, f) for f in os.listdir(root) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg'))]
                add_images_to_md(md_file_path, image_files, vault_directory)

def add_images_from_attachments(vault_directory):
    attachments_folder = os.path.join(vault_directory, 'attachments')

    if not os.path.exists(attachments_folder):
        print("Attachments folder not found.")
        return

    # Iterate through the directories within the attachments folder
    for root, _, _ in os.walk(attachments_folder):
        for file in os.listdir(root):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):
                # Extract the filename prefix (Markdown file name)
                filename_prefix = file.split('_', 1)[0]

                # Search for the corresponding Markdown file
                for root2, _, files2 in os.walk(vault_directory):
                    for file2 in files2:
                        if file2.endswith('.md') and file2.startswith(filename_prefix):
                            md_file_path = os.path.join(root2, file2)
                            image_path = os.path.join(root, file)
                            add_images_to_md(md_file_path, [image_path], vault_directory)
