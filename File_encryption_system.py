from tkinter import *
from tkinter import filedialog as fd
import hashlib

root=Tk()
root.geometry("250x190")

def apply_md5():
    print("MD5 function")
    text_file=fd.askopenfilename(title="Open Text File",filetypes=(("Text Files","*.txt"),))
    read_file=open(text_file,"r")
    file1=read_file.read()
    result=hashlib.md5(file1.encode())
    hexd_file= result.hexdigest()
    md5_file=open('md5.txt','w')
    md5_file.write(hexd_file)
    md5_file.close()

    
    
def apply_sha256():
    print("SHA function")   
    text_file=fd.askopenfilename(title="Open Text File",filetypes=(("Text Files","*.txt"),))
    read_file=open(text_file,"r")
    file1=read_file.read()
    result=hashlib.sha256(file1.encode())
    hexd_file= result.hexdigest()
    sha_file=open('sha256.txt','w')
    sha_file.write(hexd_file)
    sha_file.close()
    
    
btn=Button(root, text="Apply MD5",command=apply_md5)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()