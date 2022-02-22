## Generate JSON files from browser logs

### Example

The following command will read the keys from `localhost-1645562326908.log` and `localhost-1645562326909.log` log files and create/append the keys inside the `es.json ` and `en.json` files.

```bash
python main.py --log_file localhost-1645562326908.log --log_file localhost-1645562326909.log --lang es.json --lang en.json
```

### Generate log file

Open dev console, right click and "Save as..."

![image](https://user-images.githubusercontent.com/29048245/155230226-d4bbdc7d-68c3-4d3b-a889-19b0518b5351.png)
