#!/bin/bash

PWD="."
CMD="app/app.py"

if [ ! -f "$PWD/$CMD" ]; then
    PWD="/var/app/"
    cd $PWD
fi

./$CMD
