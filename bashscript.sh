#!/bin/bash
set -eu

project_dir = "$HOME/OneDrive/Documents/BrewApp"

if [[ $(pwd) != ${project_dir} ]];
then
      echo -e "Not in project directory. Changing to directory"
      cd ${project_dir}
fi

if pytest;
then  
      git commit -am "${1}"
fi