import yfinance as yf

# Ticker-Objekt für Tesla
tesla = yf.Ticker("TSLA")

# Historische Daten (maximal verfügbar)
data = tesla.history(period="max")

# Index zurücksetzen
data = data.reset_index()

# Erste 5 Zeilen anzeigen
print(data.head())