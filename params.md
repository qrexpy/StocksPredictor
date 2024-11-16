TIME_SERIES_INTRADAY:

API Parameters ❚ Required: function

The time series of your choice. In this case, function=TIME_SERIES_INTRADAY

❚ Required: symbol

The name of the equity of your choice. For example: symbol=IBM

❚ Required: interval

Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min

❚ Optional: adjusted

By default, adjusted=true and the output time series is adjusted by historical split and dividend events. Set adjusted=false to query raw (as-traded) intraday values.

❚ Optional: extended_hours

By default, extended_hours=true and the output time series will include both the regular trading hours and the extended (pre-market and post-market) trading hours (4:00am to 8:00pm Eastern Time for the US market). Set extended_hours=false to query regular trading hours (9:30am to 4:00pm US Eastern Time) only.

❚ Optional: month

By default, this parameter is not set and the API will return intraday data for the most recent days of trading. You can use the month parameter (in YYYY-MM format) to query a specific month in history. For example, month=2009-01. Any month in the last 20+ years since 2000-01 (January 2000) is supported.

❚ Optional: outputsize

By default, outputsize=compact. Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points in the intraday time series; full returns trailing 30 days of the most recent intraday data if the month parameter (see above) is not specified, or the full intraday data for a specific month in history if the month parameter is specified. The "compact" option is recommended if you would like to reduce the data size of each API call.

❚ Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

TIME_SERIES_DAILY:

API Parameters ❚ Required: function

The time series of your choice. In this case, function=TIME_SERIES_DAILY

❚ Required: symbol

The name of the equity of your choice. For example: symbol=IBM

❚ Optional: outputsize

By default, outputsize=compact. Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points; full returns the full-length time series of 20+ years of historical data. The "compact" option is recommended if you would like to reduce the data size of each API call.

❚ Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

TIME_SERIES_DAILY_ADJUSTED:

API Parameters ❚ Required: function

The time series of your choice. In this case, function=TIME_SERIES_DAILY_ADJUSTED

❚ Required: symbol

The name of the equity of your choice. For example: symbol=IBM

❚ Optional: outputsize

By default, outputsize=compact. Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points; full returns the full-length time series of 20+ years of historical data. The "compact" option is recommended if you would like to reduce the data size of each API call.

❚ Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

TIME_SERIES_WEEKLY

API Parameters ❚ Required: function

The time series of your choice. In this case, function=TIME_SERIES_WEEKLY

❚ Required: symbol

The name of the equity of your choice. For example: symbol=IBM

❚ Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the weekly time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

TIME_SERIES_WEEKLY_ADJUSTED

API Parameters ❚ Required: function

The time series of your choice. In this case, function=TIME_SERIES_WEEKLY_ADJUSTED

❚ Required: symbol

The name of the equity of your choice. For example: symbol=IBM

❚ Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the weekly time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

TIME_SERIES_MONTHLY

API Parameters ❚ Required: function

The time series of your choice. In this case, function=TIME_SERIES_MONTHLY

❚ Required: symbol

The name of the equity of your choice. For example: symbol=IBM

❚ Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the monthly time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

TIME_SERIES_MONTHLY_ADJUSTED

API Parameters ❚ Required: function

The time series of your choice. In this case, function=TIME_SERIES_MONTHLY_ADJUSTED

❚ Required: symbol

The name of the equity of your choice. For example: symbol=IBM

❚ Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the monthly time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

GLOBAL_QUOTE

This endpoint returns the latest price and volume information for a ticker of your choice. You can specify one ticker per API request.

If you would like to query a large universe of tickers in bulk, you may want to try out our Realtime Bulk Quotes API, which accepts up to 100 tickers per API request.

API Parameters ❚ Required: function

The API function of your choice.

❚ Required: symbol

The symbol of the global ticker of your choice. For example: symbol=IBM.

❚ Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the quote data in JSON format; csv returns the quote data as a CSV (comma separated value) file.

REALTIME_BULK_QUOTES

This API returns realtime quotes for US-traded symbols in bulk, accepting up to 100 symbols per API request and covering both regular and extended (pre-market and post-market) trading hours. You can use this endpoint as a high-throughput alternative to the Global Quote API, which accepts one symbol per API request.

API Parameters ❚ Required: function

The time series of your choice. In this case, function=REALTIME_BULK_QUOTES

❚ Required: symbol

Up to 100 symbols separated by comma. For example: symbol=MSFT,AAPL,IBM. If more than 100 symbols are provided, only the first 100 symbols will be honored as part of the API input.