import glob, random, shutil


value = input("Number of image to move:\n")
 
print('You entered {value}')

file_path_type = ["dilbert_positive_grayscale/*.png"]

for count in range(1,int(value)):
    images = glob.glob(random.choice(file_path_type))
    random_image = random.choice(images)
    shutil.move(random_image, "info/")
    print(random_image)