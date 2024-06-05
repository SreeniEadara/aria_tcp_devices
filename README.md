# WiFi Smart Plug Control from Aria
## IMPORTANT NOTES
Because the Shelly access point does not provide an internet connection, Windows may attempt to connect to other WiFi networks that are in range.
To avoid this behavior, do not save any other networks on the PC, and follow the instructions at this site:
https://www.ghacks.net/2023/04/24/how-to-prevent-windows-from-connecting-to-other-wireless-networks-automatically/
Additionally, check the "Connect even if the network is not broadcasting its name (SSID)" option to reconnect to the Shelly's WiFi in case of an interruption.

## Usage
1. Connect to the Shelly Plug's WiFi access point.
2. Run tcp_listen_toggle_shelly.py. It will run in the background, listening for a message from Aria on Port 18 (either ON or OFF) and will turn the Shelly Plug ON or OFF accordingly.
You may use aria_tcp_message_emulate.py for testing purposes. It will send two messages on port 18 (ON then OFF).