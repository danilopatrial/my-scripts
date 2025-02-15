import sys, time, logging, ctypes
from dataclasses import dataclass, field, fields
from .utils import *

# Run as admin
if not ctypes.windll.shell32.IsUserAnAdmin():
    time.sleep(1), logging.info('Running as Admin.')
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Set Logging Config
filename = f"pc-info/logging/omega-py_{datetime.now().strftime('%d%m')}.log"
log_format = '%(levelname)s - %(filename)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format, filename=filename, filemode='w')


@dataclass(frozen=True)
class InternetSpeed:
    download_speed_mbps:      float = field(default_factory=get_download_speed)
    upload_speed_mbps:        float = field(default_factory=get_upload_speed)

@dataclass(frozen=True)
class NetworkStaticInfo:
    public_ip:                str   = field(default_factory=get_public_ip)
    local_ip:                 str   = field(default_factory=get_local_ip)
    isp:                      str   = field(default_factory=get_isp)
    location:                 dict  = field(default_factory=get_location)

@dataclass(frozen=True)
class NetworkFloatingInfo:
    ping_ms:                  float = field(default_factory=get_ping)
    wifi_networks:            dict  = field(default_factory=get_wifi_networks)

    active_connections:       int   = field(default_factory=get_active_connections)
    bytes_sent_mb:            float = field(default_factory=get_bytes_sent)
    bytes_received_mb:        float = field(default_factory=get_bytes_recived)

@dataclass(frozen=True)
class HardwareStaticInfo:
    cpu_name:                 str   = field(default_factory=get_cpu_name)
    cpu_cores_physical:       int   = field(default_factory=get_cpu_cores_physical)
    cpu_cores_logical:        int   = field(default_factory=get_cpu_cores_logical)

    gpu_name:                 str   = field(default_factory=get_gpu_name)
    gpu_vram_total:           int   = field(default_factory=get_gpu_vram_total)

    ram_total:                int   = field(default_factory=get_ram_total)

    storage_total:            int   = field(default_factory=get_storage_total)

    motherboard_manufacturer: str   = field(default_factory=get_motherboard_manufacturer)
    motherboard_model:        str   = field(default_factory=get_motherboard_model)
    bios_version:             str   = field(default_factory=get_bios_version)
    bios_release_date:        str   = field(default_factory=get_bios_release_date)

    storage_used:             int   = field(default_factory=get_storage_used)
    storage_free:             int   = field(default_factory=get_storage_free)
    storage_usage_percent:    int   = field(default_factory=get_storage_usage)

@dataclass(frozen=True)
class HardwareFloatingInfo:
    cpu_usage_percent:        int   = field(default_factory=get_cpu_usage)
    cpu_frequency_mhz:        int   = NotImplemented
    cpu_temperature_c:        int   = NotImplemented

    gpu_usage_percent:        int   = field(default_factory=get_gpu_usage)
    gpu_temperature_c:        int   = NotImplemented
    gpu_frequency_mhz:        int   = NotImplemented
    gpu_vram_free:            int   = field(default_factory=get_gpu_vram_free)
    gpu_vram_used:            int   = field(default_factory=get_gpu_vram_used)

    ram_usage_percent:        int   = field(default_factory=get_ram_usage)
    ram_free:                 int   = field(default_factory=get_ram_free)
    ram_used:                 int   = field(default_factory=get_ram_used)

    system_uptime:            int   = field(default_factory=get_system_uptime)


def format_var_name(var: str) -> str:
    return var.replace('_', ' ').title() + ' '

def parse_data(info_cls: object) -> None:
    for var in fields(info_cls):
        print(f'\r{format_var_name(var.name).ljust(25, '.')} {getattr(info_cls, var.name)}', flush=True)
    print()

def parse_data(info_cls: object) -> None:
    message: str = ''
    for var in fields(info_cls):
        message += f'\n{format_var_name(var.name).ljust(25, '.')} {getattr(info_cls, var.name)}'
    return message

def stdout_main_data() -> None:
    while True:
        net = NetworkFloatingInfo()
        har = HardwareFloatingInfo()
        os.system('cls')
        print(f'\r{parse_data(net)}\n{parse_data(har)}', end='', flush=True)

def get_internet_speed() -> None:
    print('\rGetting Internet Speed...',end='', flush=True)
    internet = InternetSpeed()
    #os.system('cls')
    print(f'\rDownload: {internet.download_speed_mbps} mbps')
    print(f'Upload: {internet.upload_speed_mbps} mbps')
