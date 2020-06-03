# PythonImageEditor
Raw to jpeg converter and jpeg to png converter

# How to use?
#Make sure you have Python installed on your machine

#The libraries: Pillow, rawpy, imageio *pip install them before running the codes

At your terminal type and run:

python RawImageConvertor.py image_folder output_folder

image_folder can be any folder that you store your images (rename and remove all spaces in the folder name before running the code)

output_folder can be an existed folder or the code will create one as what you wrote 

both of the folders can be access outside the code folder:

for example, if the image folder is on desktop, then => python RawImageConvertor.py C:\Users\user\Desktop C:\Users\fengy\Desktop\output_folder

the code will search the Raw image on your desktop and save the converted files at output_folder at desktop
