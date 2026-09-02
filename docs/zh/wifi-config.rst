Wi-Fi配网说明
=============

为使 WTHM 设备联网，你需要为其配置当前可用的Wi-Fi网络信息，包括Wi-Fi AP的网络名称（SSID）和密码。

.. note::
   WTHM 设备支持 IEEE 802.11 b/g/n 标准2.4 GHz 频段 Wi-Fi网络，暂不支持5G 频段 Wi-Fi网络。

1. 进入配网模式
---------------

在 WTHM 设备面板上 **同时** 按住 **↑** 和 **↓** 按键3秒钟进入Wi-Fi配网流程。
当液晶屏显示 "Entering setup..." 后可松开按键。

.. figure:: /_static/images/up-down-hold.png
   :width: 180
   :alt: up-down-hold

当液晶屏显示 **Wi-Fi AP 二维码** 时表示设备已成功进入Wi-Fi配网模式。

.. figure:: /_static/images/wifi-ap.png
   :width: 180
   :alt: Wi-Fi AP

2. 使用手机（或Pad）进行配网
----------------------------

用手机（或Pad）扫描设备液晶屏上显示的二维码。

.. note::
   请使用 iOS / Android **系统级** 二维码扫描功能，常见可选的有：

   - 系统原生相机应用里的二维码扫描功能
   - 系统 ⚙️  **设置** -> 🛜 **WLAN** 里的二维码扫描功能
   - 系统浏览器里的二维码扫描功能

扫描二维码过程手机系统如有提示连接 「🛜 WTHM-xxx」 Wi-Fi网络的选项，请选择 **是** 。

手机成功连接上 WTHM 设备的Wi-Fi网络后，大部分手机系统会自动跳转到配置页面。

.. figure:: /_static/images/wifi-config.jpg
   :width: 360
   :alt: Wi-Fi config

在配置页面里输入设备所要连接的Wi-Fi网络名称（SSID）和密码后，点击 **Submit** 提交配置。

**WPA Enterprise（企业级）Wi-Fi 配置**

如需连接采用 WPA-Enterprise 安全认证的无线网络，在配置页面点击底部的 **"🏢 Need Enterprise/802.1X config?"** 链接，或点击右上角 **Menu** 菜单选择 **WiFi Enterprise** 项，可切换到企业级Wi-Fi配置页面。

.. figure:: /_static/images/wifi-config-enterprise.jpg
   :width: 360
   :alt: Enterprise Wi-Fi config

在企业级Wi-Fi配置页面中，需要填写以下信息：

- **Wi-Fi Name (SSID)**：选择或输入企业级Wi-Fi网络名称
- **Username (Identity)**：输入网络账户（身份标识）
- **Password**：输入网络密码
- **Advanced EAP Settings**：点击可展开高级EAP设置（如需要）

填写完成后，点击 **Submit** 提交配置。

.. note::
   如你的手机未能正常跳转到配置页面，请参考下文 **4. 详细步骤：手动打开配置页面** 部分。

3. 设备上查看Wi-Fi连接状态
--------------------------

完成配网操作后 WTHM 设备会自动退出配网模式，并尝试连接所配置的Wi-Fi网络。

你可在设备液晶屏幕上查看Wi-Fi网络连接状态。

.. note:: Wi-Fi 认证模式支持说明

   本产品在标准配网模式下，默认支持采用以下个人级安全协议 (Personal Security Protocols) 的 Wi-Fi 接入点 (AP)：

   - WPA-Personal / WPA2-Personal (基于 PSK, Pre-Shared Key)
   - WPA3-Personal (基于 SAE, Simultaneous Authentication of Equals)
   - WPA2/WPA3 混合/过渡模式 (Mixed/Transition Mode)

   对于企业级认证 (Enterprise Authentication)，如 WPA/WPA2/WPA3-Enterprise (基于 802.1X/EAP)，
   请参考上文 **WPA Enterprise（企业级）Wi-Fi 配置** 部分进行配置。

   对于其他认证方式（如开放网络、旧式 WEP 协议等），请联系我们的技术支持团队以获取帮助。

4. 详细步骤：手动打开配置页面
-----------------------------

手机（或Pad，下同）扫描设备液晶屏上显示的二维码这一操作，实质上是先让手机连接 WTHM 设备的 Wi-Fi 网络，之后依赖手机系统的自动检测网络功能跳转到配置页面，从而完成配网流程。

如你的手机未能正常跳转到配置页面，请按照如下详细步骤操作：

1. 请确认手机成功连接上 WTHM 设备的Wi-Fi网络，这是配网流程得以正确工作的 **前置条件** 。可在手机的 **设置** -> **WLAN** 配置页面中查看手机当前所连接的Wi-Fi网络名称是否是 ``WTHM-xxx`` 这一网络。如不是，请选择下列操作之一：

   - 在该 **WLAN** 配置页中使用扫码功能扫描设备液晶屏上二维码完成网络连接。
   - 在 *可用网络* 列表里手动选择连接 ``WTHM-xxx`` 网络，密码为 ``wangkong``。

2. 确认手机当前已连接上 ``WTHM-xxx`` Wi-Fi 网络这一前提下，查看该网络名下方是否有 `需要认证/登录` 之类的提示信息，或是查看系统提示栏是否有 `登录到WLAN网络` 之类提示信息。点击该 `认证/登录` 提示，触发系统弹出配置页面。

3. 如上面的步骤仍未能触发系统弹出配置页面，请手动打开 **系统浏览器** ，在浏览器的地址栏手动输入 ``http://192.168.100.1`` ，此时浏览器会加载并显示配置页面。
