# Pc-Info

## Description
This is the backend code for a future project tha i'am planning to do. I will create a nice GUI and it should look good. For now im using it as part of my scripts.

Once you run it, it should look something like this:
```bash
Ping Ms ................. 18.672
Wifi Networks ........... []
Active Connections ...... 200
Bytes Sent Mb ........... 640.26
Bytes Received Mb ....... 8634.79

Cpu Usage Percent ....... 10.1
Cpu Frequency Mhz ....... NotImplemented
Cpu Temperature C ....... NotImplemented
Gpu Usage Percent ....... 1
Gpu Temperature C ....... NotImplemented
Gpu Frequency Mhz ....... NotImplemented
Gpu Vram Free ........... 5163
Gpu Vram Used ........... 977
Ram Usage Percent ....... 44.4
Ram Free ................ 13498
Ram Used ................ 10781
System Uptime ........... 1d 1h 29m 56s
```


## Installation
1. Clone this repository or download the script.
2. Ensure you have Python installed on your system.
3. Ensure you have Open Hardware Monitor on your system
4. Also need to change the `monitor_path` on `utils.py`

## Usage
Run the script using Python:
```bash
python -m pc-info
```

### Command-line Options
- `--speedtest` : Gets the your current internet speed in mbps.

Example:
```bash
python -m pc-info --speedtest
```

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

## Autor
Danilo Patrial

