# Alpha Vantage API Parameters

## TIME_SERIES_INTRADAY

This endpoint provides intraday time series data for a specified equity.

**Required Parameters:**
- `function`: The time series of your choice. Example: `function=TIME_SERIES_INTRADAY`
- `symbol`: The name of the equity of your choice. Example: `symbol=IBM`
- `interval`: Time interval between two consecutive data points in the time series. Supported values: `1min`, `5min`, `15min`, `30min`, `60min`. Example: `interval=5min`

**Optional Parameters:**
- `adjusted`: Adjusts the output time series by historical split and dividend events. Default: `adjusted=true`. Example: `adjusted=false`
- `extended_hours`: Includes both regular trading hours and extended trading hours. Default: `extended_hours=true`. Example: `extended_hours=false`
- `month`: Queries a specific month in history. Format: `YYYY-MM`. Example: `month=2023-01`
- `outputsize`: Specifies the amount of data returned. Default: `outputsize=compact`. Accepted values: `compact`, `full`. Example: `outputsize=full`
- `datatype`: Specifies the format of the data. Default: `datatype=json`. Accepted values: `json`, `csv`. Example: `datatype=csv`

---

## TIME_SERIES_DAILY

This endpoint provides daily time series data for a specified equity.

**Required Parameters:**
- `function`: The time series of your choice. Example: `function=TIME_SERIES_DAILY`
- `symbol`: The name of the equity of your choice. Example: `symbol=IBM`

**Optional Parameters:**
- `outputsize`: Specifies the amount of data returned. Default: `outputsize=compact`. Accepted values: `compact`, `full`. Example: `outputsize=full`
- `datatype`: Specifies the format of the data. Default: `datatype=json`. Accepted values: `json`, `csv`. Example: `datatype=csv`

---

## TIME_SERIES_DAILY_ADJUSTED

This endpoint provides adjusted daily time series data for a specified equity.

**Required Parameters:**
- `function`: The time series of your choice. Example: `function=TIME_SERIES_DAILY_ADJUSTED`
- `symbol`: The name of the equity of your choice. Example: `symbol=IBM`

**Optional Parameters:**
- `outputsize`: Specifies the amount of data returned. Default: `outputsize=compact`. Accepted values: `compact`, `full`. Example: `outputsize=full`
- `datatype`: Specifies the format of the data. Default: `datatype=json`. Accepted values: `json`, `csv`. Example: `datatype=csv`

---

## TIME_SERIES_WEEKLY

This endpoint provides weekly time series data for a specified equity.

**Required Parameters:**
- `function`: The time series of your choice. Example: `function=TIME_SERIES_WEEKLY`
- `symbol`: The name of the equity of your choice. Example: `symbol=IBM`

**Optional Parameters:**
- `datatype`: Specifies the format of the data. Default: `datatype=json`. Accepted values: `json`, `csv`. Example: `datatype=csv`

---

## TIME_SERIES_WEEKLY_ADJUSTED

This endpoint provides adjusted weekly time series data for a specified equity.

**Required Parameters:**
- `function`: The time series of your choice. Example: `function=TIME_SERIES_WEEKLY_ADJUSTED`
- `symbol`: The name of the equity of your choice. Example: `symbol=IBM`

**Optional Parameters:**
- `datatype`: Specifies the format of the data. Default: `datatype=json`. Accepted values: `json`, `csv`. Example: `datatype=csv`

---

## TIME_SERIES_MONTHLY

This endpoint provides monthly time series data for a specified equity.

**Required Parameters:**
- `function`: The time series of your choice. Example: `function=TIME_SERIES_MONTHLY`
- `symbol`: The name of the equity of your choice. Example: `symbol=IBM`

**Optional Parameters:**
- `datatype`: Specifies the format of the data. Default: `datatype=json`. Accepted values: `json`, `csv`. Example: `datatype=csv`

---

## TIME_SERIES_MONTHLY_ADJUSTED

This endpoint provides adjusted monthly time series data for a specified equity.

**Required Parameters:**
- `function`: The time series of your choice. Example: `function=TIME_SERIES_MONTHLY_ADJUSTED`
- `symbol`: The name of the equity of your choice. Example: `symbol=IBM`

**Optional Parameters:**
- `datatype`: Specifies the format of the data. Default: `datatype=json`. Accepted values: `json`, `csv`. Example: `datatype=csv`

---

## GLOBAL_QUOTE

This endpoint returns the latest price and volume information for a ticker of your choice.

**Required Parameters:**
- `function`: The API function of your choice. Example: `function=GLOBAL_QUOTE`
- `symbol`: The symbol of the global ticker of your choice. Example: `symbol=IBM`

**Optional Parameters:**
- `datatype`: Specifies the format of the data. Default: `datatype=json`. Accepted values: `json`, `csv`. Example: `datatype=csv`

---

## REALTIME_BULK_QUOTES

This endpoint returns realtime quotes for US-traded symbols in bulk, accepting up to 100 symbols per API request.

**Required Parameters:**
- `function`: The time series of your choice. Example: `function=REALTIME_BULK_QUOTES`
- `symbol`: Up to 100 symbols separated by commas. Example: `symbol=MSFT,AAPL,IBM`. If more than 100 symbols are provided, only the first 100 symbols will be honored as part of the API input.