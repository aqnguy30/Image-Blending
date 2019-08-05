import numpy as np

class operation:

    def blend(self, image, logo, x=None, y=None, alpha=None):
        '''
        Use logo and blend it on the image at location (x, y)
        image: the original image
        logo: the logo to blend on to the image
        x: topleft coordinate x
        y: topleft coordinate y
        alpha: blend ratio to the logo

        returns the image blended with logo at loction (x, y)'''

        imageM = np.matrix(image)
        logoM = np.matrix(logo)
        final = np.matrix(image)

        imageX, imageY = image.shape
        logoX, logoY = logo.shape

        for i in range(logoX):
            if i + x >= imageX:
                break
            for j in range(logoY):
                if j + y >= imageY:
                    break
                else:
                    final[x + i, y + j] = alpha * imageM[x + i, y + j] + (1 - alpha) * logoM[i, j]

        return final


'''        i2 = 0
        j2 = 0

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if i >= x and j >= y and i2 < logo.shape[0] and j2 < logo.shape[1]:
                    final[i,j] = alpha * imageM[i,j] + (1-alpha) * logoM[i2, j2]
            if i >= x:
                i2 = i2 + 1
                j2 = j2 + 1

        return final
'''

        #code
        ### add your code here
        ### Please do not change the structure

        #return image #Currently the original image is returned, please replace this with the blended image

