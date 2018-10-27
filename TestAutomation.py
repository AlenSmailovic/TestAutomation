import numpy as np
from PIL import Image

def CSC(pathOutputFile):
	
	
def CompareIO(pathInputFile, pathOutputFile):
	
	
def Text2Image(pathFile, width, height, pxImg):
	textImage = open( pathFile, "r" )
	
    for x in range(width):
        for y in range(height):
			# read from text file RGB pixels
			r = textImage.readline()
			g = textImage.readline()
			b = textImage.readline()
			
            # get RGB pixels value from image
            pxImg[y][x] = (r, g, b)
	
	textImage.close()

def Image2Text( pxImg, width, height, pathFile ):
	textImage = open( pathFile, "w" )
	
    for x in range(width):
        for y in range(height):

            # get RGB pixels value from image
            (r, g, b) = pxImg[y][x]
			
			# write in text file RGB pixels
			textImage.write("%d\n%d\n%d\n" % r, g, b)
	
	textImage.close()

def End2EndTest( pathImg ):
    # print the path for input image
	print("=== Test started ===")
    print pathImg

    # Open image from path
    iImg = Image.open( pathImg )
	
	# Show image
	iImg.show()
	
	# Convert image to RGB matrix
    rgb_img = iImg.convert('RGB')
	
    # Save the image matrix in a numpy array
    iPxImg = np.array(rgb_img)

    # Get width and height of image
    width, height = rgb_img.size

    # Print RGB pixels in a text file
    Image2Text(iPxImg, width, height, "InputImage.txt")
	
	# Compute image in FPGA
	# - start the FPGA module from here :)
	# - don't forget the coeficients
	# - wait until is finishing
	
	# Apply the algorithm back
	CSC("OutputImage.txt")
	
	# Compare input with output of text file -> Passed / Failed test
	CompareIO("InputImage.txt", "OutputImage.txt")
	
	# Create RGB array from text file
	oPxImg = np.zeros((height, width, 3), dtype=np.uint8)
	
	Text2Image("OutputImage.txt", width, height, oPxImg)
	
	# Load the image from numpy array
    rgb_img = Image.fromarray(oPxImg, mode = "RGB")
	
    # Save the image at corresponding path
    rgb_img.save( pathImg.replace(".png", "Tested.png") )
	
	# Open image from path
	oImg = Image.open( pathImg )
	
	# Show image
	iImg.show()

# Start test for each type of image
End2EndTest("Images/VGA.png")
#End2EndTest("Images/HD.png")
#End2EndTest("Images/FHD.png")
#End2EndTest("Images/QHD.png")
#End2EndTest("Images/4K.png")