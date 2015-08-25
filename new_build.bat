ECHO OFF
ECHO Building new Tank-Game Exe.
ECHO Deleting old build
del build
ECHO Building Executable
python build.py build
ECHO Executable built
PAUSE
ECHO Adding necessary pyc files
copy "needed pyc/*" build
ECHO Adding necessary resource files
copy /res build
ECHO All Building done!
PAUSE