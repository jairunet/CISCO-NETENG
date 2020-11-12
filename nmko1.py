from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': 'x.x.x.x',
    'username': 'user',
    'password': 'password'
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': 'x.x.x.x',
    'username': 'user',
    'password': 'password'
}
iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': 'x.x.x.x',
    'username': 'user',
    'password': 'password'
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range(2, 21):
        print("Creating LFX VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name LFX_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
