# WiFi Smart Plug Control from Aria
## IMPORTANT NOTES
Because the Shelly access point does not provide an internet connection, Windows may attempt to connect to other WiFi networks that are in range.
To avoid this behavior, do not save any other networks on the PC, and follow the instructions at this site:
https://www.ghacks.net/2023/04/24/how-to-prevent-windows-from-connecting-to-other-wireless-networks-automatically/
Additionally, check the "Connect even if the network is not broadcasting its name (SSID)" option to reconnect to the Shelly's WiFi in case of an interruption.

## Usage
1. Connect to the Shelly Plug's WiFi access point (it will be broadcast when first plugging it in without a load attached - look for the blinking blue light. If not seen, hold the button for 10 seconds to factory reset)
2. Run tcp_listen_toggle_shelly.py. It will create a TCP server on localhost running in the background, listening for a message from Aria on Port 18.
3. Send a message from Aria on Port 18 with either the text "ON" or "OFF". Aria should be configured as a TCP client. The plug should turn on or off accordingly. You may use aria_tcp_message_emulate.py for testing purposes. It will send two messages on port 18 (ON then OFF).
