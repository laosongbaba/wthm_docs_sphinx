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
   如你的手机未能正常跳转到配置页面，请参考这一 :doc:`详细指引 <detailed-instructions>` 。

3. 设备上查看Wi-Fi连接状态
--------------------------

完成配网操作后 WTHM 设备会自动退出配网模式，并尝试连接所配置的Wi-Fi网络。

你可在设备液晶屏幕上查看Wi-Fi网络连接状态。

.. note:: Wi-Fi 认证模式支持说明

   本产品在标准配网模式下，默认支持采用以下个人级安全协议 (Personal Security Protocols) 的 Wi-Fi 接入点 (AP)：
   
   - WPA-Personal / WPA2-Personal (基于 PSK, Pre-Shared Key)
   - WPA3-Personal (基于 SAE, Simultaneous Authentication of Equals)
   - WPA2/WPA3 混合/过渡模式 (Mixed/Transition Mode)

   如需连接至采用其他认证方式的无线网络，例如：

   - 企业级认证 (Enterprise Authentication)，如 WPA/WPA2/WPA3-Enterprise (基于 802.1X/EAP)
   - 开放网络 (Open / Unsecured Networks)
   - 旧式 WEP 协议 (Legacy WEP protocol)

   请联系我们的技术支持团队以获取高级配置指南。