# **jarPhys**

# What is jarPhys?

jarPhys is a PDF smart-search app, that's **designed to rapidly run quick token matching based searches on a set of PDFs**.

Far from complete, jarPhys is still a small but fully functional project. As of now, jarPhys allows real-time search of pre-cached PDFs.
Currently, jarPhys inputs documents images. So the best solution is to convert PDFs to PNG images using a tool like [PDF2PNG](https://pdf2png.com/ "Allows you to upload `PDF` files and convert each page into a `PNG` file").

The real advantage jarPhys presents is avoiding searching through multiple (*or very large*) PDFs using CTRL-F (*or however the "find" feature works in your browser* :P).
Since jarPhys does token matching, you also don't have to worry about not finding an exact match, similar to the Google/Bing search tools (lol).
For the time being, the search interface is hosted on your device's command prompt and triggered through a command-line, while the results for now are presented using an HTML where the matched pages from PDFs are displayed.

**For me personally, a tool like this is helpful during exams/quizzes/tests or when trying to lookup material from a vague memory.
A great advantage is being able to search for questions without worrying about not finding "exact" matches.**

At some point, I'll make a complete browser run downloadable app, but for now this is it.
The name itself is a coinage from the combination Tony Stark's **Jar**vice bot, and the **Phy**sics (*the sad hell in which we are united*).

# **Installing and using the jarPhys-search**
## Requirements
**If you have Python installed and have used it a few times before, or did [5CCP211C - Intro. to Numerical Modelling](https://keats.kcl.ac.uk/enrol/index.php?id=77693), and haven't deleted the installation, you can skip reading this part.*
1. Python 3.8 (or later) installed. You can download it from [python.org](https://www.python.org/downloads/)
2. At least 1GB of storage on disk availabe.
3. An active internet connection **during installation**.
## The Stand-Alone Installer

The simplest way to install the application quickly is to run the stand-alone installer.

1. Download the installer : [**jarPhys-simple-installer.py**](https://github.com/Magnus167/jarPhys/releases/download/r1/jarPhys-simple-installer.py).


   You can do this by clicking on the embedded link above (or [click here](https://www.github.com/Magnus167/jarPhys/releases/download/jarPhys-simple-installer/jarPhys-simple-installer.py)), or downloading the latest release from Releases section.

2. Run jarPhys-simple-installer.py; This should launch a command line installer right away. Follow the installation instructions. (if it doesn't, try running the installer from command line)
3. Et voila! Enjoy :D

## Download the source

Downloading the source allows you to access all the documentation and code. You can rebuild the code for yourself, and try to run the complete application on your own. If you are able to download the source, and can install Tesseract OCR & OpenCV, and replace the path in the buildDatabase file, you can create your own database.
`installer.py` is useful for downloading and extracting the complete database, and set it up correctly for developers... so use it :P.

1. Download the entire project as a ZIP File from the green download button ([link here as well](https://codeload.github.com/Magnus167/jarPhys/zip/refs/heads/main)).
   Extract the project to the desired location and follow the install instructions in `Install_Instruction.txt`. The entire project is also mirrored on Google Drive ([link here](https://drive.google.com/drive/folders/18VgVaxoDj531Imugoc_VvvTUzCvTQdZ9?usp=sharing)).

2. Now you can search the pre-built database (*all lecture notes/slides/past papers were provided from KEATs*).

   If you have any more similar resources (not very long books, but rather presentations, cheat-sheets, or past question papers), I'd be more than happy to add them, or guide you on how you can add to the database on your own. Adding your own resources and custom-building your database is a bit of an icky process now. But lookout for updates!
   And please, do give me your feedback wherever possible! It's highly appreciated.

Please support the project by [buying me coffee!](https://www.buymeacoffee.com/pt420). It will be very appreciated! :)


# **Contributing resources to the public database**:
1. Upload your PDF file(s) to [PDF2PNG (pdf2png.com)](https://pdf2png.com/). Sadly, there's a limit of 20 files per run, but you can open it in multiple websites :D
2. Once all the files are done converting, click on 'Download All', which gives you a ZIP (`.zip`) file.
3. Upload the ZIP file to the ['Resources_to_be_added' Google Drive folder:](https://drive.google.com/drive/folders/1VlwK030HcLgWpZKgSjWAITGdqkWpZmyY?usp=sharing) `jarPhys/pdfs/Resources_to_be_added` in the relevant subject folder. **Please DO NOT delete/modify any exisiting files here.**
4. The files will be proccessed and the latest version of the database will be distributed with the next release (*~5-6 times a week as of now*).

   If you have trouble converting your files to a ZIP file, simply upload your PDFs to the relevant folders, and they'll be processed later. (*This will take some more time as compared to uploading the ZIP files.*)  


# **Supporting and Contributing**
- You're welcome to create branches, and issues wherever to fix/upgrade/add any relevant code/features/functionality. However, the main branch will remain solely under my control as, at the end of the day it is my repository.
- And of course :

  <a href="https://www.buymeacoffee.com/pt420"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=pt420&button_colour=BD5FFF&font_colour=ffffff&font_family=Lato&outline_colour=000000&coffee_colour=FFDD00"></a>  


# **Declaration and Permissions**

All code contributed here is as is, with no guarantees of correction. I guarantee my good intentions in sharing this as a tool, but not a finished product. Anyone interested is free to make valid contributions (suggestions) to the code, or add to the files database (as long as they are helpful contributions). You may clone and use the code from this repository however you please – although I would appreciate learning about what you found useful here.

All learning resources used in the provided database/Google Drive are learning resources provided by lecturers of KCL and other online resources mostly accessed via their teaching platform KEATs.

## **TLDR**:

You’re allow to:

1. Commercially use the code
2. Modify
3. Distribute
4. Privately Use
5. Contribute (the best option)
   The project is **open-source** and  licensed under the **MIT License**.

I assure you that the code in this repository is free of malintent, but I can not guarantee that it works correctly.  

**Have fun, hope you enjoy using the tool.** 
