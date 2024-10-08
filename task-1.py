import os
import shutil


def recursive_copy(src_dir, dest_dir):
    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Walk through the source directory recursively
        for root, _, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[-1][1:].lower() or "no_extension"
                target_dir = os.path.join(dest_dir, file_extension)

                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                shutil.copy2(file_path, target_dir)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    src = input("Enter the path to the source directory: ").strip()
    dest = input("Enter the path to the destination directory (default is 'dist'): ").strip() or "dist"

    if not os.path.exists(src):
        print(f"Error: Source directory '{src}' does not exist.")
    else:
        recursive_copy(src, dest)
