#/bin/bash
clear

cat<< EOF
                   ___  _    _ _____    _____ _____  _____ _     
                  |_  || |  | |_   _|  |_   _|  _  ||  _  | |    
                    | || |  | | | |______| | | | | || | | | |    
                    | || |/\| | | |______| | | | | || | | | |    
                /\__/ /\  /\  / | |      | | \ \_/ /\ \_/ / |____
                \____/  \/  \/  \_/      \_/  \___/  \___/\_____/

    01101010 01110111 01110100 00101101 01110100 01101111 01101111 01101100 
 
         ＴＨＥ  ＰＯＷＥＲＦＵＬ  ＪＷＴ  ＥＸＰＬＯＩＴＥＲ  ＴＯＯＬ
         ______________________________________________________________                                                    
EOF

read -p "a) Use as a JWT secret key bruteforcer
b) Use as a JWT admin changer
(select a or b) >>" ab

 case $ab in
         a) echo ENABLING KEY CRACKER ...;;
         b) echo ENABLING ADMIN CHANGER ...;
         python3 src/Jwt_bypass.py
         exit
         
 esac
python3 src/secret_key_finder.py
