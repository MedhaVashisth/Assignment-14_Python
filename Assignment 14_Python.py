#!/usr/bin/env python
# coding: utf-8
1.alpha value
3. tuple submodule provides read-only access for the tuple userdata type. It allows, for a single tuple: selective retrieval of the field contents, retrieval of information about size, iteration over all the fields, and conversion to a Lua table. Below is a list of all box. tuple functions.
5. The crop() method on Image objects takes a box tuple and returns an Image object representing the cropped image. 
6. Image.save() Saves this image under the given filename. If no format is specified, the format to use is determined from the filename extension, if possible.
7. The 'ImageDraw' module provides simple 2D graphics support for Image Object. Generally, we use this module to create new images, annotate or retouch existing images and to generate graphics on the fly for web use. The graphics commands support the drawing of shapes and annotation of text.
8. Drawing object buffers instructions for drawing shapes into images, and then it can draw these shapes into zero or more images. Syntax : with Drawing() as draw: Note: In the above syntax “as draw” is just a nomenclature and can be any string as needed. The Drawing function in Python wand take has no parameter.
# In[1]:


from PIL import Image


# In[11]:


img = Image.open('./downloads./sign.png')
rgba = img.convert("RGBA")
datas = rgba.getdata()


# In[12]:


newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 0:  # finding yellow colour
        # replacing it with a transparent value
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
  
rgba.putdata(newData)
rgba.save("transparent_image.png", "PNG")


# In[9]:


pip install pillow


# In[10]:


from PIL import Image


# In[13]:


filepath = "./downloads./sign.png"
img = Image.open(filepath)


# In[14]:


width = img.width
height = img.height


# In[15]:


print("The height of the image is: ", height)
print("The width of the image is: ", width)


# In[ ]:




