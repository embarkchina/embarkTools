# EmbarkTools
Some methods for reading and saving files in notebook when use [pgcontents](https://github.com/quantopian/pgcontents) as contentsmanager 

## Install
`git clone` this repository, then `cd` this directory and use `pip install .` to install.

## set kernel and session config
```python
# set into `jupyter_notebook_config.py`

# kernel settings
from embarkTools.kernel import PGKernelManager
c.NotebookApp.kernel_manager_class = PGKernelManager

# session settings
from embarkTools.session import PGSessionManager
c.NotebookApp.session_manager_class = PGSessionManager
```