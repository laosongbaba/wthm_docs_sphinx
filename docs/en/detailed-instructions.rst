Wi-Fi Configuration Detailed Guide
==================================

The operation of scanning the QR code displayed on the device LCD screen with a mobile phone (or Pad, same below) essentially first connects the phone to the WTHM device's Wi-Fi network, and then relies on the phone's automatic network detection function to redirect to the configuration page, thus completing the network configuration process.

If your mobile phone fails to redirect to the configuration page normally, please follow the detailed steps below:

1. Please confirm that your phone successfully connects to the WTHM device's Wi-Fi network, as this is the **prerequisite** for the configuration process to work properly. You can check in the phone's **Settings** -> **WLAN** configuration page whether the current Wi-Fi network name is ``WTHM-xxx``. If not, please select one of the following operations:

   - Use the QR code scanning function on the **WLAN** configuration page to scan the QR code on the device LCD to complete network connection.
   - Manually select and connect to the ``WTHM-xxx`` network in the *Available Networks* list, password is ``wangkong``.

2. After confirming that the phone is currently connected to the ``WTHM-xxx`` Wi-Fi network, check whether there is a prompt such as `Authentication Required/Login` below the network name, or whether there is a prompt such as `Login to WLAN Network` in the system notification bar. Click the `Authentication/Login` prompt to trigger the system to pop up the configuration page.

3. If the steps above still fail to trigger the system to pop up the configuration page, please manually open the **System Browser**, and manually enter ``http://192.168.100.1`` in the browser's address bar. The browser will then load and display the configuration page.

:doc:`Back <wifi-config>`
