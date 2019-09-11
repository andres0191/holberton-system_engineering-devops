NAME
    pwd - Print the name of the current working directory.

SYNOPSIS
    pwd [-LP]

DESCRIPTION
    Print the name of the current working directory.
    
    Options:
      -L	print the value of $PWD if it names the current working
    	directory
      -P	print the physical directory, without any symbolic links
    
    By default, `pwd' behaves as if `-L' were specified.
    
    Exit Status:
    Returns 0 unless an invalid option is given or the current directory
    cannot be read.

SEE ALSO
    bash(1)

IMPLEMENTATION
    GNU bash, version 4.1.5(1)-release (i486-pc-linux-gnu)
    Copyright (C) 2009 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later 


