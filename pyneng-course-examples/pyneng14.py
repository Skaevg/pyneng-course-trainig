def connect(device_type, host, username, password, secret, command):
    print(f"Подключаемся к {host}")
    print(f"Отправляем команду {command}")

devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.20.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.12.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
]
for dev in devices:
    print(dev)
    connect(device_type=dev["device_type"], username=dev["username"],host=dev["host"], password=dev["password"], secret=dev["secret"], command="sh run"
    )
    # connect(**dev, command="sh run")
