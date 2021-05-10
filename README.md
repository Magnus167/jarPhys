# **jarPhys**

# What is jarPhys?

jarPhys is a PDF smart-search app, that's **designed to rapidly run quick token matching based searches on a set of images**.
jarPhys uses OCR to tag images, and search through the text in them. As of now jarPhys works amazingly with plain text, so-so with handwriting, and extremely poorly with mathematical text.

Far from complete, jarPhys is still a small but fully functional project. As of now, jarPhys allows real-time search of pre-cached PDFs.
Currently, jarPhys inputs documents as images, so the best solution is to convert PDFs to PNG images using a tool like [PDF2PNG](https://pdf2png.com/ "Allows you to upload `PDF` files and convert each page into a `PNG` file").

The real advantage jarPhys presents is avoiding searching through multiple (*or very large*) PDFs using CTRL-F (*or however the "find" feature works in your browser* :P).
Since jarPhys does token matching, you also don't have to worry about not finding an exact match, similar to the Google/Bing search tools (lol).
For the time being, the search interface is hosted on your device's command prompt and triggered through a command-line, while the results for now are presented using an HTML where the matched pages from PDFs are displayed.

**For me personally, a tool like this is helpful during exams/quizzes/tests or when trying to lookup material from a vague memory.
A great advantage is being able to search for questions without worrying about not finding "exact" matches.**
If you're worried about being penalized for using jarPhys (or similar programs), don't be! You're allowed to! Check [this section for further details](https://github.com/Magnus167/jarPhys/blob/main/README.md#am-i-allowed-to-use-jarphys-for-open-book-exams).

At some point, I'll make a complete browser-run downloadable app, but for now this is it.
The name itself is a coinage from the combination Tony Stark's **Jar**vice bot, and **Phy**sics (*the sad hell in which we are united*).
Quick links : 
 - [**Installing jarPhys-search**](https://magnus167.github.io/jarPhys/#installing-and-using-jarphys-search)
 - [**Using jarPhys-search**](https://magnus167.github.io/jarPhys/#running-the-application-hands-on-guide)
 - [**Most asked question : Am I "allowed" to use jarPhys in an exam?**](https://magnus167.github.io/jarPhys/#am-i-allowed-to-use-jarphys-for-open-book-exams)

# **Installing and using jarPhys-search**
## Requirements
**If you have Python installed and have used it a few times before, or did [5CCP211C - Intro. to Numerical Modelling](https://keats.kcl.ac.uk/enrol/index.php?id=77693), and haven't deleted the installation, you can skip reading this part.*
1. Python 3.8 (or later) installed. You can download it from [python.org](https://www.python.org/downloads/)
2. At least 3GB of available storage on disk (*~1GB for JarPhys ~2GB for Python files*).
3. An active internet connection **during installation**.


##  The Stand-Alone Installer

The simplest way to install the application quickly is to run the stand-alone installer.

1. Download the installer: [**jarPhys-simple-installer.py**](https://github.com/Magnus167/jarPhys/releases/download/r1/jarPhys-simple-installer.py).


   You can do this by clicking on the embedded link above (or [click here](https://www.github.com/Magnus167/jarPhys/releases/download/jarPhys-simple-installer/jarPhys-simple-installer.py)), or downloading the latest release from Releases section.

2. Run jarPhys-simple-installer.py; Do this by running 

   `python jarPhys-simple-installer.py` 
      
   on your terminal in the same directory. ( *Don't worry, the file's are installed within a nested folder :)* ). 
This should launch a command line installer right away. Follow the installation instructions.
3. Et voila! Enjoy :D
4. **Optional** (*recommended*) : [Buy me coffee!](https://www.buymeacoffee.com/pt420 "Only if it helped! ;p")



##  Download the source (and scanning your own documents)

Downloading the source allows you to access all the documentation and code. You can rebuild the code for yourself, and try to run the complete application on your own. 
`installer.py` is useful for downloading and extracting the complete database, and set it up correctly for developers... so use it ;P.

1. Download the entire project as a ZIP File from the green download button ([link here as well](https://codeload.github.com/Magnus167/jarPhys/zip/refs/heads/main)).
   Extract the project to the desired location and follow the install instructions in `Install_Instruction.txt`. The entire project is also mirrored on Google Drive ([link here](https://drive.google.com/drive/folders/18VgVaxoDj531Imugoc_VvvTUzCvTQdZ9?usp=sharing)).

2. Now you can search the pre-built database (*all lecture notes/slides/past papers were provided from KEATs*).
   If you have any more similar resources (*not very long books, but rather presentations, cheat-sheets, or past question papers*), I'd be more than happy to add them, or guide you on how you can add to the database on your own. 


3. If you'd like to import your own documents, and create your own database:
- Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract). You can look at their repository [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) if you want the source. The documentation is available at [tesseract-ocr/tessdoc](https://github.com/tesseract-ocr/tessdoc#binaries).  If you're running **Windows**, you can find an installer here - [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)^.   If you're running **Linux or MacOS**, try following [this guide by PyImageSearch](https://www.pyimagesearch.com/2017/07/03/installing-tesseract-for-ocr/).
- Install [OpenCV](https://opencv.org/) for Python from : by running 
   `pip install opencv-python`. 

4. The installer otherwise does other libraries required to run jarPhys. But you may want to check requirements.txt

5. If you're running windows, and **did not** install Tesseract-OCR in `C:/Program Files/Tesseract-OCR/tesseract.exe`, change [Line 14 in buildDatabase.py](https://github.com/Magnus167/jarPhys/blob/7ec38704636981e4b06f9101c236cfe63631914c/buildDatabase.py#L14) in your code to point to where you installed Tesseract-OCR. 
  
6. Et viola! Enjoy! 

And please, do give us your feedback wherever possible! It's highly appreciated.
Please support the project by [buying me coffee](https://www.buymeacoffee.com/pt420)! That's appreciated as well! :)

# Running the application (hands-on guide)
## Running the jarPhys installer

1. Navigate to the folder where you downloaded the installer. 
2. Run the command 
   
   `python jarPhys-simple-installer.py`
   
   Example : 
   
   ![image](https://user-images.githubusercontent.com/23239946/117704549-ddecfd80-b1c2-11eb-8484-e20f96d5888b.png)

3. This should launch a command line installer with fairly simple instructions you can follow :D


## Running jarPhys search

1. Navigate to the folder where you have installed jarPhys. 
2. Run the command 
   
   `python jarPhys-search.py`
   
   Example : 
   
   ![image](https://user-images.githubusercontent.com/23239946/117705423-ee51a800-b1c3-11eb-9e69-5909f0c04d69.png)


3. The results will be shown as an HTML file. There are two result sets - one based on direct matching, and the other based on frequency of matches, stored in `results.html` and `results.html` repsectively.  

   On Windows your HTML will be launched immediately on your default browser, while on MacOS/Linux (posix) you may have to launch `results.html` manually. 
   
   Example : 
   
   ![image](https://user-images.githubusercontent.com/23239946/117706729-9025c480-b1c5-11eb-9669-d21cfe4cf045.png)







# **Contributing resources to the public database**:
1. Upload your PDF file(s) to [PDF2PNG (pdf2png.com)](https://pdf2png.com/). Sadly, there's a limit of 20 files per run, but you can open it in multiple tabs :D
2. Once all the files are done converting, click on 'Download All', which gives you a ZIP (`.zip`) file.
3. Upload the ZIP file to the ['Resources_to_be_added' Google Drive folder:](https://drive.google.com/drive/folders/1VlwK030HcLgWpZKgSjWAITGdqkWpZmyY?usp=sharing) `jarPhys/pdfs/Resources_to_be_added` in the relevant subject folder. **Please DO NOT delete/modify any exisiting files here.**
4. The files will be processed and the latest version of the database will be distributed with the next release (*~5-6 times a week as of now*).

   If you have trouble converting your files to a ZIP file, simply upload your PDFs to the relevant folders, and they'll be processed later. (*This will take some more time as compared to uploading the ZIP files.*)  


# **Supporting and Contributing to the repository**
- You're welcome to create branches, forks, and issues wherever to fix/upgrade/add any relevant code/features/functionality. I will obviously consider pull-requests which improve the overall app. However, the main branch will remain solely under my control as, at the end of the day it is my repository.
- And of course:

  <a href="https://www.buymeacoffee.com/pt420"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=pt420&button_colour=BD5FFF&font_colour=ffffff&font_family=Lato&outline_colour=000000&coffee_colour=FFDD00"></a>  


# Am I **allowed** to use jarPhys for open book exams?
If you study at **King's College London**, you're not doing anything wrong. In fact, KCL encourages you to have a pre-compiled database of notes/documents you may need during your exams. As stated in the [Student Guide to Online Assessments (pg2, section "Preparing your material for an open book exam")](https://www.kcl.ac.uk/teachlearntech/assets/students-online-exams-guide.pdf), **students will not be doing anything wrong by using jarPhys**. **After all, it's simply a fancy way to search through your notes**. To be clear, using jarPhys is not "illegal" or even quasi-legal, **it's perfectly and completely "legal"**. 


**Screenshot from Student Guide to Online Assessments : KCL.AC.UK**
![image](https://user-images.githubusercontent.com/23239946/117709763-37f0c180-b1c9-11eb-922a-e954c8f58e64.png)

link : https://www.kcl.ac.uk/teachlearntech/assets/students-online-exams-guide.pdf



# **Declaration and Permissions**

All code contributed here is as is, with no guarantees of correctness or it even working on your computers. I guarantee my good intentions in sharing this as a tool, but not a finished product. Anyone interested is free to make valid contributions (suggestions) to the code, or add to the files database (as long as they are helpful contributions). You may clone and use the code from this repository however you please – although I would appreciate learning about what you found useful here.

All learning resources used in the provided database/Google Drive are learning resources provided by lecturers of KCL and other online resources mostly accessed via their teaching platform KEATs.

## **TLDR**:

You’re allowed to:

1. Commercially use the code
2. Modify
3. Distribute
4. Privately Use
5. Contribute (the best option)
   The project is **open-source** and  licensed under the **MIT License**.

I assure you that the code in this repository is free of malintent, but I can not guarantee that it works correctly.  

**Have fun, hope you enjoy using the tool.** 

