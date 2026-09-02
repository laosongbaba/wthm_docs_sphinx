Wi-Fi Provisioning Guide
========================

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

.. figure:: /_static/images/wifi-config.jpg
   :width: 360
   :alt: Wi-Fi config

After entering the Wi-Fi network name (SSID) and password that the device needs to connect to, click **Submit** to submit the configuration.

**WPA Enterprise Wi-Fi Provisioning**

To connect to a wireless network using WPA-Enterprise security authentication, click the **"🏢 Need Enterprise/802.1X config?"** link at the bottom of the configuration page, or click the **Menu** in the upper right corner and select **WiFi Enterprise** to switch to the enterprise Wi-Fi configuration page.

.. figure:: /_static/images/wifi-config-enterprise.jpg
   :width: 360
   :alt: Enterprise Wi-Fi config

On the enterprise Wi-Fi configuration page, you need to fill in the following information:

- **Wi-Fi Name (SSID)**: Select or enter the enterprise Wi-Fi network name
- **Username (Identity)**: Enter the network account (identity)
- **Password**: Enter the network password
- **Advanced EAP Settings**: Click to expand advanced EAP settings (if needed)

After filling in the information, click **Submit** to submit the configuration.

.. note::
   If your phone fails to redirect to the configuration page, please refer to the **4. Detailed Steps: Manually Open the Configuration Page** section below.

3. Check Wi-Fi Connection Status on Device
------------------------------------------

After completing the configuration, the WTHM device will automatically exit configuration mode and attempt to connect to the configured Wi-Fi network.

You can check the Wi-Fi network connection status on the device LCD screen.

.. note:: Wi-Fi Authentication Mode Support Information

   In standard configuration mode, this product supports the following Personal Security Protocols for Wi-Fi Access Points (AP):

   - WPA-Personal / WPA2-Personal (based on PSK, Pre-Shared Key)
   - WPA3-Personal (based on SAE, Simultaneous Authentication of Equals)
   - WPA2/WPA3 Mixed/Transition Mode

   For Enterprise Authentication, such as WPA/WPA2/WPA3-Enterprise (based on 802.1X/EAP),
   please refer to the **WPA Enterprise Wi-Fi Provisioning** section above for configuration.

   For other authentication methods (such as open networks, legacy WEP protocol, etc.), please contact our technical support team for assistance.

4. Detailed Steps: Manually Open the Configuration Page
-------------------------------------------------------

The operation of scanning the QR code displayed on the device LCD screen with a mobile phone (or Pad, same below) essentially first connects the phone to the WTHM device's Wi-Fi network, and then relies on the phone's automatic network detection function to redirect to the configuration page, thus completing the network configuration process.

If your mobile phone fails to redirect to the configuration page normally, please follow the detailed steps below:

1. Please confirm that your phone successfully connects to the WTHM device's Wi-Fi network, as this is the **prerequisite** for the configuration process to work properly. You can check in the phone's **Settings** -> **WLAN** configuration page whether the current Wi-Fi network name is ``WTHM-xxx``. If not, please select one of the following operations:

   - Use the QR code scanning function on the **WLAN** configuration page to scan the QR code on the device LCD to complete network connection.
   - Manually select and connect to the ``WTHM-xxx`` network in the *Available Networks* list, password is ``wangkong``.

2. After confirming that the phone is currently connected to the ``WTHM-xxx`` Wi-Fi network, check whether there is a prompt such as `Authentication Required/Login` below the network name, or whether there is a prompt such as `Login to WLAN Network` in the system notification bar. Click the `Authentication/Login` prompt to trigger the system to pop up the configuration page.

3. If the steps above still fail to trigger the system to pop up the configuration page, please manually open the **System Browser**, and manually enter ``http://192.168.100.1`` in the browser's address bar. The browser will then load and display the configuration page.
