## English

**Minecraft hash extractor for Minecraft Wiki** is a tool for obtaining the parameters of all versions available in the launcher for the [Infobox version template](https://minecraft.wiki/w/Template:Infobox_version) on the [Minecraft Wiki](https://minecraft.wiki/). **Requires a network connection at startup and after selecting a version.** Supports unique parameter names in different language sections.

### Prerequisites

This script requires you to have [**Python > 3.x.x**](https://www.python.org/downloads/) installed with the `requests` and `tkinter`library installed on your system.

- **Windows**: There is a ready-made exe.
- **Ubuntu/Debian**:

  ```bash
  sudo apt install python3 python3-tk python3-requests
  wget https://raw.githubusercontent.com/Secret-Rabbit/MCHashExtractorForMCW/refs/heads/main/MCHashExtractor.pyw
  ```

- For buld on Windows or launch via a .pyw file: tkinter is already built in. You must install `requests` with the `pip install requests` command.

### Usage

- **Windows**: [Download](https://github.com/Secret-Rabbit/MCHashExtractorForMCW/releases/latest/download/MCHashExtractor.exe) and launch!
- **Linux**: `python3 MCHashExtractor.pyw`

By default, English is set and the latest snapshot is selected. You can choose any combination.

**After selecting the version**, you **need to wait** a bit for the data to be uploaded.

Switching versions will not be very convenient if you need one of the earlier ones. Use the arrow buttons, it's more convenient to select.

[`lang.json`](https://github.com/Secret-Rabbit/MCHashExtractorForMCW/blob/main/lang.json) file contains template variable names for different language sections. If a value is empty (`""`), the variable will be removed. It is not included in the program and is downloaded from this repository every time it is launched.

## Русский

**Minecraft hash extractor for Minecraft Wiki** — это инструмент для получения параметров любых версий, доступных в лаунчере, для использования в шаблоне [Карточка версии](https://ru.minecraft.wiki/w/%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD:%D0%9A%D0%B0%D1%80%D1%82%D0%BE%D1%87%D0%BA%D0%B0%20%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8) на [Minecraft Wiki](https://ru.minecraft.wiki/). **Требуется подключение к интернету при запуске и после выбора версии.** Поддерживает уникальные имена параметров для разных разных языковых разделов.

### Требования

Для запуска необходимо установить [**Python > 3.x.x**](https://www.python.org/downloads/) с библиотеками `requests` и `tkinter`.

- **Windows**: Есть готовый exe-файл.
- **Ubuntu/Debian**:

  ```bash
  sudo apt install python3 python3-tk python3-requests
  wget https://raw.githubusercontent.com/Secret-Rabbit/MCHashExtractorForMCW/refs/heads/main/MCHashExtractor.pyw
  ```

- Для сборки под Windows или запуска через файл .pyw: tkinter уже встроен. Необходимо установить `requests` командой `pip install requests`.

### Использование

- **Windows**: [Скачать](https://github.com/Secret-Rabbit/MCHashExtractorForMCW/releases/latest/download/MCHashExtractor.exe) и запустить!
- **Linux**: `python3 MCHashExtractor.pyw`

По умолчанию выбран английский язык и последний снапшот. Вы можете выбрать любую комбинацию.

**После выбора версии** необходимо немного **подождать**, пока данные загрузятся.

Переключение между версиями может быть не очень удобным, если нужна одна из более ранних. Используйте кнопки со стрелками — это более удобный способ выбора.

Файл [`lang.json`](https://github.com/Secret-Rabbit/MCHashExtractorForMCW/blob/main/lang.json) содержит имена переменных шаблона для разных языковых разделов. Если значение пустое (`""`), переменная будет удалена. Файл не входит в состав программы и загружается из этого репозитория при каждом запуске.
