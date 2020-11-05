#ASCIIE ART python scripts by 
#RECOMMANDED TO USE A CLEAR and SMALL IMAGE 

#IMPORTING DEPENDENCIES
import cv2 as cv
import sys
import re

#Comment out the 14th line and uncomment the 13th line to use sys.argv 
#Or put the path name to 14th line 


# image = sys.argv[1]
image =r''
img1 = cv.imread(str(image))




#Checking for whether image exits or not and putting text to the Image.
try:
   if not None in img1:
        cv.putText( img1, "PRESS ANTHING  TO CONTINUE FOR THIS IMAGE ", (40,160), cv.FONT_HERSHEY_SIMPLEX,  0.3, (0, 40, 200),1)
   
       
except:
    print('Something went wrong!')
    exit()


#searching for  the name of the image using Regular expression.
search_string = r"[\\]"
reversed_image = image[::-1]
search = re.search(  search_string   ,  reversed_image  )
img_name = reversed_image[4:search.span()[1]-1][::-1]





# Displaying and asking to continue for current image.
cv.imshow('img',img1)
cv.waitKey(0)



#creating a function to return a charachter for hue of the pixel.
def asciie_value_return(value):
    chrs = [ ',','#', '?', '%', '.', 'S', 'o', '*', ':',  '@'
    ]
    Hue_value = int(value/25)
    return chrs[Hue_value-1]






#opning a text file to print ASCIIE ART.      
new_img = open(f'{image.replace(image[-4:],"")}.txt','w')




#creating the final function that iterate thruough every pixel of the image and print a characher in a text file according to the hue of pixel.
def main():    
    for line in range(img1.shape[0]):
        for pixel in range(img1.shape[1]):
            
            #taking average of hue of image
            pixel1 = img1[line][pixel]
            total_hue = pixel1[0]+pixel1[1]+pixel1[2]
            avg_hue = total_hue/3

            
            #assigning character according to the average hue
            char = asciie_value_return(avg_hue)

            #writing to the file 
            new_img.write(char)
        new_img.write('\n')

    print(f'ASCII art text file saved to directory {image.replace(img_name+image[-4:],"")} as {img_name}.txt ')    




if __name__ =='__main__':
    main()









        












