#!/bin/bash
os_checking(){
    . /etc/os-release
    case $ID in
        ubuntu) sudo apt install docker docker.io
        ;;
        arch) sudo pacman -S docker
        ;;
        darwin) brew install docker
        ;;
        debian) sudo apt install docker docker.io
        ;;
        *) echo "If windows you can see the documentation"
        ;;
    esac
}

running_docker() {
    docker build -t openseries:1.0 -f Dockerfile.openseries_test .
    docker run openseries:1.0
}

os_checking
running_docker