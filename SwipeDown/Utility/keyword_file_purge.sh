#!/bin/bash

delete_file_recursively() {
        sudo apt purge "${entry}"
        KEYWORD=${entry}
        for entry in "$1"/*; do
                path=$(ls -lahR /* | grep "$KEYWORD")
                cd "$path" || exit
                shred -f ./*
        done
}