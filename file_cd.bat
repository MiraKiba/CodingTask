REM Create three new folders
mkdir folder1
mkdir folder2
mkdir folder3

REM Navigate inside folder1 and create three new folders
cd folder1
mkdir subfolder1
mkdir subfolder2
mkdir subfolder3

REM Remove two of the folders created inside folder1
rmdir subfolder2
rmdir subfolder3

REM Navigate back to the root directory
cd ..