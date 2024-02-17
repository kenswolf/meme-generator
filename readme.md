# Meme Generator Project

## Overview 

This program generates memes by adding quotes to images.

## Setup 

#### Required Folders  
- A folder of images 
- A folder of various files (pdf, docx, txt, and csv) 
- A 'memes' folder in which to place generated meme files

#### Required 3rd party Python libraries<
 
- flask
- numpy
- pandas
- pillow (PIL)
- python-docx (docx)
- requests

## Command Line Invocation (CLI)

#### Syntax

    Optional command line parameters are ...

        path
            -p  <value> or --path <value>  
            value is a path to an image     
            When optional parameter is not provided, a randmom image is used

        body
            -b  <value> or --body <value>  
            value is a quoted text string, ie the body of a quote 
            When optional parameter is not provided, a randmom quote is used 

        author
            -a  <value> or --author <value>  
            value is a quoted text string, ie the name of the author of a quote
            When optional parameter is not provided, a randmom author is used  

            Note that, in some cases, using a random author value produces 
            misattributed quotes, but that is the requirement of this project.  
            The project rubric clearly states, about the cmd line arguements,  
            'If any argument is not defined, a random selection is used.'

#### Examples

        python3 meme.py 
        python3 meme.py -p  ./_data/photos/dog/xander_3.jpg 
        python3 meme.py -p  ./_data/photos/dog/xander_4.jpg -b "It is a far, far better..."  -a "Charles Dickens"
        python3 meme.py -b "The risk of a wrong decision..."  -a "Maimonides"

## Techincal Details 

#### Quote Engine

- Ingestors are used to read quotes from pdf, txt, csv, and docx files.
- Each file format has a file-type specific concrete class that implements an interface.
- A controller class also implements that interface, and it directs requests to the appropriate file-type specific classes.
- To parse a document the controller class implementation of that interface is invoked.
- The interface declaration is made in a class that is the parent class of all the interface implementing classes.  
- The parent class also has a utility class method.

#### Meme Generation

- In order to have text overlay on an image it must fit.  As a result not all memes use the same size text.  A combination of font size reduction and shifting of the starting location are used.  There are still going to be some quotes that will not fit though.
- The folder in which meme files are placed, is a child folder of where the code is executed.   This child folder is named 'memes'

#### Unit Tests
- Pytest is used.
- Tests are in multiple files with names that start with the word 'test'. 
- Test are not exhaustive but very helpful. 
  