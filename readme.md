## Generate JSON files from browser logs

### Example

The following command will read the keys from `localhost-1645562326908.log` and `localhost-1645562326909.log` log files and create/append the keys inside the `es.json ` and `en.json` files.

```bash
python main.py --log_file localhost-1645562326908.log --log_file localhost-1645562326909.log --lang es.json --lang en.json
```

### Generate log file

Open dev console, right click and "Save as..."

![image](https://user-images.githubusercontent.com/29048245/155228918-28de4af2-a3d7-4e7e-bb65-b4baa3cbf52f.png)

