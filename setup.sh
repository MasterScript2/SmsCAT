echo -e "\e[1;33m \e"
figlet SmsCat
echo -e "\e[0;32m Creador: \e"+="\e[0;34mMasterScript\e"+="\e[0;31m MiGithub: \e"+="\e[0;35mhttps://github.com/MasterScript2\e"
sleep 0.2
echo -e "\e[0;31m \e"
read -p "NNumero: " non
read -p "Mensaje: " mes
curl -X POST https://textbelt.com/text \
   --data-urlencode phone=$non \
   --data-urlencode message=$mes \
   -d key=textbelt
echo -e "\e[0;31mSend--..\e"
sleep 1

