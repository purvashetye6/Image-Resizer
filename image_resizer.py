# from PIL import Image
# import os

# def resize(image, new_width):
#     width, height = image.size
#     ratio = height/width
#     new_height = int(ratio * new_width)
#     resized_image = image.resize((new_width,new_height))
#     return resized_image

# files = os.listdir()
# extensions = ['jpg', 'jpeg', 'png']
# for file in files:
#     ext = file.split(".")[-1]
#     if ext in extensions:
#         image = Image.open(file)
#         image_resized = resize(image, 400)
#         filepath = f"resized_images/{file}.jpg"
#         image_resized.save(filepath)


from PIL import Image
import os

def resize(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Get user input for directory and new width
input_directory = input("Enter the directory containing images: ")
new_width = int(input("Enter the new width for the images: "))

# Create output directory if it doesn't exist
output_directory = os.path.join(input_directory, "resized_images")
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Get list of files in the directory
files = os.listdir(input_directory)
extensions = ['jpg', 'jpeg', 'png']

for file in files:
    ext = file.split(".")[-1].lower()
    if ext in extensions:
        image_path = os.path.join(input_directory, file)
        image = Image.open(image_path)
        image_resized = resize(image, new_width)
        output_path = os.path.join(output_directory, f"{os.path.splitext(file)[0]}.jpg")
        image_resized.save(output_path)

print(f"Images have been resized and saved to {output_directory}")


