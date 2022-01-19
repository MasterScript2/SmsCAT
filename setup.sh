echo -e "\e[1;33m \e"
figlet SmsCat
echo -e "\e[0;32m Creador: \e"+="\e[0;34mMasterScript\e"+="\e[0;31mMiGithub: \e"+="\e[0;35mhttps://github.com/MasterScript2\e"
sleep 0.2
echo -e "\e[0;36m<Numero telefonico>\e" $var1 
read var1
echo -e "\e[0;36m<Mensaje>\e" $var2
read var2
curl -X POST https://textbelt.com/text \
   --data-urlencode phone=$var1 \
   --data-urlencode message=$var2 \
   -d key=textbelt
echo -e "\e[0;31mSend--..\e"
sleep 1

