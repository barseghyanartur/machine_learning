import os

from PIL import Image
import numpy as np

#Directory containing images you wish to convert
input_dir = "/Users/Josh/Documents/celeb_machine_learning_matching/data/output_images/"


directories = os.listdir(input_dir)

index = 0
index2 = 0

#Iterating through each folder in input directory
for folder in directories:
	#Ignoring .DS_Store dir
	if folder == '.DS_Store':
		pass

	else:
		print folder

		folder2 = os.listdir(input_dir + '/' + folder)
		index += 1

		#Iterating through each image in folder
		for image in folder2:
			index2 += 1

			im = Image.open(input_dir+"/"+folder+"/"+image) #Opening image
			im = (np.array(im)) #Converting to numpy array

			try:
				r = im[:,:,0] #Slicing to get R data
				g = im[:,:,1] #Slicing to get G data
				b = im[:,:,2] #Slicing to get B data

				if index2 != 1:
					new_array = np.array([[r] + [g] + [b]], np.uint8) #Creating array with shape (3, 100, 100)
					out = np.append(out, new_array, 0) #Adding new image to array shape of (x, 3, 100, 100) where x is image number

				elif index2 == 1:
					out = np.array([[r] + [g] + [b]], np.uint8) #Creating array with shape (3, 100, 100)

				if index == 1 and index2 == 1:
					index_array = np.array([[index]])

				else:
					new_index_array = np.array([[index]], np.int8)
					index_array = np.append(index_array, new_index_array, 0)

			except Exception as e:
				print e
				print image

print index
print index2
np.save('X.npy', out) #Saving image arrays
np.save('Y.npy', index_array) #Saving data labels into seperate array
