import tkinter as tk 

HEIGHT = 600 
WIDTH = 500 

root = tk.Tk() 
root.title('Video Format convertor')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack() 

frame1 = tk.Frame(root, bg='#035afc', bd=5) 
frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

file_label = tk.Label(frame1, text="File Name")
file_label.place(relx=0, rely=0, relwidth=0.25, relheight=0.45)

file_name = tk.Entry(frame1)
file_name.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.45)

fmt_label = tk.Label(frame1, text="Target Format")
fmt_label.place(relx=0, rely=0.55, relwidth=0.25, relheight=0.45)

tar_fmt = tk.Entry(frame1) 
tar_fmt.place(relx=0.3, rely=0.55, relwidth=0.7, relheight=0.45)

frame2 = tk.Frame(root, bd=5)
frame2.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')

conv_btn = tk.Button(frame2, text="CONVERT")
conv_btn.place(relx=0.5, rely=0, relwidth=0.4, relheight=1, anchor='n')

root.mainloop() 
