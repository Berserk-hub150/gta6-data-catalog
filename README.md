# GTA VI Data Catalog

**Need a region name, a stable ID and a source for your map?** Six Leonida regions are available in one searchable JSON file, with a CSV export for spreadsheets.

## Look up Vice City

```sh
python catalog.py --search vice
python catalog.py --csv > regions.csv
```

The first command returns the record with ID `vice-city`. The second writes all six records with columns `id,name,kind,source`. Both use the Python standard library.

[Browse the region records](data/regions.json) · [Open the official GTA VI reference](https://www.rockstargames.com/VI)

## Add a sourced record

Give the entry a unique ID, a display name, a kind and a direct HTTPS source. Run `python catalog.py` to validate the collection. Missing fields, invalid source URLs and duplicate IDs cause a validation error. To check another file, pass `--input your-data.json`.

This is a collection of public references. A game installation is unnecessary.

---

[Explore the GTA VI project collection](https://github.com/Berserk-hub150/gta6-resource-index) · Independent fan project. Grand Theft Auto is a trademark of its respective owners.
