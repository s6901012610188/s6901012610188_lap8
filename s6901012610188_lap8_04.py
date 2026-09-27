import os

def list_files(directory):
    """แสดงรายชื่อไฟล์ทั้งหมดในไดเรกทอรี พร้อมขนาดรวม"""
    total_size = 0
    print(f"Files in '{directory}':")
    print("-" * 50)

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            total_size += size
            print(f"{filename:<30} {size:>10} bytes")

    print("-" * 50)
    print(f"Total file size: {total_size} bytes ({total_size / 1024:.2f} KB)\n")
    return total_size


def list_image_files(directory):
    """แสดงเฉพาะไฟล์รูปภาพ (.jpg, .gif, .png) พร้อมขนาดรวม"""
    image_extensions = ('.jpg', '.jpeg', '.gif', '.png')
    total_image_size = 0

    print(f"Image files in '{directory}':")
    print("-" * 50)

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(image_extensions):
            size = os.path.getsize(filepath)
            total_image_size += size
            print(f"{filename:<30} {size:>10} bytes")

    print("-" * 50)
    print(f"Total image file size: {total_image_size} bytes ({total_image_size / 1024:.2f} KB)\n")
    return total_image_size


if __name__ == "__main__":
    directory = input("Enter directory path: ").strip()

    if not os.path.isdir(directory):
        print("Invalid directory path.")
    else:
        # แสดงไฟล์ทั้งหมด + ขนาดรวม
        list_files(directory)

        # แสดงเฉพาะไฟล์รูปภาพ + ขนาดรวม
        list_image_files(directory)
