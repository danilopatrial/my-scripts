import os, time, logging, functools, socket
import requests, speedtest, psutil, wmi
from datetime import datetime
from pynvml import (
    nvmlInit, 
    nvmlDeviceGetHandleByIndex, 
    nvmlDeviceGetMemoryInfo, 
    nvmlDeviceGetUtilizationRates
)

# Run 'OpenHardwareMonitor.exe' if needed
monitor_path = r"C:\Users\Danilo Patrial\openhardwaremonitor-v0.9.6\OpenHardwareMonitor\OpenHardwareMonitor.exe"

if not any("OpenHardwareMonitor.exe" in p for p in os.popen('tasklist').read().splitlines()):
    os.startfile(monitor_path)
    time.sleep(2)  

w = wmi.WMI()
nvmlInit()

# Error Hanlder Decorator.
def Error_Handler(func: 'function') -> None:
    @functools.wraps(func)
    def wrappper(*args, **kwargs) -> None:
        try:
            result = func(*args, **kwargs)
            logging.debug(f'{func.__name__} returned {result}')
            return result
        except Exception as e:
            logging.error(f'[ERROR] {func.__name__}: {e}')
            return None
    return wrappper

@Error_Handler
def get_cpu_name() -> str:
    return w.Win32_Processor()[0].Name.strip()

@Error_Handler
def get_cpu_cores_physical() -> int:
    return psutil.cpu_count(logical=False)

@Error_Handler
def get_cpu_cores_logical() -> int:
    return psutil.cpu_count(logical=True)

@Error_Handler
def get_gpu_name() -> str:
    return w.Win32_VideoController()[0].Name.strip()

@Error_Handler
def get_gpu_vram_total() -> int:
    return nvmlDeviceGetMemoryInfo(nvmlDeviceGetHandleByIndex(0)).total // (1024 ** 2)

@Error_Handler
def get_ram_total() -> int:
    return int(psutil.virtual_memory().total / (1024 ** 2))

@Error_Handler
def get_public_ip() -> str:
    return requests.get('https://api64.ipify.org?format=json', timeout=5).json().get('ip')

@Error_Handler
def get_local_ip() -> str:
    return socket.gethostbyname(socket.gethostname())

@Error_Handler
def get_isp() -> str:
    return requests.get("http://ip-api.com/json/").json().get('isp')

@Error_Handler
def get_location() -> str:
    data = requests.get("http://ip-api.com/json/").json()
    return f'{data.get('country')}, {data.get('city')}'

@Error_Handler
def get_ping() -> float:
    st = speedtest.Speedtest()
    st.get_best_server()
    return st.results.ping

@Error_Handler
def get_download_speed() -> tuple:
    st = speedtest.Speedtest()
    st.get_best_server()
    return round(st.download() / 1_000_000, 2)

@Error_Handler
def get_upload_speed() -> float:
    st = speedtest.Speedtest()
    st.get_best_server()
    return round(st.upload() / 1_000_000, 2)

@Error_Handler
def get_wifi_networks() -> dict:
    return socket.gethostbyname_ex(socket.gethostname())[2]

@Error_Handler
def get_active_connections():
    return len(psutil.net_connections(kind='inet'))

@Error_Handler
def get_bytes_sent() -> float:
    return round(psutil.net_io_counters().bytes_sent / 1_000_000, 2)

@Error_Handler
def get_bytes_recived() -> float:
    return round(psutil.net_io_counters().bytes_recv / 1_000_000, 2)

@Error_Handler
def get_storage_total() -> str:
    return int(psutil.disk_usage(psutil.disk_partitions()[0].mountpoint).total / (1024 ** 2))

@Error_Handler
def get_motherboard_manufacturer() -> str:
    return w.Win32_BaseBoard()[0].Manufacturer

@Error_Handler
def get_motherboard_model() -> str:
    return w.Win32_BaseBoard()[0].Product

@Error_Handler
def get_bios_version() -> str:
    return w.Win32_BIOS()[0].SMBIOSBIOSVersion

@Error_Handler
def get_bios_release_date() -> str:
    date_part = w.Win32_BIOS()[0].ReleaseDate[:14]
    dt = datetime.strptime(date_part, "%Y%m%d%H%M%S")
    return dt.strftime("%d/%m/%Y")

@Error_Handler
def get_cpu_usage() -> int:
    return psutil.cpu_percent(interval=1)

@Error_Handler
def get_gpu_vram_free() -> int:
    return nvmlDeviceGetMemoryInfo(nvmlDeviceGetHandleByIndex(0)).free // (1024 ** 2)

@Error_Handler
def get_gpu_vram_used() -> int:
    return nvmlDeviceGetMemoryInfo(nvmlDeviceGetHandleByIndex(0)).used // (1024 ** 2)

@Error_Handler
def get_gpu_usage() -> int:
    return nvmlDeviceGetUtilizationRates(nvmlDeviceGetHandleByIndex(0)).gpu

@Error_Handler
def get_ram_used() -> int:
    return int(psutil.virtual_memory().used / (1024 ** 2))

@Error_Handler
def get_ram_free() -> int:
    return int(psutil.virtual_memory().available / (1024 ** 2))

@Error_Handler
def get_ram_usage() -> int:
    return psutil.virtual_memory().percent

@Error_Handler
def get_storage_used() -> int:
    return int(psutil.disk_usage(psutil.disk_partitions()[0].mountpoint).used / (1024 ** 2))

@Error_Handler
def get_storage_free() -> int:
    return int(psutil.disk_usage(psutil.disk_partitions()[0].mountpoint).free / (1024 ** 2))

@Error_Handler
def get_storage_usage() -> int:
    return psutil.disk_usage(psutil.disk_partitions()[0].mountpoint).percent

@Error_Handler
def get_system_uptime() -> int:
    def format_uptime(seconds: int) -> str:
        days, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        return f"{days}d {hours}h {minutes}m {seconds}s"
    return format_uptime(int(time.time() - psutil.boot_time()))