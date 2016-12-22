# Electrohydrodynamic-Graphing-Analysis-Tool
A graphing and analysis tool to be used for characterizing Electrohydrodynamic (EHD) flow generated 
at the tip of sharp metal pins.

## Installation
```
download python 3.5
download Miniconda

conda install
conda update conda
conda install conda-build
conda create --name ehdgraph
activate ehdgraph
conda build .
```

OR

```
download python 3.5
download Miniconda

conda install
conda update conda
conda create --name ehdgraph
activate ehdgraph
conda install --name ehdgraph python --update-dependencies
conda install --name ehdgraph numpy --update-dependencies
conda install --name ehdgraph pyqtgraph --update-dependencies
conda install --name ehdgraph pyserial --update-dependencies
```

##Executing
'''
*****After Installing the Necessary Dependencies*****
			AND
***After Downloading & Extracting the Zip folder into your specified folder***
--> Please go to the command line and type:	cd [into-the-directory-with-that-folder]
--> Then while in that directory type:		cd [Electrohydrodynamic-Graphing-Analysis-Tool]
--> Then type:					activate ehdgraph
--> Then type:					python test-program.py
--> Lastly run your apparatus
'''