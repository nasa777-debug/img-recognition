from PIL import Image, ImageChops
def images_are_equal(img_path1, img_path2):
    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)
    if img1.size != img2.size:
        return False
    diff = ImageChops.difference(img1, img2)
    return diff.getbbox() is None
image1 = "image1.jpg"
image2 = "image1.jpg"
result = images_are_equal(image1, image2)
print("Images are identical." if result else "Images are different.")
