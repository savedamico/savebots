if command -v python3 &>/dev/null; then
    python3 -m pip3 install -r requirements.txt
    cd src
    python3 main.py
else
    echo Python 3 is not installed
fi


