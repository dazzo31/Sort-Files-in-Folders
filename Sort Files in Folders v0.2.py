import os
import shutil

path = "<Your Folder name here Format: C:/Users/User_name/Downloads/>"
names = os.listdir(path)
folder_name = [
    'Misc Files', 'Developer Files', 'Disk Image Files', 'Compressed Files', 'Settings Files', 
    'System Files', 'Plugin Files', 'Web Files', 'Game Files', 'Database', 
    'Spreadsheet', '3d', 'Images', 'Text Files', 'Executables', 'Videos', 
    'Music', 'pdf', 'Presentation', 'Data Files'
]

# Create directories if they do not exist
for x in range(len(folder_name)):
    if not os.path.exists(os.path.join(path, folder_name[x])):
        os.makedirs(os.path.join(path, folder_name[x]))

# Move files based on their extensions
for files in names:
    full_file_path = os.path.join(path, files)
    if os.path.isfile(full_file_path):  # Ensure it's a file and not a directory
        if files.endswith(".png"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".jpg"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".tif"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".tiff"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".bmp"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".jpeg"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".gif"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".eps"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".raw"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".cr2"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".nef"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".orf"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".sr2"):
                shutil.move(full_file_path, os.path.join(path, 'Images', files))
        elif files.endswith(".txt"):
                shutil.move(full_file_path, os.path.join(path, 'Text Files', files))
        elif files.endswith(".fpt"):
                shutil.move(full_file_path, os.path.join(path, 'Text Files', files))
        elif files.endswith(".docx"):
                shutil.move(full_file_path, os.path.join(path, 'Text Files', files))
        elif files.endswith(".rtf"):
                shutil.move(full_file_path, os.path.join(path, 'Text Files', files))
        elif files.endswith(".log"):
                shutil.move(full_file_path, os.path.join(path, 'Text Files', files))
        elif files.endswith(".doc"):
                shutil.move(full_file_path, os.path.join(path, 'Text Files', files))
        elif files.endswith(".ppt"):
                shutil.move(full_file_path, os.path.join(path, 'Presentation', files))
        elif files.endswith(".pptx"):
                shutil.move(full_file_path, os.path.join(path, 'Presentation', files))
        elif files.endswith(".csv"):
                shutil.move(full_file_path, os.path.join(path, 'Data Files', files))
        elif files.endswith(".key"):
                shutil.move(full_file_path, os.path.join(path, 'Data Files', files))
        elif files.endswith(".keychain"):
                shutil.move(full_file_path, os.path.join(path, 'Data Files', files))
        elif files.endswith(".dat"):
                shutil.move(full_file_path, os.path.join(path, 'Data Files', files))
        elif files.endswith(".sdf"):
                shutil.move(full_file_path, os.path.join(path, 'Data Files', files))
        elif files.endswith(".tar"):
                shutil.move(full_file_path, os.path.join(path, 'Data Files', files))
        elif files.endswith(".xml"):
                shutil.move(full_file_path, os.path.join(path, 'Data Files', files))
        elif files.endswith(".vcf"):
                shutil.move(full_file_path, os.path.join(path, 'Data Files', files))
        elif files.endswith(".aif"):
                shutil.move(full_file_path, os.path.join(path, 'Music', files))
        elif files.endswith(".iff"):
                shutil.move(full_file_path, os.path.join(path, 'Music', files))
        elif files.endswith(".m3u"):
                shutil.move(full_file_path, os.path.join(path, 'Music', files))
        elif files.endswith(".m4a"):
                shutil.move(full_file_path, os.path.join(path, 'Music', files))
        elif files.endswith(".mid"):
                shutil.move(full_file_path, os.path.join(path, 'Music', files))
        elif files.endswith(".mp3"):
                shutil.move(full_file_path, os.path.join(path, 'Music', files))
        elif files.endswith(".mpa"):
                shutil.move(full_file_path, os.path.join(path, 'Music', files))
        elif files.endswith(".wav"):
                shutil.move(full_file_path, os.path.join(path, 'Music', files))
        elif files.endswith(".wma"):
                shutil.move(full_file_path, os.path.join(path, 'Music', files))
        elif files.endswith(".3g2"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".3gp"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".asf"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".avi"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".flv"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".m4v"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".mov"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".mp4"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".mpg"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".rm"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".srt"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".swf"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".mkv"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".vob"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".wmv"):
                shutil.move(full_file_path, os.path.join(path, 'Videos', files))
        elif files.endswith(".3dm"):
                shutil.move(full_file_path, os.path.join(path, '3d', files))
        elif files.endswith(".3ds"):
                shutil.move(full_file_path, os.path.join(path, '3d', files))
        elif files.endswith(".max"):
                shutil.move(full_file_path, os.path.join(path, '3d', files))
        elif files.endswith(".obj"):
                shutil.move(full_file_path, os.path.join(path, '3d', files))
        elif files.endswith(".xlr"):
                shutil.move(full_file_path, os.path.join(path, 'Spreadsheet', files))
        elif files.endswith(".xls"):
                shutil.move(full_file_path, os.path.join(path, 'Spreadsheet', files))
        elif files.endswith(".xlsx"):
                shutil.move(full_file_path, os.path.join(path, 'Spreadsheet', files))
        elif files.endswith(".db"):
                shutil.move(full_file_path, os.path.join(path, 'Database', files))
        elif files.endswith(".sql"):
                shutil.move(full_file_path, os.path.join(path, 'Database', files))
        elif files.endswith(".accdb"):
                shutil.move(full_file_path, os.path.join(path, 'Database', files))
        elif files.endswith(".dbf"):
                shutil.move(full_file_path, os.path.join(path, 'Database', files))
        elif files.endswith(".mdb"):
                shutil.move(full_file_path, os.path.join(path, 'Database', files))
        elif files.endswith(".pdb"):
                shutil.move(full_file_path, os.path.join(path, 'Database', files))
        elif files.endswith(".apk"):
                shutil.move(full_file_path, os.path.join(path, 'Executables', files))
        elif files.endswith(".app"):
                shutil.move(full_file_path, os.path.join(path, 'Executables', files))
        elif files.endswith(".bat"):
                shutil.move(full_file_path, os.path.join(path, 'Executables', files))
        elif files.endswith(".cgi"):
                shutil.move(full_file_path, os.path.join(path, 'Executables', files))
        elif files.endswith(".com"):
                shutil.move(full_file_path, os.path.join(path, 'Executables', files))
        elif files.endswith(".exe"):
                shutil.move(full_file_path, os.path.join(path, 'Executables', files))
        elif files.endswith(".gadget"):
                shutil.move(full_file_path, os.path.join(path, 'Executables', files))
        elif files.endswith(".jar"):
                shutil.move(full_file_path, os.path.join(path, 'Executables', files))
        elif files.endswith(".wsf"):
                shutil.move(full_file_path, os.path.join(path, 'Executables', files))
        elif files.endswith(".b"):
                shutil.move(full_file_path, os.path.join(path, 'Game Files', files))
        elif files.endswith(".dem"):
                shutil.move(full_file_path, os.path.join(path, 'Game Files', files))
        elif files.endswith(".gam"):
                shutil.move(full_file_path, os.path.join(path, 'Game Files', files))
        elif files.endswith(".nes"):
                shutil.move(full_file_path, os.path.join(path, 'Game Files', files))
        elif files.endswith(".rom"):
                shutil.move(full_file_path, os.path.join(path, 'Game Files', files))
        elif files.endswith(".sav"):
                shutil.move(full_file_path, os.path.join(path, 'Game Files', files))
        elif files.endswith(".pdf"):
                shutil.move(full_file_path, os.path.join(path, 'pdf', files))
        elif files.endswith(".asp"):
                shutil.move(full_file_path, os.path.join(path, 'Web Files', files))
        elif files.endswith(".aspx"):
                shutil.move(full_file_path, os.path.join(path, 'Web Files', files))
        elif files.endswith(".css"):
                shutil.move(full_file_path, os.path.join(path, 'Web Files', files))
        elif files.endswith(".htm"):
                shutil.move(full_file_path, os.path.join(path, 'Web Files', files))
        elif files.endswith(".html"):
                shutil.move(full_file_path, os.path.join(path, 'Web Files', files))
        elif files.endswith(".js"):
                shutil.move(full_file_path, os.path.join(path, 'Web Files', files))
        elif files.endswith(".jsp"):
                shutil.move(full_file_path, os.path.join(path, 'Web Files', files))
        elif files.endswith(".php"):
                shutil.move(full_file_path, os.path.join(path, 'Web Files', files))
        elif files.endswith(".rss"):
                shutil.move(full_file_path, os.path.join(path, 'Web Files', files))
        elif files.endswith(".crx"):
                shutil.move(full_file_path, os.path.join(path, 'Plugin Files', files))
        elif files.endswith(".plugin"):
                shutil.move(full_file_path, os.path.join(path, 'Plugin Files', files))
        elif files.endswith(".fnt"):
                shutil.move(full_file_path, os.path.join(path, 'Plugin Files', files))
        elif files.endswith(".fon"):
                shutil.move(full_file_path, os.path.join(path, 'Plugin Files', files))
        elif files.endswith(".otf"):
                shutil.move(full_file_path, os.path.join(path, 'Plugin Files', files))
        elif files.endswith(".ttf"):
                shutil.move(full_file_path, os.path.join(path, 'Plugin Files', files))
        elif files.endswith(".cab"):
                shutil.move(full_file_path, os.path.join(path, 'System Files', files))
        elif files.endswith(".deskthemepack"):
                shutil.move(full_file_path, os.path.join(path, 'System Files', files))
        elif files.endswith(".dll"):
                shutil.move(full_file_path, os.path.join(path, 'System Files', files))
        elif files.endswith(".ico"):
                shutil.move(full_file_path, os.path.join(path, 'System Files', files))
        elif files.endswith(".sys"):
                shutil.move(full_file_path, os.path.join(path, 'System Files', files))
        elif files.endswith(".lnk"):
                shutil.move(full_file_path, os.path.join(path, 'System Files', files))
        elif files.endswith(".dmp"):
                shutil.move(full_file_path, os.path.join(path, 'System Files', files))
        elif files.endswith(".drv"):
                shutil.move(full_file_path, os.path.join(path, 'System Files', files))
        elif files.endswith(".ini"):
                shutil.move(full_file_path, os.path.join(path, 'Settings Files', files))
        elif files.endswith(".cfg"):
                shutil.move(full_file_path, os.path.join(path, 'Settings Files', files))
        elif files.endswith(".prf"):
                shutil.move(full_file_path, os.path.join(path, 'Settings Files', files))
        elif files.endswith(".7z"):
                shutil.move(full_file_path, os.path.join(path, 'Compressed Files', files))
        elif files.endswith(".cbr"):
                shutil.move(full_file_path, os.path.join(path, 'Compressed Files', files))
        elif files.endswith(".deb"):
                shutil.move(full_file_path, os.path.join(path, 'Compressed Files', files))
        elif files.endswith(".gz"):
                shutil.move(full_file_path, os.path.join(path, 'Compressed Files', files))
        elif files.endswith(".pkg"):
                shutil.move(full_file_path, os.path.join(path, 'Compressed Files', files))
        elif files.endswith(".rar"):
                shutil.move(full_file_path, os.path.join(path, 'Compressed Files', files))
        elif files.endswith(".rpm"):
                shutil.move(full_file_path, os.path.join(path, 'Compressed Files', files))
        elif files.endswith(".tar.gz"):
                shutil.move(full_file_path, os.path.join(path, 'Compressed Files', files))
        elif files.endswith(".zip"):
                shutil.move(full_file_path, os.path.join(path, 'Compressed Files', files))
        elif files.endswith(".zipx"):
                shutil.move(full_file_path, os.path.join(path, 'Compressed Files', files))
        elif files.endswith(".bin"):
                shutil.move(full_file_path, os.path.join(path, 'Disk Image Files', files))
        elif files.endswith(".dmg"):
                shutil.move(full_file_path, os.path.join(path, 'Disk Image Files', files))
        elif files.endswith(".iso"):
                shutil.move(full_file_path, os.path.join(path, 'Disk Image Files', files))
        elif files.endswith(".mdf"):
                shutil.move(full_file_path, os.path.join(path, 'Disk Image Files', files))
        elif files.endswith(".vcd"):
                shutil.move(full_file_path, os.path.join(path, 'Disk Image Files', files))
        elif files.endswith(".c"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".class"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".cpp"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".cs"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".java"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".pl"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".py"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".sh"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".vb"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".vcxproj"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".jsp"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".servlet"):
                shutil.move(full_file_path, os.path.join(path, 'Developer Files', files))
        elif files.endswith(".ics"):
                shutil.move(full_file_path, os.path.join(path, 'Misc Files', files))
        elif files.endswith(".msi"):
                shutil.move(full_file_path, os.path.join(path, 'Misc Files', files))
        elif files.endswith(".part"):
                shutil.move(full_file_path, os.path.join(path, 'Misc Files', files))
        elif files.endswith(".torrent"):
                shutil.move(full_file_path, os.path.join(path, 'Misc Files', files))
        
print("Files organized successfully!")
