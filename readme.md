## Generate JSON translations files (vue-i18n) from browser logs

### Example

The following command will read the translations keys from `localhost-1645562326908.log` and `localhost-1645562326909.log` log files and create/append the keys inside the `es.json ` and `en.json` files.

```bash
python main.py --log_file localhost-1645562326908.log --log_file localhost-1645562326909.log --lang es.json --lang en.json
```

After that we have `en.json` and `es.json` with the new keys found inside the log files and the old keys already translated.

![image](https://user-images.githubusercontent.com/29048245/173318776-5ee031b5-aa5d-4c53-b456-a94120723f70.png)

### Generate log file

Open dev console, right click and "Save as..." and save the log file

![image](https://user-images.githubusercontent.com/29048245/155230226-d4bbdc7d-68c3-4d3b-a889-19b0518b5351.png)
