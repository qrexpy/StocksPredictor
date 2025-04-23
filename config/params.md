# Alpha Vantage API Parameters

## TIME_SERIES_INTRADAY

**Required:**
- `function`: The time series of your choice. In this case, `function=TIME_SERIES_INTRADAY`
- `symbol`: The name of the equity of your choice. For example: `symbol=IBM`
- `interval`: Time interval between two consecutive data points in the time series. Supported values: `1min`, `5min`, `15min`, `30min`, `60min`

**Optional:**
- `adjusted`: By default, `adjusted=true` and the output time series is adjusted by historical split and dividend events. Set `adjusted=false` to query raw (as-traded) intraday values.
- `extended_hours`: By default, `extended_hours=true` and the output time series will include both the regular trading hours and the extended (pre-market and post-market) trading hours. Set `extended_hours=false` to query regular trading hours only.
- `month`: By default, this parameter is not set and the API will return intraday data for the most recent days of trading. You can use the `month` parameter (in `YYYY-MM` format) to query a specific month in history.
- `outputsize`: By default, `outputsize=compact`. Strings `compact` and `full` are accepted. `compact` returns only the latest 100 data points; `full` returns trailing 30 days of the most recent intraday data if the `month` parameter is not specified, or the full intraday data for a specific month in history if the `month` parameter is specified.
- `datatype`: By default, `datatype=json`. Strings `json` and `csv` are accepted.

## TIME_SERIES_DAILY

**Required:**
- `function`: The time series of your choice. In this case, `function=TIME_SERIES_DAILY`
- `symbol`: The name of the equity of your choice. For example: `symbol=IBM`

**Optional:**
- `outputsize`: By default, `outputsize=compact`. Strings `compact` and `full` are accepted. `compact` returns only the latest 100 data points; `full` returns the full-length time series of 20+ years of historical data.
- `datatype`: By default, `datatype=json`. Strings `json` and `csv` are accepted.

## TIME_SERIES_DAILY_ADJUSTED

**Required:**
- `function`: The time series of your choice. In this case, `function=TIME_SERIES_DAILY_ADJUSTED`
- `symbol`: The name of the equity of your choice. For example: `symbol=IBM`

**Optional:**
- `outputsize`: By default, `outputsize=compact`. Strings `compact` and `full` are accepted. `compact` returns only the latest 100 data points; `full` returns the full-length time series of 20+ years of historical data.
- `datatype`: By default, `datatype=json`. Strings `json` and `csv` are accepted.

## TIME_SERIES_WEEKLY

**Required:**
- `function`: The time series of your choice. In this case, `function=TIME_SERIES_WEEKLY`
- `symbol`: The name of the equity of your choice. For example: `symbol=IBM`

**Optional:**
- `datatype`: By default, `datatype=json`. Strings `json` and `csv` are accepted.

## TIME_SERIES_WEEKLY_ADJUSTED

**Required:**
- `function`: The time series of your choice. In this case, `function=TIME_SERIES_WEEKLY_ADJUSTED`
- `symbol`: The name of the equity of your choice. For example: `symbol=IBM`

**Optional:**
- `datatype`: By default, `datatype=json`. Strings `json` and `csv` are accepted.

## TIME_SERIES_MONTHLY

**Required:**
- `function`: The time series of your choice. In this case, `function=TIME_SERIES_MONTHLY`
- `symbol`: The name of the equity of your choice. For example: `symbol=IBM`

**Optional:**
- `datatype`: By default, `datatype=json`. Strings `json` and `csv` are accepted.

## TIME_SERIES_MONTHLY_ADJUSTED

**Required:**
- `function`: The time series of your choice. In this case, `function=TIME_SERIES_MONTHLY_ADJUSTED`
- `symbol`: The name of the equity of your choice. For example: `symbol=IBM`

**Optional:**
- `datatype`: By default, `datatype=json`. Strings `json` and `csv` are accepted.

## GLOBAL_QUOTE

This endpoint returns the latest price and volume information for a ticker of your choice. You can specify one ticker per API request.

**Required:**
- `function`: The API function of your choice.
- `symbol`: The symbol of the global ticker of your choice. For example: `symbol=IBM`.

**Optional:**
- `datatype`: By default, `datatype=json`. Strings `json` and `csv` are accepted.

## REALTIME_BULK_QUOTES

This API returns realtime quotes for US-traded symbols in bulk, accepting up to 100 symbols per API request and covering both regular and extended (pre-market and post-market) trading hours.

**Required:**
- `function`: The time series of your choice. In this case, `function=REALTIME_BULK_QUOTES`
- `symbol`: Up to 100 symbols separated by comma. For example: `symbol=MSFT,AAPL,IBM`. If more than 100 symbols are provided, only the first 100 symbols will be honored as part of the API input.