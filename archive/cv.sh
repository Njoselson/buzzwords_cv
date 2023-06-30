#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

if 
    [[ "${TRACE-0}" == "1" ]]; then 
    set -o xtrace; 
fi

if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
    echo 'Usage: ./cv.sh outfile -b

    This script writes your amazing CV to a plaintext file!
    outfile is name of file, ie test or cv
    -b flag fills empty space with buzzwords in white text!

'
    exit
fi

main() {
    WHITE='\033[1;37m'
    NC='\033[0m' # No Color
    echo "Gathering text from python"
    cv=$(python cv.py 2>&1)
    cowsay=$(cowsay -e ^^ -W 20 "Nathaniel Joselson
    Address line
    Phone number 
    ")
    
    flowers=$(cat flower.txt 2>&1)
    echo "putting together text and media "
    printf "$cowsay\n$cv\n$flowers" \
        | ./ansi2html.sh > ${1}.html
    echo "converting to PDF"
    wkhtmltopdf ${1}.html ${1}.pdf 

}

main "$@"

