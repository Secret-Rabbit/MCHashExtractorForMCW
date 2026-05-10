import requests, re
import tkinter as tk
from tkinter import ttk,messagebox
from urllib.parse import urlparse, unquote

# Getting links to JSON versions list
try:
    versionManifest = requests.get(
        "https://piston-meta.mojang.com/mc/game/version_manifest.json"
    ).json()
except Exception as e:
    messagebox.showerror("Error", f"Error getting manifest: {e}")
versionsList = []
for i in versionManifest["versions"]:
    versionsList.append(i["id"])

# Loading languages from a deleted JSON file and setting the maximum width for the widget
langsArray = requests.get(
    "https://raw.githubusercontent.com/Secret-Rabbit/MCHashExtractorForMCW/refs/heads/main/lang.json"
).json()
languagesList = []
widthTextBoard = 0
for i in langsArray:
    languagesList.append(i)
    widthTextBoard = max(
        max(
            len(langsArray[i]["clienthash"]),
            len(langsArray[i]["jsonhash"]),
            len(langsArray[i]["jsonfile"]),
            len(langsArray[i]["serverhash"]),
            len(langsArray[i]["clientmap"]),
            len(langsArray[i]["servermap"]),
        )
        + 42,
        widthTextBoard,
    )


# Function for getting values from nested dictionaries and lists along the path
def jget(obj, path, default=None):
    for key in path.split("."):
        if isinstance(obj, dict):
            obj = obj.get(key, default)
        elif isinstance(obj, list):
            try:
                obj = obj[int(key)]
            except:
                return default
        else:
            return default
    return obj


# Implementing data updates when changing the version
def updateVerManifest(event):
    selectedVersion = versionVar.get()
    for i in versionManifest["versions"]:
        global jsonhash, jsonfile, clienthash, clientmap, serverhash, servermap, exehash
        if i["id"] == selectedVersion:
            # Reading a version-related JSON file and then converting JSON strings into a Python object
            ver_url = i["url"]
            try:
                ver_json = requests.get(ver_url).json()
            except Exception as e:
                messagebox.showerror("Error", f"Error getting version manifest: {e}")
            pattern = r"/packages/([a-f0-9]{40})/([^/]+)$"
            match = re.search(pattern, ver_url)
            if match:
                jsonhash = match.group(1)
                jsonfile = match.group(2).removesuffix(".json")
            clienthash = jget(ver_json, "downloads.client.sha1", "")
            clientmap = jget(ver_json, "downloads.client_mappings.sha1", "")
            serverhash = jget(ver_json, "downloads.server.sha1", "")
            servermap = jget(ver_json, "downloads.server_mappings.sha1", "")
            exehash = jget(ver_json, "downloads.windows_server.sha1", "")
            if i["type"] == "release":
                jsonfile = ""
    return (
        jsonhash,
        jsonfile,
        clienthash,
        clientmap,
        serverhash,
        servermap,
        exehash,
        langSelect(""),
    )


# Implementing a language change
def langSelect(event):
    global jsonhashVarName, jsonfileVarName, clienthashVarName, clientmapVarName, serverhashVarName, servermapVarName, exehashVarName
    selectedLang = selectLang.get()
    jsonhashVarName = langsArray[selectedLang]["jsonhash"]
    jsonfileVarName = langsArray[selectedLang]["jsonfile"]
    clienthashVarName = langsArray[selectedLang]["clienthash"]
    clientmapVarName = langsArray[selectedLang]["clientmap"]
    serverhashVarName = langsArray[selectedLang]["serverhash"]
    servermapVarName = langsArray[selectedLang]["servermap"]
    exehashVarName = langsArray[selectedLang]["exehash"]
    return (
        jsonhashVarName,
        jsonfileVarName,
        clienthashVarName,
        clientmapVarName,
        serverhashVarName,
        servermapVarName,
        exehashVarName,
        updateWidget(),
    )


# Function for updating the text in the widget and building a string with parameters depending on the selected language
def updateWidget():
    global formattedOut
    formattedOut = ""
    if not jsonhashVarName == "" and not jsonhash == "":
        formattedOut += f"|{jsonhashVarName}={jsonhash}\n"
    if not jsonfileVarName == "" and not jsonfile == "" and jsonfileVar.get():
        formattedOut += f"|{jsonfileVarName}={jsonfile}\n"
    if not clienthashVarName == "" and not clienthash == "":
        formattedOut += f"|{clienthashVarName}={clienthash}\n"
    if not clientmapVarName == "" and not clientmap == "":
        formattedOut += f"|{clientmapVarName}={clientmap}\n"
    if not serverhashVarName == "" and not serverhash == "":
        formattedOut += f"|{serverhashVarName}={serverhash}\n"
    if not servermapVarName == "" and not servermap == "":
        formattedOut += f"|{servermapVarName}={servermap}\n"
    if not exehashVarName == "" and not exehash == "":
        formattedOut += f"|{exehashVarName}={exehash}"
    formattedOut = formattedOut.strip()
    # Updating widget content
    widget.config(state="normal")
    # Wipe
    widget.delete("1.0", "end")
    widget.insert("1.0", formattedOut)
    widget.config(state="disabled")
    return formattedOut


# Function for copying text to the clipboard
def copy2Clipboard():
    try:
        # Clear clipboard and append new text
        root.clipboard_clear()
        root.clipboard_append(formattedOut)
        root.update()  # Keeps clipboard content after app closes
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy text: {e}")


root = tk.Tk()
root.title("MCHashExtractor")
root.resizable(False, False)

frame = tk.Frame(root, bg="lightgreen")
frame.pack(fill="both")

# --- SELECT LANGUAGE ---
textLang = tk.Label(frame, text="Select language:", bg="lightgreen")
textLang.grid(row=0, column=0, padx=5, pady=5,sticky="w")
selectLang = tk.StringVar(value=languagesList[1])
langMenu = tk.OptionMenu(frame, selectLang, *languagesList, command=langSelect)
langMenu.grid(row=0, column=1, pady=5,sticky="ew")

# --- SELECT VERSION ---
textVersion = tk.Label(frame, text="Select version:", bg="lightgreen")
textVersion.grid(row=1, column=0, padx=5,sticky="w")
versionVar = tk.StringVar(value=versionsList[0])
versionMenu = ttk.Combobox(
    frame,
    values=versionsList,
    state="readonly",
    textvariable=versionVar
    )
versionMenu.grid(row=1, column=1,sticky="ew")
versionMenu.current(0)
versionMenu.bind("<<ComboboxSelected>>",updateVerManifest)

# --- Disable jsonfile name checkbox ---
jsonfileVar = tk.BooleanVar(value=True)
jsonfileCheck = tk.Checkbutton(frame, text="Name json file", variable=jsonfileVar, command=updateWidget, bg="lightgreen")
jsonfileCheck.grid(row=1, column=2, padx=5, pady=5)

# --- TEXT OUTPUT ---
widget = tk.Text(frame, width=widthTextBoard, height=6, wrap="word")
widget.grid(row=3, column=0, padx=5, columnspan=3)
updateVerManifest("")

# --- COPY BUTTON ---
copyButton = tk.Button(frame, text="Copy to Clipboard", command=copy2Clipboard)
copyButton.grid(row=4, column=0, padx=5, pady=5, columnspan=3, sticky="ew")

root.mainloop()