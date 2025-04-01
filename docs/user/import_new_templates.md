---
title: Import New Templates
layout: default
parent: Userguide
---

# Import new templates
On the homepage of the application, either press `Ctrl` + `I` or open the `File` Menu and click on `Import`

![The Homepage with the open file menu and markers for where to click]({% link user/import_button.png %})

## File selection
In the file selection dialog, you can select the filter `*.captura` to only show captura template files.
Internally the captura files are just zip files, so you can also change the file to also show `*.zip` files.
See this screenshot at number `2`.

![]({% link user/import_file_dialog.png %})

## Manual import of templates
1. Identify the path where the template library is located. [^1]
  - On Windows this is `C:\Users\<Your Username>\.captura\templates\`
  - On macOS this is: `/Users/<Your Username>/.captura/templates/`. Navigate to this folder by opening Finder. 
    Then use `Go` > `Go to Folder...` and enter the path
  - On Linux this is `${XDG_DATA_DIR}/.captura/templates/`, with `${XDG_DATA_DIR}` usually located at `~/.local/share/`
2. Navigate to the folder identified at step 1.
3. Create a new folder with the schema: `com.example.theme_name-x.y.z`.
  - Replace `com.example.theme_name` with the `id` found in the configuration file `config.yml`
  - Replace `x.y.z` with the `version` of the configuration file `config.yml`.
  - `version` and `id` **have to match** their values in the respective `config.yml` file, otherwise the final step of
    actually creating the LaTeX files will fail!
4. Copy all the relevant files into this folder. This should include:
  - A **valid** `config.yml` _(invalid configurations will be ignored by captura)_
  - All the needed LaTeX Source files
5. Launch captura and see your template on the home screen!

---

[^1]: In the future there will be a button in the app to open the library location

