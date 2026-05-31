from sec_edgar_downloader import Downloader
import os
import time


def download_sec_filing(ticker):

    try:

        os.makedirs("data/sec_filings", exist_ok=True)

        # IMPORTANT:
        # Use realistic company identity
        dl = Downloader(
            "data/sec_filings",
            "AI Financial Research Agent",
            "rithvikeshgoud01@gmail.com"
        )

        # Delay to reduce SEC blocking
        time.sleep(2)

        dl.get(
            "10-K",
            ticker,
            limit=1
        )

        return {
            "status": "success",
            "message": f"Downloaded latest 10-K filing for {ticker}"
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }