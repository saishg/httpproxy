# httpproxy

This is an attempt to write a efficient HTTP proxy in Python. To get around the
GIL in Python, I decided to try using AsyncIO. I decided to use the "asyncio"
support in Python 3, which lets me use co-routinges. While I personally prefer
Python 2, this library was too good to pass. This library is available in
Python version 3.5 and later, so you may need to upgrade your Python.

I'd like this code to be modular and allow plugins to be written for the proxy,
much like nginx does.  Eventually I'd like to add multi-processing support to
this code to allow it to scale past a single core.

