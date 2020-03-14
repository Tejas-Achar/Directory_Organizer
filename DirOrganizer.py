import os
import shutil


def walklevel(some_dir, level=1):
   some_dir = some_dir.rstrip(os.path.sep)
   assert os.path.isdir(some_dir)
   num_sep = some_dir.count(os.path.sep)
   for root, dirs, files in os.walk(some_dir):
      yield root, dirs, files
      num_sep_this = root.count(os.path.sep)
      if num_sep + level <= num_sep_this:
         del dirs[:]

DocumentsFoleder = "Doc Files"
PdfFiles = "PDF Files"
Videos = "Video Files"
images = "image Files"
threedModels = "3d model Files"
AudioFiles = "Audio Files"
Junk = "Junk Files"
ExeFiles = "Exe Files"

DirectoryMain = r'C:\Users\Tejas\downloads'

DocPath = os.path.join(DirectoryMain, DocumentsFoleder)
PdfPath = os.path.join(DirectoryMain, PdfFiles)
VideosPath = os.path.join(DirectoryMain, Videos)
ImagesPath = os.path.join(DirectoryMain, images)
ThreemodelsPath = os.path.join(DirectoryMain, threedModels)
AudioPath = os.path.join(DirectoryMain, AudioFiles)
JunkPath = os.path.join(DirectoryMain, Junk)
ExeFilesPath = os.path.join(DirectoryMain, ExeFiles)


if os.path.isdir(DocPath):
   print("Exists")
else:
 os.mkdir(DocPath)

if os.path.isdir(PdfPath):
   print("Exists")
else:
 os.mkdir(PdfPath)

if os.path.isdir(VideosPath):
   print("Exists")
else:
 os.mkdir(VideosPath)

if os.path.isdir(ImagesPath):
   print("Exists")
else:
 os.mkdir(ImagesPath)

if os.path.isdir(ThreemodelsPath):
   print("Exists")
else:
   os.mkdir(ThreemodelsPath)

if os.path.isdir(AudioPath):
   print(AudioPath,"-Exists")
else:
  os.mkdir(AudioPath)

if os.path.isdir(JunkPath):
   print("Exists")
else:
  os.mkdir(JunkPath)

if os.path.isdir(ExeFilesPath):
   print("Exists")
else:
 os.mkdir(ExeFilesPath)

print("This ***************************",DocPath)



for root, dirs, files in walklevel(DirectoryMain,level=1):
   for name in files:
      # print(os.path.join(root, name))
      print(name)
      if name.endswith(".docx") or name.endswith(".doc*") or name.endswith(".word") or name.endswith(".txt") or name.endswith(".odt") or name.endswith("ppt"):
         shutil.move(DirectoryMain+ "\\" + name, DocPath)
      elif name.endswith(".pdf"):
         shutil.move(DirectoryMain+ "\\" + name, PdfPath)
      elif name.endswith(".mp4") or name.endswith(".mkv*") or name.endswith(".avi"):
         shutil.move(DirectoryMain+ "\\" + name, VideosPath)
      elif name.endswith(".png") or name.endswith(".jp*") or name.endswith(".jpeg") or name.endswith(".gif"):
         shutil.move(DirectoryMain+ "\\" + name, ImagesPath)
      elif name.endswith(".blend") or name.endswith(".fbx") or name.endswith(".obj") or name.endswith(".mtl"):
         shutil.move(DirectoryMain+ "\\" + name, ThreemodelsPath)
      elif name.endswith(".mp3"):
         shutil.move(DirectoryMain+ "\\" + name, AudioPath)
      elif name.endswith(".exe") or name.endswith(".apk") or name.endswith(".word") or name.endswith(".txt"):
         shutil.move(DirectoryMain+ "\\" + name, ExeFilesPath)
      else:
         shutil.move(DirectoryMain+ "\\" + name, JunkPath)

   for name in dirs:
      # print(os.path.join(root, name))
      print(name)
