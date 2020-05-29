# BLOCK 1

# Use os.mkdir to create your directories
# You will need a directory for cats-v-dogs, and subdirectories for training
# and testing. These in turn will need subdirectories for 'cats' and 'dogs'

try:
    os.chdir('/tmp/')
    os.mkdir('cats-v-dogs')
    os.chdir('/tmp/cats-v-dogs')
    os.mkdir('training')
    os.mkdir('testing')
    os.chdir('/tmp/cats-v-dogs/training')
    os.mkdir('cats')
    os.mkdir('dogs')
    os.chdir('/tmp/cats-v-dogs/testing')
    os.mkdir('cats')
    os.mkdir('dogs')
except OSError:
    pass
	
# BLOCK 2

# Write a python function called split_data which takes
# a SOURCE directory containing the files
# a TRAINING directory that a portion of the files will be copied to
# a TESTING directory that a portion of the files will be copie to
# a SPLIT SIZE to determine the portion
# The files should also be randomized, so that the training set is a random
# X% of the files, and the test set is the remaining files
# SO, for example, if SOURCE is PetImages/Cat, and SPLIT SIZE is .9
# Then 90% of the images in PetImages/Cat will be copied to the TRAINING dir
# and 10% of the images will be copied to the TESTING dir
# Also -- All images should be checked, and if they have a zero file length,
# they will not be copied over
#
# os.listdir(DIRECTORY) gives you a listing of the contents of that directory
# os.path.getsize(PATH) gives you the size of the file
# copyfile(source, destination) copies a file from source to destination
# random.sample(list, len(list)) shuffles a list
def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
    # YOUR CODE STARTS HERE
    all_files = os.listdir(SOURCE)
    total_files = len(all_files)
    file_range = range(0, total_files)
    train_idx = random.sample(file_range, int(np.round(total_files*SPLIT_SIZE)))
    test_idx = [i for i in file_range if i not in train_idx]
    os.chdir(SOURCE)
    for idx in train_idx:
        current_img_path = os.path.join(SOURCE, all_files[idx])
        if os.path.getsize(current_img_path) != 0:
            shutil.copy(all_files[idx], TRAINING)

    for idx in test_idx:
        current_img_path = os.path.join(SOURCE, all_files[idx])
        if os.path.getsize(current_img_path) != 0:
            shutil.copy(all_files[idx], TESTING)
    # YOUR CODE ENDS HERE


CAT_SOURCE_DIR = "/tmp/PetImages/Cat/"
TRAINING_CATS_DIR = "/tmp/cats-v-dogs/training/cats/"
TESTING_CATS_DIR = "/tmp/cats-v-dogs/testing/cats/"
DOG_SOURCE_DIR = "/tmp/PetImages/Dog/"
TRAINING_DOGS_DIR = "/tmp/cats-v-dogs/training/dogs/"
TESTING_DOGS_DIR = "/tmp/cats-v-dogs/testing/dogs/"

split_size = .9
split_data(CAT_SOURCE_DIR, TRAINING_CATS_DIR, TESTING_CATS_DIR, split_size)
split_data(DOG_SOURCE_DIR, TRAINING_DOGS_DIR, TESTING_DOGS_DIR, split_size)