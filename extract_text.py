


def get_cropped_images(img):
    # iterCount was chosen by trial-and-error
    '''
    this function draws a bounding box around the identified "chunk" of text.
    each pass from the loop 'enhances' the feature as there is now a box drawn around it. 
    finally, when the loop ends, the same chunks are selected from of the original image. 
    not fixed. change to return a sorted dict of images
    '''
    
    imOut = img.copy()
    imCopy = img.copy()
    croppedImgs = {}

    for I in range(0, iterCount): 
        gray = imCopy.copy()
        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
        dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        im2 = imCopy.copy()
        counter = 0
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cropped = im2[y:y + h, x:x + w]                       
            counter+=1           
            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if I==iterCount-1:
                imCropped = imOut[y:y + h, x:x+w] 
                croppedImgs[y] = imCropped
        imCopy = im2.copy() 
    
    #croppedImgs
    return imOut



def run_ocr(cropped_images_dict, show_progress=True):
    from joblib import Parallel, delayed

    if show_progress:
        txtractArr = Parallel(n_jobs=-1)(delayed(pytesseract.image_to_string)(cropped_images_dict[file], "eng") for file in tqdm(cropped_images_dict.keys()))
    else:
        txtractArr = Parallel(n_jobs=-1)(delayed(pytesseract.image_to_string)(cropped_images_dict[file], "eng") for file in cropped_images_dict.keys())
    
    txtractArr = [t for t in txtractArr if len(t.strip())>0]


    return ' '.join(txtractArr)

