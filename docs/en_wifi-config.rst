Wi-Fi Network Configuration Guide
=================================

To connect the WTHM device to the internet, you need to configure the available Wi-Fi network information for it, including the network name (SSID) and password of the Wi-Fi AP.

.. note::
   The WTHM device supports IEEE 802.11 b/g/n standard 2.4 GHz band Wi-Fi networks and does not currently support 5G band Wi-Fi networks.

1. Enter Configuration Mode
---------------------------

On the WTHM device panel, **simultaneously** press and hold the **↑** and **↓** buttons for 3 seconds to enter the Wi-Fi configuration process.
After the LCD displays "Entering setup...", you can release the buttons.

.. figure:: /_static/images/up-down-hold.png
   :width: 180
   :alt: up-down-hold

When the LCD displays the **Wi-Fi AP QR code**, the device has successfully entered Wi-Fi configuration mode.

.. figure:: /_static/images/wifi-ap.png
   :width: 180
   :alt: Wi-Fi AP

2. Configure using Mobile Phone (or Pad)
----------------------------------------

Use your mobile phone (or Pad) to scan the QR code displayed on the device LCD.

.. note::
   Please use the iOS / Android **system-level** QR code scanning function. Common options include:

   - QR code scanning function in the native camera app
   - QR code scanning function in system ⚙️ **Settings** -> 🛜 **WLAN**
   - QR code scanning function in system browsers

If your phone prompts to connect to the 「🛜 WTHM-xxx」 Wi-Fi network during QR code scanning, please select **Yes**.

After your mobile phone successfully connects to the WTHM device's Wi-Fi network, most phone systems will automatically redirect to the configuration page.

.. figure:: /_static/images/wifi-config.jpeg
   :width: 360
   :alt: Wi-Fi config

After entering the Wi-Fi network name (SSID) and password that the device needs to connect to, click **Submit** to submit the configuration.

.. note::
   If your phone fails to redirect to the configuration page, please refer to this :doc:`detailed guide <en_detailed-instructions>`.

3. Check Wi-Fi Connection Status on Device
------------------------------------------

After completing the configuration, the WTHM device will automatically exit configuration mode and attempt to connect to the configured Wi-Fi network.

You can check the Wi-Fi network connection status on the device LCD screen.

.. note:: Wi-Fi Authentication Mode Support Information

   In standard configuration mode, this product supports the following Personal Security Protocols for Wi-Fi Access Points (AP):

   - WPA-Personal / WPA2-Personal (based on PSK, Pre-Shared Key)
   - WPA3-Personal (based on SAE, Simultaneous Authentication of Equals)
   - WPA2/WPA3 Mixed/Transition Mode

   For connecting to wireless networks using other authentication methods, such as:

   - Enterprise Authentication, e.g. WPA/WPA2/WPA3-Enterprise (based on 802.1X/EAP)
   - Open Networks (Open / Unsecured Networks)
   - Legacy WEP Protocol (Legacy WEP protocol)

   Please contact our technical support team for advanced configuration guidelines.