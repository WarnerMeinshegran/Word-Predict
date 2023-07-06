# Word predict
A game where you guess a word that is choosen randomly.  
![image](https://github.com/blabla-labALT/Word-Predict/assets/92992442/43f123df-1727-4a77-be23-af61ec5a4a9d)  
## Installing
### Installing from already compiled binaries
go to releases and click on assests then choose the binary type for you os.  
windows > exe
linux > appimage
### compiling from source code
NOTE: this project uses python 3.10.6  
How to:  
1. download the source code
2. open the terminal or command prompt and type:  
```pip install pysimplegui```
```pip install playsound```
and if you are using linux type:  
```sudo apt-get install python3-tk```  
to make sure you also have tkinter  
4. extract the zip file and delete everything except the .py file and the .ico file  
5. Open the terminal and make sure the directory is the same one which has the files you didnt delete  
6. type ```pip install pyinstaller```  
7. now you are ready to compile, type ```pyinstaller -F -w -i word.ico WordPredict.py``` or for linux 
```pyinstaller -F -w WordPredict.py```
8. when it finished the application should be in the dist folder
## Credits
Developer - blabla_lab
GUI Library - PySimpleGUI
Sounds      - Nathan Gibson
