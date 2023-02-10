from PIL import Image
import os

def convert_to_jpeg(dir_path):
  for filename in os.listdir(dir_path):
    if filename.endswith(".jpg"):
      filepath = os.path.join(dir_path, filename)
      img = Image.open(filepath)
      new_filepath = filepath.replace("imgs", "converted_imgs")
      new_filepath = os.path.splitext(new_filepath)[0] + '.jpeg'
      img.save(new_filepath, 'JPEG')

if __name__ == "__main__":
  convert_to_jpeg("../imgs/cloth")
  convert_to_jpeg("../imgs/person")
