@echo off
REM Check if one of the folders is named "new_folder"
if exist "folder1\new_folder" (
    if not exist "folder1\if_folder" (
        mkdir if_folder
        echo Created if_folder because folder1 contains new_folder.
    )
) else (
    echo No action taken because folder1 does not contain new_folder.
)

REM Check if if_folder exists
if not exist "folder1\if_folder" (
    mkdir hyperionDev
    echo Created hyperionDev because if_folder does not exist.
) else (
    echo No action taken because if_folder already exists.
)