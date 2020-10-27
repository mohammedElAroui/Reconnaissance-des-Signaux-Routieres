import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy
#load the trained model to classify sign
from keras.models import load_model
model = load_model('classification_traffic.h5')

#Dictionnaire de tous les labels des signaux routiéres
classes = { 1:'Limite Vitesse (20km/h)',
            2:'Limite Vitesse (30km/h)',      
            3:'Limite Vitesse (50km/h)',       
            4:'Limite Vitesse (60km/h)',      
            5:'Limite Vitesse (70km/h)',    
            6:'Limite Vitesse (80km/h)',      
            7:'Fin de limite Vitesse (80km/h)',     
            8:'Limite Vitesse (100km/h)',    
            9:'Limite Vitesse (120km/h)',     
           10:'Doublage Interdit',
           11:'Doublage interdit pour plus de 3.5 tons',
           12:'Intersection des routes',     
           13:'Route Prioritaire',    
           14:'Céder le passage',     
           15:'Stop',       
           16:'Interdit pour les vehicules',       
           17:'Veh > 3.5 tons sont interdits',       
           18:'interdit d entrer',       
           19:'General caution',     
           20:'vierage dangereux sur la gauche',      
           21:'Vierage dangereux sur la droite',   
           22:'Double vierage',      
           23:'Route difficile',     
           24:'Route Glissante',       
           25:'Route Rétrecit sur la droite',  
           26:'Traveaux',    
           27:'Feux de la route',      
           28:'Passage Piétons',     
           29:'Attention les enfants',     
           30:'Attention les byciclettes',       
           31:'Attention les neiges',
           32:'Attention les animaux',      
           33:'Fin de limite vitesse',      
           34:'Tournez a droite obligatoirement',     
           35:'Tournez a gauche obligatoirement',       
           36:'Devant uniquement',      
           37:'Devant ou droite',      
           38:'Devant ou gauche',      
           39:'Restez a droite',     
           40:'Restez a gauche',      
           41:'Rond point',     
           42:'Fin de non doublage',      
           43:'Fin de non doulage veh > 3.5 tons' }
                 
#initialiser la GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Reconnaissances des signaux routiéres')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict_classes([image])[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Classifier l'image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#1B4F72', foreground='black',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Importer l'image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Reconnaissance des signes routières ",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
