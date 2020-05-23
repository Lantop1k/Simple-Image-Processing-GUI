#import libraries
from os.path import isfile,join
from PIL import Image as im
from PIL import ImageTk
from os import *
from tkinter import *
from imageprocessingfunctions import *
 

#window configuration
root = Tk() 
root.geometry("700x600") #Width x Height
root.minsize(300,600)
root.configure(background='#ed0fcf')

    
def CallBack():
   global bb
   global I
   
   mypath=text.get("1.0","end-1c")
   
   bb=listdir(mypath)
   y=bb

   for j in y[:]:
       if not(j.endswith(".jpg")) and not(j.endswith(".bmp")) and not(j.endswith(".png")) and not(j.endswith(".jpeg")) and not(j.endswith(".tif")):
           
           y.remove(j)

   I=[]
   for j in range(len(bb)):
       I.append(mypath+'\\'+bb[j])
   
   
   
   if len(mypath)==0 :
       messagebox.showerror(title="Error",message="please enter a path")

   elif path.exists(mypath)==False:
       messagebox.showerror(title="Error",message="path does not exist,please enter a valid path")

   else:    
   
       
       for i in range(len(bb)):
            List.insert(i+1, bb[i])
       

       List.pack()
  

def CallBack2():
    root.l=[]
    action=List.curselection()[0]
    root.l.append(action)

    List2.delete('0','end')
    List2.insert(1,bb[action])
    List2.pack()
    

def CallBack3():
        savepath=text2.get("1.0","end-1c")
    
        global action2

    
        if len(savepath)==0:
            
            imag= I[root.l[0]]


            readimage=im.open(imag)
            percent=(basewidth/float(readimage.size[0]))
            heigt=int((float(readimage.size[1])*float(percent)))
            readimage=readimage.resize((basewidth,heigt),im.ANTIALIAS)


            
            saveimage='processed_' + path.basename(imag)
            print('successful')
            IMG.save(saveimage, 'JPEG')

        elif path.exists(savepath)==False:
           messagebox.showerror(title="Error",message="path does not exist,please enter a valid path")

        else:
            
            imag= I[root.l[0]]
            
            readimage=im.open(imag)
            percent=(basewidth/float(readimage.size[0]))
            heigt=int((float(readimage.size[1])*float(percent)))
            readimage=readimage.resize((basewidth,heigt),im.ANTIALIAS)

            
            saveimage=savepath+'\processed_' + path.basename(imag)
            
            print('successful')
            IMG.save(saveimage, 'JPEG')
    
        
    
def poll(event):
    global action
    action=List.curselection()[0]
    
    basewidth=256

    
    if action>-1:
        readimage=im.open(I[action])
        percent=(basewidth/float(readimage.size[0]))
        heigt=int((float(readimage.size[1])*float(percent)))
        readimage=readimage.resize((basewidth,heigt),im.ANTIALIAS)
        root.img = ImageTk.PhotoImage(readimage)

        imageprint.configure(image=root.img)
        imageprint.place(x=420,y=30) 

def poll2(event):
    global action3
    global IMG
    action3=List3.curselection()[0]
    basewidth=256

  
    imag= I[root.l[0]]
            
    
            
    if action3==0:
       IMG=rotate(imag)
    elif action3==1:
       IMG=black_and_white(imag)
    elif action3==2:
       IMG=mirror(imag)
    elif action3==3:
       IMG=negative(imag)

    
    percent=(basewidth/float(IMG.size[0]))
    heigt=int((float(IMG.size[1])*float(percent)))
    IMG=IMG.resize((basewidth,heigt),im.ANTIALIAS)

    root.IMG=ImageTk.PhotoImage(IMG)
    
    processedimage.configure(image=root.IMG)
    processedimage.place(x=420,y=270)

   

       
l=Label(root,text="Enter Folder path")
l.place(x=0,y=0)
l.config(width=20,height=1,font=("Times New Roman",11))


text = Text(root)
text.place(x=165,y=0)
text.config(width=60,height=1,font=("Times New Roman",11))


B = Button(root, text = "Choose", command = CallBack)
B.place(x=550,y=0)
B.config(width=15,height=1,font=("Times New Roman",11))
 



List = Listbox(root)
List.place(x=250,y=30,width=120,height=100)

List.bind('<Double-1>',poll)

basewidth=128
readimage=im.open("lena256.jpg")
percent=(basewidth/float(readimage.size[0]))
heigt=int((float(readimage.size[1])*float(percent)))
readimage=readimage.resize((basewidth,heigt),im.ANTIALIAS)
root.photo = ImageTk.PhotoImage(readimage)


imageprint = Label(root,image=None)
imageprint.place(x=420,y=30)


B1 = Button(root, text = "Select", command = CallBack2)

B1.config(width=20,height=1)
B1.place(x=100,y=110) 



List2 = Listbox(root)
List2.place(x=250,y=160,width=120,height=20)



l3=Label(root,text="Select Processed Operation")
l3.place(x=0,y=400)
l3.config(width=30,height=1,font=("Times New Roman",11))


List3 = Listbox(root,selectmode=EXTENDED)
List3.place(x=250,y=330,height=80)
List3.config(font=("Times New Roman",11))
List3.insert(1,'Rotate')
List3.insert(2,'Black & White')
List3.insert(3,'Mirror')
List3.insert(4,'Negative')

List3.bind('<Double-1>',poll2)

processedimage = Label(root,image=None)
processedimage.place(x=420,y=270)





l2=Label(root,text="Please enter processed-image path")
l2.place(x=0,y=550)
l2.config(width=35,height=1,font=("Times New Roman",11))

text2 = Text(root)
text2.config(width=50,height=1,font=("Times New Roman",11))
text2.place(x=285,y=550)

B2 = Button(root, text = "Save", command = CallBack3)
B2.place(x=550,y=550)
B2.config(width=20,height=1)


root.mainloop()


