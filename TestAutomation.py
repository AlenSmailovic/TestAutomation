import numpy as np
from PIL import Image
from time import sleep

def CSC(pathOutputFile, pathOutputFileReverseCSC, width, height):
    textImage    = open(pathOutputFile, "r")
    textImageCSC = open(pathOutputFileReverseCSC, "w")
    
    for i in range(width):
        for j in range(height):
            # read from text file XYZ pixels
            x = textImage.readline()
            y = textImage.readline()
            z = textImage.readline()
            
            # convert back to RGB
            r =  3.063 * x - 1.393 * y - 0.476 * z
            g = -0.969 * x + 1.876 * y + 0.042 * z
            b =  0.068 * x - 0.229 * y + 1.069 * z
            
            # write in text file RGB pixels
            textImageCSC.write("%.3f\n%.3f\n%.3f\n" % (r, g, b))
    
    textImage.close()
    textImageCSC.close()

def CompareIO(pathInputFile, pathOutputFile, width, height):
    textImageInput  = open(pathInputFile, "r")
    textImageOutput = open(pathOutputFile, "r")
    
    diff = 0.0
    
    for i in range(width):
        for j in range(height):
            # read from input text file RGB pixels
            rI = textImageInput.readline()
            gI = textImageInput.readline()
            bI = textImageInput.readline()
            
            # read from output text file RGB pixels
            rO = textImageOutput.readline()
            gO = textImageOutput.readline()
            bO = textImageOutput.readline()
            
            # compute the noise
            
            # compute difference
            diff += abs(rI - rO) / 255.0
            diff += abs(gI - gO) / 255.0
            diff += abs(bI - bO) / 255.0
            
    textImageInput.close()
    textImageOutput.close()
    
    diff = diff * 100.0 / float(width * height * 3.0)
    
    print("Difference (percentage): %.3f" % diff)
    if diff < 10.0:
        print("Test PASSED!")
    else:
        print("Test FAILED!")
    

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
            textImage.write("%d\n%d\n%d\n" % (r, g, b))
            
    textImage.close()

def End2EndTest( pathImg ):
    # print the path for input image
    print("=== Test started ===")
    print(pathImg)

    # Open image from path
    iImg = Image.open( pathImg )
    
    # Show image
    #iImg.show()
    
    # Convert image to RGB matrix
    rgb_img = iImg.convert('RGB')
    
    # Save the image matrix in a numpy array
    iPxImg = np.array(rgb_img)

    # Get width and height of image
    width, height = rgb_img.size

    # Print RGB pixels in a text file
    Image2Text(iPxImg, width, height, "InputImage.txt")
    
    # Compute image in FPGA
    # - *InputImage.txt => FPGA
    # - start the FPGA module from here :)
    # - don't forget the coeficients
    # - wait until is finishing
    # - *FPGA => OutputImage.txt
    sleep(60) #sleep 60sec
    
    # Apply the algorithm back and save the results
    CSC("OutputImage.txt", "OutputImage_ReverseCSC.txt", width, height)
    
    # Compare input with output of text file -> Passed / Failed test
    CompareIO("InputImage.txt", "OutputImage_ReverseCSC.txt", width, height)
    
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
    #iImg.show()

# Start test for each type of image
End2EndTest("Images/Parrots.bmp")
#End2EndTest("Images/VGA.png")
#End2EndTest("Images/HD.png")
#End2EndTest("Images/FHD.png")
#End2EndTest("Images/QHD.png")
#End2EndTest("Images/4K.png")
