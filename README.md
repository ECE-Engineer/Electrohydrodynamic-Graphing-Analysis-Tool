# Electrohydrodynamic-Graphing-Analysis-Tool
A graphing and analysis tool to be used for characterizing Electrohydrodynamic (EHD) flow generated 
at the tip of sharp metal pins.

## Installation
```
conda install
conda update conda
conda install conda-build
conda create --name ehdgraph
activate ehdgraph
conda build .
```

OR

```
conda install
conda update conda
conda create --name ehdgraph
activate ehdgraph
conda install --name ehdgraph python --update-dependencies
conda install --name ehdgraph numpy --update-dependencies
conda install --name ehdgraph pyqtgraph --update-dependencies
conda install --name ehdgraph pyserial --update-dependencies
```