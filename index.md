<h1 id="-jarphys-"><strong>jarPhys</strong></h1>
<div style="text-align: right"> <a href="https://www.buymeacoffee.com/pt420"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&amp;emoji=&amp;slug=pt420&amp;button_colour=BD5FFF&amp;font_colour=ffffff&amp;font_family=Poppins&amp;outline_colour=000000&amp;coffee_colour=FFDD00"></a> </div>

<h1 id="what-is-jarphys-">What is jarPhys?</h1>
<p>jarPhys is a PDF smart-search app, that&#39;s <strong>designed to rapidly run quick token matching based searches on a set of images</strong>. jarPhys uses OCR to tag images, and search through the text in them. As of now jarPhys works amazingly with plain text, so-so with handwriting, and extremely poorly with mathematical text.</p>
<p>Far from complete, jarPhys is still a small but fully functional project. As of now, jarPhys allows real-time search of pre-cached PDFs. Currently, jarPhys inputs documents as images, so the best solution is to convert PDFs to PNG images using a tool like <a href="https://pdf2png.com/" title="Allows you to upload `PDF` files and convert each page into a `PNG` file">PDF2PNG</a>.</p>
<p>The real advantage jarPhys presents is avoiding searching through multiple (<em>or very large</em>) PDFs using CTRL-F (<em>or however the &quot;find&quot; feature works in your browser</em> :P). Since jarPhys does token matching, you also don&#39;t have to worry about not finding an exact match, similar to the Google/Bing search tools (lol). For the time being, the search interface is hosted on your device&#39;s command prompt and triggered through a command-line, while the results for now are presented using an HTML where the matched pages from PDFs are displayed.</p>
<p><strong>For me personally, a tool like this is helpful during exams/quizzes/tests or when trying to lookup material from a vague memory. A great advantage is being able to search for questions without worrying about not finding &quot;exact&quot; matches.</strong> If you&#39;re worried about being penalized for using jarPhys (or similar programs), don&#39;t be! You&#39;re allowed to! Check <a href="https://github.com/Magnus167/jarPhys/blob/main/README.md#am-i-allowed-to-use-jarphys-for-open-book-exams">this section for further details</a>.</p>
<p>At some point, I&#39;ll make a complete browser-run downloadable app, but for now this is it. The name itself is a coinage from the combination Tony Stark&#39;s <strong>Jar</strong>vice bot, and <strong>Phy</strong>sics (<em>the sad hell in which we are united</em>). Quick links :</p>
<ul>
<li><a href="https://magnus167.github.io/jarPhys/#installing-and-using-jarphys-search"><strong>Installing jarPhys-search</strong></a></li>
<li><a href="https://magnus167.github.io/jarPhys/#running-the-application-hands-on-guide"><strong>Using jarPhys-search</strong></a></li>
<li><a href="https://magnus167.github.io/jarPhys/#am-i-allowed-to-use-jarphys-for-open-book-exams"><strong>Most asked question : Am I &quot;allowed&quot; to use jarPhys in an exam?</strong></a></li>
</ul>
<h1 id="-installing-and-using-jarphys-search-"><strong>Installing and using jarPhys-search</strong></h1>
<h2 id="requirements">Requirements</h2>
<p><em>*If you have Python installed and have used it a few times before, or did <a href="https://keats.kcl.ac.uk/enrol/index.php?id=77693">5CCP211C - Intro. to Numerical Modelling</a>, and haven&#39;t deleted the installation, you can skip reading this part.</em></p>
<ol>
<li>Python 3.8 (or later) installed. You can download it from <a href="https://www.python.org/downloads/">python.org</a></li>
<li>At least 3GB of available storage on disk (<em>~1GB for JarPhys ~2GB for Python files</em>).</li>
<li>An active internet connection <strong>during installation</strong>.</li>
</ol>
<h2 id="the-stand-alone-installer">The Stand-Alone Installer</h2>
<p>The simplest way to install the application quickly is to run the stand-alone installer.</p>
<ol>
<li><p>Download the installer: <a href="https://github.com/Magnus167/jarPhys/releases/download/r1/jarPhys-simple-installer.py"><strong>jarPhys-simple-installer.py</strong></a>.</p>
<p>You can do this by clicking on the embedded link above (or <a href="https://www.github.com/Magnus167/jarPhys/releases/download/jarPhys-simple-installer/jarPhys-simple-installer.py">click here</a>), or downloading the latest release from Releases section.</p>
</li>
<li><p>Run jarPhys-simple-installer.py; Do this by running</p>
<p><code>python jarPhys-simple-installer.py</code></p>
<p>on your terminal in the same directory. ( <em>Don&#39;t worry, the file&#39;s are installed within a nested folder :)</em> ). This should launch a command line installer right away. Follow the installation instructions.</p>
</li>
<li><p>Et voila! Enjoy :D</p>
</li>
<li><strong>Optional</strong> (<em>recommended</em>) : <a href="https://www.buymeacoffee.com/pt420" title="Only if it helped! ;p">Buy me coffee!</a></li>
</ol>
<h2 id="download-the-source-and-scanning-your-own-documents-">Download the source (and scanning your own documents)</h2>
<p>Downloading the source allows you to access all the documentation and code. You can rebuild the code for yourself, and try to run the complete application on your own. <code>installer.py</code> is useful for downloading and extracting the complete database, and set it up correctly for developers... so use it ;P.</p>
<ol>
<li><p>Download the entire project as a ZIP File from the green download button (<a href="https://codeload.github.com/Magnus167/jarPhys/zip/refs/heads/main">link here as well</a>). Extract the project to the desired location and follow the install instructions in <code>Install_Instruction.txt</code>. The entire project is also mirrored on Google Drive (<a href="https://drive.google.com/drive/folders/18VgVaxoDj531Imugoc_VvvTUzCvTQdZ9?usp=sharing">link here</a>).</p>
</li>
<li><p>Now you can search the pre-built database (<em>all lecture notes/slides/past papers were provided from KEATs</em>). If you have any more similar resources (<em>not very long books, but rather presentations, cheat-sheets, or past question papers</em>), I&#39;d be more than happy to add them, or guide you on how you can add to the database on your own.</p>
</li>
<li><p>If you&#39;d like to import your own documents, and create your own database:</p>
<ul>
<li>Install <a href="https://github.com/tesseract-ocr/tesseract">Tesseract OCR</a>. You can look at their repository <a href="https://github.com/tesseract-ocr/tesseract">tesseract-ocr/tesseract</a> if you want the source. The documentation is available at <a href="https://github.com/tesseract-ocr/tessdoc#binaries">tesseract-ocr/tessdoc</a>. If you&#39;re running <strong>Windows</strong>, you can find an installer here - <a href="https://github.com/UB-Mannheim/tesseract/wiki">UB-Mannheim/tesseract</a>^. If you&#39;re running <strong>Linux or MacOS</strong>, try following <a href="https://www.pyimagesearch.com/2017/07/03/installing-tesseract-for-ocr/">this guide by PyImageSearch</a>.</li>
<li>Install <a href="https://opencv.org/">OpenCV</a> for Python from : by running <code>pip install opencv-python</code>.</li>
</ul>
</li>
<li><p>The installer otherwise does other libraries required to run jarPhys. But you may want to check requirements.txt</p>
</li>
<li><p>If you&#39;re running windows, and <strong>did not</strong> install Tesseract-OCR in <code>C:/Program Files/Tesseract-OCR/tesseract.exe</code>, change <a href="https://github.com/Magnus167/jarPhys/blob/7ec38704636981e4b06f9101c236cfe63631914c/buildDatabase.py#L14">Line 14 in buildDatabase.py</a> in your code to point to where you installed Tesseract-OCR.</p>
</li>
<li><p>Et viola! Enjoy!</p>
</li>
</ol>
<p>And please, do give us your feedback wherever possible! It&#39;s highly appreciated. Please support the project by <a href="https://www.buymeacoffee.com/pt420">buying me coffee</a>! That&#39;s appreciated as well! :)</p>
<h1 id="running-the-application-hands-on-guide-">Running the application (hands-on guide)</h1>
<h2 id="running-the-jarphys-installer">Running the jarPhys installer</h2>
<ol>
<li>Navigate to the folder where you downloaded the installer.</li>
<li><p>Run the command</p>
<p><code>python jarPhys-simple-installer.py</code></p>
<p>Example :</p>
<p><img src="https://user-images.githubusercontent.com/23239946/117704549-ddecfd80-b1c2-11eb-8484-e20f96d5888b.png" alt="image"></p>
</li>
<li><p>This should launch a command line installer with fairly simple instructions you can follow :D</p>
</li>
</ol>
<h2 id="running-jarphys-search">Running jarPhys search</h2>
<ol>
<li>Navigate to the folder where you have installed jarPhys.</li>
<li><p>Run the command</p>
<p><code>python jarPhys-search.py</code></p>
<p>Example :</p>
<p><img src="https://user-images.githubusercontent.com/23239946/117705423-ee51a800-b1c3-11eb-9e69-5909f0c04d69.png" alt="image"></p>
</li>
<li><p>The results will be shown as an HTML file. There are two result sets - one based on direct matching, and the other based on frequency of matches, stored in <code>results.html</code> and <code>results.html</code> repsectively.</p>
<p>On Windows your HTML will be launched immediately on your default browser, while on MacOS/Linux (posix) you may have to launch <code>results.html</code> manually.</p>
<p>Example :</p>
<p><img src="https://user-images.githubusercontent.com/23239946/117706729-9025c480-b1c5-11eb-9669-d21cfe4cf045.png" alt="image"></p>
</li>
</ol>
<h1 id="-contributing-resources-to-the-public-database-"><strong>Contributing resources to the public database</strong>:</h1>
<ol>
<li>Upload your PDF file(s) to <a href="https://pdf2png.com/">PDF2PNG (pdf2png.com)</a>. Sadly, there&#39;s a limit of 20 files per run, but you can open it in multiple tabs :D</li>
<li>Once all the files are done converting, click on &#39;Download All&#39;, which gives you a ZIP (<code>.zip</code>) file.</li>
<li>Upload the ZIP file to the <a href="https://drive.google.com/drive/folders/1VlwK030HcLgWpZKgSjWAITGdqkWpZmyY?usp=sharing">&#39;Resources_to_be_added&#39; Google Drive folder:</a> <code>jarPhys/pdfs/Resources_to_be_added</code> in the relevant subject folder. <strong>Please DO NOT delete/modify any exisiting files here.</strong></li>
<li><p>The files will be processed and the latest version of the database will be distributed with the next release (<em>~5-6 times a week as of now</em>).</p>
<p>If you have trouble converting your files to a ZIP file, simply upload your PDFs to the relevant folders, and they&#39;ll be processed later. (<em>This will take some more time as compared to uploading the ZIP files.</em>)</p>
</li>
</ol>
<h1 id="reporting-and-getting-help-with-issues">Reporting and getting help with issues</h1>
<p>You can use either of the following methods to report and get help with an issue. In both cases, we will get back to you as soon as possible:</p>
<ul>
<li>Any issues can be reported using the <a href="https://docs.google.com/forms/d/e/1FAIpQLSevOXeW1HRqBSGvk_3cVTdAd4moyb6PY86kbKT4Yd8snj707A/"><strong>Issue/Feedback Form</strong></a>.</li>
<li>If you use Github, the issue can be submitted directly to the <a href="https://github.com/Magnus167/jarPhys/issues"><strong>repository&#39;s issues tab</strong></a></li>
</ul>
<h1 id="-supporting-and-contributing-to-the-repository-"><strong>Supporting and Contributing to the repository</strong></h1>
<ul>
<li>You&#39;re welcome to create branches, forks, and issues wherever to fix/upgrade/add any relevant code/features/functionality. I will obviously consider pull-requests which improve the overall app. However, the main branch will remain solely under my control as, at the end of the day it is my repository.</li>
<li><p>And of course:</p>
<p><a href="https://www.buymeacoffee.com/pt420"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&amp;emoji=&amp;slug=pt420&amp;button_colour=BD5FFF&amp;font_colour=ffffff&amp;font_family=Lato&amp;outline_colour=000000&amp;coffee_colour=FFDD00" alt=""></a></p>
</li>
</ul>
<h1 id="am-i-allowed-to-use-jarphys-for-open-book-exams-">Am I <strong>allowed</strong> to use jarPhys for open book exams?</h1>
<p>If you study at <strong>King&#39;s College London</strong>, you&#39;re not doing anything wrong. In fact, KCL encourages you to have a pre-compiled database of notes/documents you may need during your exams. As stated in the <a href="https://www.kcl.ac.uk/teachlearntech/assets/students-online-exams-guide.pdf">Student Guide to Online Assessments (pg2, section &quot;Preparing your material for an open book exam&quot;)</a>, <strong>students will not be doing anything wrong by using jarPhys</strong>. <strong>After all, it&#39;s simply a fancy way to search through your notes</strong>. To be clear, using jarPhys is not &quot;illegal&quot; or even quasi-legal, <strong>it&#39;s perfectly and completely &quot;legal&quot;</strong>.</p>
<p><strong>Screenshot from Student Guide to Online Assessments : KCL.AC.UK</strong> <img src="https://user-images.githubusercontent.com/23239946/117709763-37f0c180-b1c9-11eb-922a-e954c8f58e64.png" alt="image"></p>
<p>link : <a href="https://www.kcl.ac.uk/teachlearntech/assets/students-online-exams-guide.pdf">https://www.kcl.ac.uk/teachlearntech/assets/students-online-exams-guide.pdf</a></p>
<h1 id="-declaration-and-permissions-"><strong>Declaration and Permissions</strong></h1>
<p>All code contributed here is as is, with no guarantees of correctness or it even working on your computers. I guarantee my good intentions in sharing this as a tool, but not a finished product. Anyone interested is free to make valid contributions (suggestions) to the code, or add to the files database (as long as they are helpful contributions). You may clone and use the code from this repository however you please – although I would appreciate learning about what you found useful here.</p>
<p>All learning resources used in the provided database/Google Drive are learning resources provided by lecturers of KCL and other online resources mostly accessed via their teaching platform KEATs.</p>
<h2 id="-tldr-"><strong>TLDR</strong>:</h2>
<p>You’re allowed to:</p>
<ol>
<li>Commercially use the code</li>
<li>Modify</li>
<li>Distribute</li>
<li>Privately Use</li>
<li>Contribute (the best option) The project is <strong>open-source</strong> and licensed under the <strong>MIT License</strong>.</li>
</ol>
<p>I assure you that the code in this repository is free of malintent, but I can not guarantee that it works correctly.</p>
<p><strong>Have fun, hope you enjoy using the tool.</strong></p>
