from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def homepage(request):
    return render(request,'labelDetection/index.html')

def upload(request):
    if request.method == 'POST':
        file = request.FILES['type'].file
        filename = str(request.FILES['type'])
        from PIL import Image
        image = Image.open(file)
        print(image)
        handle_uploaded_file(image,filename)
        print("Image Succesfully Stored")
        return render(request,'labelDetection/index.html')
 
    return HttpResponse("Failed")

def handle_uploaded_file(file,filename):
    filepath = r'E:\\Mini Projects\\insights!\\insights\\labelDetection\\static\\labelDetection\\img\\uploadedImages\\'
    import cv2
    import numpy as np
    fileName = filepath+filename.lower()
    #print(filename)
    image = np.array(file)
    cv2.imwrite(fileName,image)
    
@csrf_exempt  
def detect_labels(request):
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="E:\Image Vision-b10cc37cecba.json"
    from google.cloud import vision
    from google.cloud import storage
    from google.cloud.vision import types
    vision_client = vision.ImageAnnotatorClient()
    import io
    filepath = r'E:/Mini Projects/insights!/insights/labelDetection/static/labelDetection/img/uploadedImages/'
    filename = os.listdir(filepath)[0]
    filepath += filename
    print("Filepath is:"+filepath)
    with io.open(filepath,'rb') as i:
        image = i.read()
    
    result = vision.types.Image(content=image)
    response = vision_client.label_detection(image=result)
    labels = response.label_annotations
    print('Labels:')
    final_result = "The image may contain "
    for label in labels:
        final_result+="<b>"+label.description+"</b>, "
    
    return HttpResponse(final_result)
