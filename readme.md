## Generate JSON files from browser logs

## Example

Will read the keys from `localhost-1645562326908.log` and `localhost-1645562326909.log` files and create/append the keys inside the `es.json ` and `en.json` files.

```bash
python main.py --log_file localhost-1645562326908.log --log_file localhost-1645562326909.log --lang es.json --lang en.json
```
