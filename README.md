# Deaths by COVID-19 in Bulgaria

Deaths by age, sex and comorbidities graphs and stats available from the data scraped from <https://www.mh.government.bg/>

## Usage

```bash
pip install -r requrements.txt
```
For scraping delete past data, set up the parameter in `PAGES_TO_SCRAPE` to reflect the amount of past data needed in `src/scraper.py` and run:

```bash
python src/scraper.py
```

Run jupyter lab 
```bash
jupyter lab
```
and execute all cells in the `CovidStats.ipynb` notebook.

## Output

To output graphs in nice html format use:
```bash
jupyter nbconvert  --no-input --no-prompt --to html CovidStats.ipynb
```

## Contributing
Pull requests are welcome. 