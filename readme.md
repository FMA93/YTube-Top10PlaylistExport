# YouTube Playlist Top 10 Exporter

This Python script extracts the top 10 videos from a YouTube playlist based on the number of views and exports the details to an Excel file. It utilizes the `pytube`, `pandas`, and `openpyxl` libraries for YouTube video extraction, data manipulation, and Excel file handling, respectively.

## Prerequisites

Before running the script, make sure you have Python installed on your system. You can download it from the official website: [Python Downloads](https://www.python.org/downloads/)

Install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt



Usage
Edit the playlist_url variable in the script with the URL of the YouTube playlist you want to process.

Run the script using the following command:

python export_top_10.py

The script will extract the top 10 videos from the playlist based on the number of views and export the details to an Excel file named top_10_playlist.xlsx.


Customization
You can change the number of top videos to export by modifying the head method on the DataFrame. For example, if you want the top 5 videos, change top_10_df = df.head(10) to top_5_df = df.head(5).

You can customize the name of the output Excel file by changing the excel_file variable.


License
This project is licensed under the MIT License - see the LICENSE file for details.


Acknowledgments
This project uses the pytube library for YouTube video extraction. You can find the library here.

It also uses pandas for data manipulation. You can find the library here.


Excel file handling is done with the openpyxl library. You can find the library here.

Feel free to contribute to the project and report any issues or suggestions!