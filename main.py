from markdown_utility import add_images_to_md, add_images_from_folder, add_images_from_attachments

def main():
    # Ask the user for the vault directory path
    vault_directory = input("Enter the path to your Obsidian vault directory: ")

    # Ask the user which images they want to add
    option = input("Select an option:\n1. Add images from the same folder\n2. Add images from the 'attachments' folder\nEnter 1 or 2: ")

    if option == '1':
        add_images_from_folder(vault_directory)
    elif option == '2':
        add_images_from_attachments(vault_directory)
    else:
        print("Invalid option. Please select 1 or 2.")

if __name__ == "__main__":
    main()
