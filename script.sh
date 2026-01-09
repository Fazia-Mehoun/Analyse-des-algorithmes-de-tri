#!/bin/bash

cd src/

set -e   # Arrêter le script en cas d'erreur

echo "=============================="
echo "➡️  Mise à jour des paquets système"
echo "=============================="
if command -v apt >/dev/null 2>&1; then
    sudo apt update
    sudo apt install -y python3 python3-pip
elif command -v dnf >/dev/null 2>&1; then
    sudo dnf install -y python3 python3-pip
elif command -v yum >/dev/null 2>&1; then
    sudo yum install -y python3 python3-pip
elif command -v brew >/dev/null 2>&1; then
    brew install python3
else
    echo "⚠️  Impossible de détecter le gestionnaire de paquets."
    echo "Installez manuellement python3 et pip3 avant de relancer ce script."
    exit 1
fi

echo "=============================="
echo "➡️  Installation/Upgrade de pip et des dépendances Python"
echo "=============================="
python3 -m ensurepip --upgrade || true
python3 -m pip install --upgrade pip
python3 -m pip install pandas numpy matplotlib

echo "=============================="
echo "➡️  Lancement des expérimentations"
echo "=============================="



for valeur in 100 200 300 400 500 600 700 800 900 1000 2000 3000 4000 5000 6000 7000; do
    python3 experimentation.py analyse tout $valeur -n taux 0.5
done

python3 figureTaille.py

python3 experimentation.py effacer

for taux in $(seq 0.05 0.05 1.0 | sed 's/,/./g'); do
    python3 experimentation.py analyse tout 1000 -n taux $taux
done

python3 figureTaux.py

python3 experimentation.py effacer

for val in 0.1 0.3 0.5 0.7 0.9 1 1.2 1.4 1.5 1.7 1.9; do
    python3 experimentation.py analyse tout 1000 shannon 4 $val
done

python3 figureShannon.py

