def modify_content(content: str) -> str:
    """
    Modify the file content.
    Currently converts text to uppercase.
    Customize this function for other transformations.
    """
    return content.upper()


def main():
    filename = input("Enter the filename to read: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"⚠️ File '{filename}' not found.")
        choice = input("Do you want to create a new file? (y/n): ").strip().lower()
        if choice == "y":
            default_text = "This is a new file.\nAdd your content here."
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(default_text)
                print(f"✅ Created new file '{filename}' with default text.")
                content = default_text
            except Exception as e:
                print(f"❌ Failed to create file: {e}")
                return
        else:
            print("❌ Operation cancelled.")
            return
    except PermissionError:
        print(f"❌ Error: You don't have permission to read '{filename}'.")
        return
    except Exception as e:
        print(f"❌ Unexpected error while reading file: {e}")
        return

    # Modify content
    new_content = modify_content(content)

    # Write to new file
    new_filename = "modified_" + filename
    try:
        with open(new_filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Modified content written to '{new_filename}'.")
    except Exception as e:
        print(f"❌ Failed to write to new file: {e}")


if __name__ == "__main__":
    main()
