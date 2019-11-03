# Desktop organizer
Python application to organize Desktop

## Build the app for Mac
To build the app make sure to have newest Python and py2app library
It did not work for me until I updated the libraries
- I installed the newest Python version via brew `python 3.7.5`
- pip install -U py2app gave me this version `py2app==0.19`

### Build the app for development and testing
py2app builds the standalone application based on the definition in `setup.py`.

For testing and development, py2app provides an “alias mode”, which builds an app with symbolic links to the development files:

`$ python setup.py py2app -A`

This is not a standalone application, and the applications built in alias mode are not portable to other machines!

The app built with alias mode simply references the original code files, so any changes you make to the original `app.py` file are instantly available on the next app start.

The resulting development app in `dist/Desktop.app` can be opened just like any other .app with the Finder or the open command (`$ open dist/Desktop.app`). To run your application directly from the Terminal you can just run:

`$ ./dist/Desktop.app/Contents/MacOS/Desktop`

### Building for deployment
When everything is tested you can produce a build for deployment with a calling `python setup.py py2app`. Make sure that any old build and dist directories are removed:

`$ rm -rf build dist`
`$ python setup.py py2app`
This will assemble your application as `dist/Desktop.app`. Since this application is self-contained, you will have to run the py2app command again any time you change any source code, data files, options, etc.
