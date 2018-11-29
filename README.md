# housefinder API
## API Usage
- documented with core api in schema.yml
- API endpoints
	- upload/<filename>/ POST
		- post a CSV file of listings to the app, headers required
	- listings/<int:pk>/
		- GET  get a listing by ID
		- PUT replace a listing with a new listing
		- PATCH edit a listing
	- listings/
		- POST create a new listing, fields listed in listings/models.py
		- GET get a list of Listings, available search params documented in schema.yml
		- example
		```
		http GET http://127.0.0.1:8000/listings/ min_last_sold_date=="2017-02-22" max_last_sold_date=="2018-02-22"
		```
## Assumptions
- price comes in format $/d\*K|M
- internal API, API would need more security and input verification to be fully implemented 
- no fields are mandatory

## Next Steps
if i were to flesh out this API more fully i'd add
- authentication
- duplicate detection on records(zillow ID if that is available for all enteries, address if not)
- impliment a location proximity search (ie within 10km of given address.  could get location info from google api)