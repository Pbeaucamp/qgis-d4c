### Plugin Data4Citizen Qgis

Manipulate your Data4Citizen datasets inside Qgis with D4C Plugin. Import, export, create and modify datasets directly from this plugin. Also connects to Open Data websites :

- Data.gouv.fr
- Data4Citizen
- CKAN/DKAN
- OpenDataSoft

To install :
Download the repository and add it to Qgis. In the toolbar, Extensions -> Install/Manage extensions -> Install from ZIP.

You can also find the plugin online : https://plugins.qgis.org/plugins/d4c_api/

Author : MSE @ BPM-Conseil

Version 1.8.0 (February 2024):

Added :

- Changed os.path to pathlib library to access files
- Radio buttons for alphabetical filtering in the search dataset window
- New connection interface
- More explicit Geo Columns buttons
- More explicit Metadata button
- In export, "changed" -> "search" (to avoid confusion)
- All URI data sources (PostGIS, Oracle ...) layers are now saved as a .geojson when exporting
- Added a searchbar for the tags in the search dataset window

Bug fixes :

- Private datasets wouldn't show up even with an auth account, solved
- Layout for the dataset list in search dataset window displaying uncorrectly after applying filters, solved
- Changing between "organizations" and "dataset" in the OpenData section would sometimes cause an error, solved
