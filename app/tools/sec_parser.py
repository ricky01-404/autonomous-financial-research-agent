import os


def read_sec_filing():

    base_path = "data/sec_filings"

    all_text = ""

    for root, dirs, files in os.walk(base_path):

        for file in files:

            if file.endswith(".txt"):

                file_path = os.path.join(root, file)

                try:

                    with open(
                        file_path,
                        "r",
                        encoding="utf-8",
                        errors="ignore"
                    ) as f:

                        text = f.read()

                        all_text += text + "\n"

                except Exception as e:

                    print(e)

    return all_text[:50000]